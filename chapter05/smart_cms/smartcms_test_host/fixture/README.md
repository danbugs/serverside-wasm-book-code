# Note on models

I got the model inside `model_inputids_mod` (i.e., `model.onnx`) 
from here: https://huggingface.co/wellness10/tinystories_onnx 
(same place I got the `./tokenizer.json`). Then, I used 
`model_inputids_mod/main.py` to add an extra node to the model 
to make it accept a TensorType of Fp32 instead of I64 (which the
ONNX backend doesn't support) together with a cast node creating
`./modified_model.onnx`.