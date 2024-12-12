import yaml


test_file = "surfline_data/1733983398/surf.yaml"


# file format:
#
# associated:
# ...
# data:
#   surf:
#   - surf:
#       humanRelation: Waist to chest
#       max: 4
#       min: 3
#       plus: false
#       raw:
#         max: 4.00098
#         min: 2.28068
#     timestamp: 1733904000
#     utcOffset: -8
#   - surf:
#       humanRelation: Waist to chest
#       max: 4
#       min: 3
#       plus: false
#       raw:
#         max: 3.90108
#         min: 2.24483
#     timestamp: 1733907600
#     utcOffset: -8


# Open and read the YAML file
with open(test_file, "r") as file:
    data = yaml.safe_load(file)

# Extract surf data
surf_data = data["data"]["surf"]

# Example of processing: print each surf entry with its timestamp
for surf in surf_data:
    print(f"Timestamp: {surf['timestamp']}, Surf Data: {surf['surf']}")
