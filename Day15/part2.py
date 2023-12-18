from pprint import pprint

items = []

with open("input.txt", 'r') as file:
    for line in file:
        items += line.strip().split(",")

boxes = [{'lenses': [], 'lens_indexes': {}} for _ in range(256)]

for item in items:
    box_index = 0
    lens_name, lens_value = None, None
    is_remove = False
    if item[-1] == "-":
        lens_name = item[:-1]
        is_remove = True
    else:
        lens_name, lens_value = item.split("=")
        lens_value = int(lens_value)
    for char in lens_name:
        box_index += ord(char)
        box_index = box_index * 17
        box_index = box_index % 256


    lens_index =  boxes[box_index]["lens_indexes"].get(lens_name)
    if is_remove:
        if lens_index is not None:
            boxes[box_index]["lenses"].pop(lens_index)
            boxes[box_index]["lens_indexes"][lens_name] = None
            for lens in boxes[box_index]["lenses"][lens_index:]:
                boxes[box_index]["lens_indexes"][lens["lens_name"]] -= 1
    else:
        if lens_index is not None:
            boxes[box_index]["lenses"][lens_index]["lens_value"] = lens_value
        else:
            boxes[box_index]["lenses"].append({
                "lens_name": lens_name,
                "lens_value": lens_value
            })
            boxes[box_index]["lens_indexes"][lens_name] = len(boxes[box_index]["lenses"]) - 1

sum = 0
for box_index, box in enumerate(boxes):
    for lens_index, lens in enumerate(box["lenses"]):
        sum += (box_index + 1) * (lens_index + 1) * lens["lens_value"]

print(sum)
