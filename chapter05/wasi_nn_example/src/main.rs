use image::{ImageReader, imageops::Triangle};
use ndarray::Array;
use std::{env, fs};
use std::io::BufRead;

wit_bindgen::generate!({
    path: "wit/wasi-nn.wit",
    world: "ml",
});

use self::wasi::nn::{
    graph::{Graph, load, ExecutionTarget, GraphEncoding},
    tensor::{Tensor, TensorType},
};

fn main() {
    let image_path = env::args().nth(1).expect("Usage: <image_path>");

    // Load the ONNX model
    let model_data = fs::read("fixture/models/squeezenet1.1-7.onnx").unwrap();
    let graph = load(&[model_data], GraphEncoding::Onnx, ExecutionTarget::Cpu).unwrap();
    let exec_context = Graph::init_execution_context(&graph).unwrap();

    // Load labels
    let labels_data = fs::read("fixture/labels/squeezenet1.1-7.txt").unwrap();
    let class_labels: Vec<String> = labels_data.lines().map(|line| line.unwrap()).collect();

    // Prepare input tensor
    let data = image_to_tensor(&image_path, 224, 224);
    let dimensions = vec![1, 3, 224, 224];
    let tensor = Tensor::new(&dimensions, TensorType::Fp32, &data);
    exec_context.set_input("data", tensor).unwrap();

    // Execute inference
    exec_context.compute().unwrap();

    // Get and process output
    let output_data = exec_context.get_output("squeezenet0_flatten0_reshape0").unwrap().data();
    let output_f32 = bytes_to_f32_vec(&output_data);
    let output_array = Array::from_vec(output_f32);

    // Compute softmax
    let exp_output = output_array.mapv(f32::exp);
    let sum_exp = exp_output.sum();
    let softmax_output = exp_output / sum_exp;

    // Get top 3 predictions
    let mut probabilities: Vec<_> = softmax_output.iter().enumerate().collect();
    probabilities.sort_by(|a, b| b.1.partial_cmp(a.1).unwrap());

    for &(index, &probability) in probabilities.iter().take(3) {
        println!("Class: {} - Probability: {}", class_labels[index], probability);
    }
}

pub fn bytes_to_f32_vec(data: &[u8]) -> Vec<f32> {
    data.chunks_exact(4)
        .map(|c| f32::from_le_bytes(c.try_into().unwrap()))
        .collect()
}

fn image_to_tensor(path: &str, height: u32, width: u32) -> Vec<u8> {
    let img = ImageReader::open(path).unwrap().decode().unwrap();
    let resized_img = img.resize_exact(width, height, Triangle).to_rgb8();
    let raw_pixels = resized_img.into_raw();

    let mean = [0.485, 0.456, 0.406];
    let std = [0.229, 0.224, 0.225];

    let num_pixels = (height * width) as usize;
    let mut data_f32 = vec![0f32; num_pixels * 3];

    for i in 0..num_pixels {
        let idx = i * 3;
        let r = raw_pixels[idx] as f32 / 255.0;
        let g = raw_pixels[idx + 1] as f32 / 255.0;
        let b = raw_pixels[idx + 2] as f32 / 255.0;

        data_f32[i] = (r - mean[0]) / std[0];
        data_f32[i + num_pixels] = (g - mean[1]) / std[1];
        data_f32[i + 2 * num_pixels] = (b - mean[2]) / std[2];
    }

    let mut data_u8 = Vec::with_capacity(data_f32.len() * 4);
    for &v in &data_f32 {
        data_u8.extend_from_slice(&v.to_ne_bytes());
    }

    data_u8
}
