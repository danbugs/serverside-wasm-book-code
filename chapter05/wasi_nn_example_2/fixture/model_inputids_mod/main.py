# Simple script to modify the `input_ids` tensor input from
# an I64 tensor type to Fp32.
#
# This is needed because, right now, Wasmtime's ONNX backend
# only supports Fp32 for input.
import onnx
from onnx import helper, TensorProto

model = onnx.load('model.onnx')
graph = model.graph

input_tensor = None
for input in graph.input:
    if input.name == 'input_ids':
        input_tensor = input
        break

if input_tensor is None:
    raise ValueError("Input tensor 'input_ids' not found in the model.")

input_tensor.type.tensor_type.elem_type = TensorProto.FLOAT

cast_node = helper.make_node(
    'Cast',
    inputs=[input_tensor.name],            # Input is 'input_ids'
    outputs=['input_ids_int64'],           # Output is 'input_ids_int64'
    to=TensorProto.INT64,
    name='CastInputIdsToInt64'
)

graph.node.insert(0, cast_node)

# Get a list of all node names to identify the Cast node
cast_node_name = 'CastInputIdsToInt64'

for node in graph.node:
    if node.name != cast_node_name:
        for i, name in enumerate(node.input):
            if name == 'input_ids':
                node.input[i] = 'input_ids_int64'

onnx.save(model, 'modified_model.onnx')
onnx.checker.check_model(model)
