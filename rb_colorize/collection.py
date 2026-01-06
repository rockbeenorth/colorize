import math

from previews.generate_preview import generate_basic_css
from previews.css import render_css_colors

# def create_log_scale(num_steps, start=0):
#     if not 5 <= num_steps <= 17:
#         raise ValueError("Number of steps must be between 5 and 17")
#     if not 0 <= start <= 50:
#         raise ValueError("Start value must be between 0 and 50")

#     num_steps = num_steps + 1
#     result = [start]
#     max_value = 100
#     available_range = max_value - start

#     for i in range(1, num_steps):
#         progress = i / (num_steps - 1)
#         log_progress = math.log(1 + progress * (math.e - 1))
#         next_value = start + math.ceil(log_progress * available_range)
#         result.append(min(next_value, max_value))

#     return result[:-1]

# print(create_log_scale(7))
# print(create_log_scale(7, 45))
# print(create_log_scale(12, 50))
# generate_basic_css()

render_css_colors(h=213, s=6, steps=12, model='triadic', light_initial=5, dark_initial=95)
# render_css_colors(217, 100, steps=7)
# render_css_colors(31, 22, steps=7)
# #  model='triadic',


# import json
# from uuid import uuid4

# # Assuming these are imported from your existing code
# from tools.collection import Collection
# # from tools.color import Color

# def generate_figma_tokens(collections):
#     all_tokens = []

#     for collection in collections:
#         variable_collection_id = f"VariableCollectionId:{uuid4()}"
#         light_mode_id = f"{uuid4()}:0"
#         dark_mode_id = f"{uuid4()}:1"

#         variables = []

#         for light, dark in zip(collection.light_objects, collection.dark_objects):
#             variable_id = f"VariableID:{uuid4()}"
#             variable = {
#                 "id": variable_id,
#                 "name": light['var'],
#                 "description": "",
#                 "type": "COLOR",
#                 "valuesByMode": {
#                     light_mode_id: {
#                         "r": light['rgb'][0] / 255,
#                         "g": light['rgb'][1] / 255,
#                         "b": light['rgb'][2] / 255,
#                         "a": light.get('a', 1)
#                     },
#                     dark_mode_id: {
#                         "r": dark['rgb'][0] / 255,
#                         "g": dark['rgb'][1] / 255,
#                         "b": dark['rgb'][2] / 255,
#                         "a": dark.get('a', 1)
#                     }
#                 },
#                 "resolvedValuesByMode": {
#                     light_mode_id: {
#                         "resolvedValue": {
#                             "r": light['rgb'][0] / 255,
#                             "g": light['rgb'][1] / 255,
#                             "b": light['rgb'][2] / 255,
#                             "a": light.get('a', 1)
#                         },
#                         "alias": None
#                     },
#                     dark_mode_id: {
#                         "resolvedValue": {
#                             "r": dark['rgb'][0] / 255,
#                             "g": dark['rgb'][1] / 255,
#                             "b": dark['rgb'][2] / 255,
#                             "a": dark.get('a', 1)
#                         },
#                         "alias": None
#                     }
#                 },
#                 "scopes": ["ALL_SCOPES"],
#                 "hiddenFromPublishing": False,
#                 "codeSyntax": {}
#             }
#             variables.append(variable)

#         figma_tokens = {
#             "id": variable_collection_id,
#             "name": f"rb-color-{collection.name}",
#             "modes": {
#                 light_mode_id: "light",
#                 dark_mode_id: "dark"
#             },
#             "variableIds": [v['id'] for v in variables],
#             "variables": variables
#         }

#         all_tokens.append(figma_tokens)

#     return all_tokens

# # Example usage
# if __name__ == "__main__":
#     # Create your collections
#     arrow_collection = Collection("arrow", 217, s=100, steps=7)
#     vhred_collection = Collection("vh-red", 8, s=100, steps=7)
#     bg_collection = Collection("backgrounds", 31, 22, steps=7)
#     # Add more collections as needed

#     # List of all collections
#     all_collections = [arrow_collection, vhred_collection, bg_collection]

#     # Generate tokens for all collections
#     figma_tokens = generate_figma_tokens(all_collections)

#     # Print or save the JSON
#     print(json.dumps(figma_tokens, indent=2))

#     # Optionally, save to a file
#     with open('layers_for_figma.json', 'w') as f:
#         json.dump(figma_tokens, f, indent=2)