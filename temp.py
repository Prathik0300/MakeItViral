from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2,status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization','Key c3f7d810d60b46479b99e7730f97321a'),)


# Post inputs using python methods

# post_inputs_response = stub.PostInputs(
#     service_pb2.PostInputsRequest(
#         inputs=[
#             resources_pb2.Input(
#                 data = resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url="https://samples.clarifai.com/puppy.jpeg",
#                         allow_duplicate_url=True
#                     ),
#                     concepts=[resources_pb2.Concept(id="charlie",value=1.)]
#                 )
#             )
#         ]
#     ),metadata=metadata
# )


# if post_inputs_response.status.code != status_code_pb2.SUCCESS:
#     raise Exception("Post inputs failes, status: "+ post_inputs_response.status.description)

# Get inputs using python methods

# get_input_response = stub.GetInput(
#     service_pb2.GetInputRequest(input_id="5bdbbdb716b54a9bbd32b3273b974718"),
#     metadata = metadata
# )
# print("Get Input", get_input_response)
# print("###############################")
# print("Post Input",post_inputs_response)


# Predict an image via url using python methods and print the concepts and corresponding values.

# post_model_output = stub.PostModelOutputs(
#     service_pb2.PostModelOutputsRequest(
#         model_id="aaa03c23b3724a16a56b629203edc62c",
#         inputs=[
#             resources_pb2.Input(
#                 data = resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url="https://samples.clarifai.com/metro-north.jpg"
#                     )
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )

# if post_model_output.status.code != status_code_pb2.SUCCESS:
#     raise Exception("Post model outputs failed, status: ",post_model_output.status.description)

# op = post_model_output.outputs[0]
# print(post_model_output)
# print("\n\n\n\n")
# print("Predicted Concepts: \n\n\n\n")

# for concept in op.data.concepts:
#     print(concept.name,concept.value)


# ############################################
# Text prediction

# with open(r"C:\college\Personal\jpmc round 2.txt","r") as f:
#     file = f.read()

# post_text_model = stub.PostModelOutputs(
#     service_pb2.PostModelOutputsRequest(
#         model_id="aaa03c23b3724a16a56b629203edc62c",
#         inputs=[
#             resources_pb2.Input(
#                 data=resources_pb2.Data(
#                     text=resources_pb2.Text(
#                         raw="Butchart Gardens contains over 900 varieties of plants."
#                     )
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )

# if post_text_model.status.code != status_code_pb2.SUCCESS:
#     raise Exception("text model failed with status : ",post_text_model.status.description)

# op = post_text_model.outputs[0]

# for concept in op.data.concepts:
#     print(concept.name,concept.value)

# Custom Model/////////////////

# pmr = stub.PostInputs(
#     service_pb2.PostInputsRequest(
#         inputs=[
#             resources_pb2.Input(
#                 data=resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url="https://samples.clarifai.com/puppy.jpeg",
#                         allow_duplicate_url=True
#                     ),
#                     concepts=[
#                         resources_pb2.Concept(id="charlie",value=1),
#                         resources_pb2.Concept(id="our_wedding",value=0)
#                     ]
#                 )
#             ),
#             resources_pb2.Input(
#                 data=resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url="https://samples.clarifai.com/wedding.jpg",
#                         allow_duplicate_url=True
#                     ),
#                     concepts=[
#                         resources_pb2.Concept(id="our_wedding",value=1),
#                         resources_pb2.Concept(id="charlie",value=0),
#                         resources_pb2.Concept(id="cat",value=0)
#                     ]
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )

# if pmr.status.code != status_code_pb2.SUCCESS:
#     for obj in pmr.inputs:
#         print("INPUT : ",obj.id+" status")
#         print(obj.status)

#     raise Exception("inp failed status ", pmr.status.description)

# model = stub.PostModels(
#     service_pb2.PostModelsRequest(
#         models=[
#             resources_pb2.Model(
#                 id="pet",
#                 output_info=resources_pb2.OutputInfo(
#                     data=resources_pb2.Data(
#                         concepts=[resources_pb2.Concept(id="charlie",value=1)]
#                     ),
#                     output_config=resources_pb2.OutputConfig(
#                         concepts_mutually_exclusive=False,
#                         closed_environment=False
#                     )
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )

# if model.status.code != status_code_pb2.SUCCESS:
#     raise Exception("models failed", model.status.description)
# print(model)

# mod_ver = stub.PostModelVersions(
#     service_pb2.PostModelVersionsRequest(
#         model_id="pet"
#     ),
#     metadata=metadata
# )
# print(mod_ver)

# pred = stub.PostModelOutputs(
#     service_pb2.PostModelOutputsRequest(
#         model_id="pet",
#         version_id='c39c300f50d54519b8adc99f4c9e9377',
#         inputs=[
#             resources_pb2.Input(
#                 data = resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url="https://samples.clarifai.com/metro-north.jpg"
#                     )
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )

# if pred.status.code != status_code_pb2.SUCCESS:
#     raise Exception("pred failed ",pred.status.description)

# op = pred.outputs[0]
# print(op)
# for c in op.data.concepts:
#     print(c.name,c.value)


# Custom model for text data


