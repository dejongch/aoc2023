histories = []
with open("input.txt", 'r') as file:
    for index, line in enumerate(file):
        histories.append([int(value) for value in line.strip().split()])

sum = 0

def get_value(levels, level, index):
    value = levels[level][index]
    if value is not None:
        return value
    value = get_value(levels, level-1, index+1) - get_value(levels, level-1, index)
    levels[level][index] = value
    return value

for history in histories:
    levels = [history]
    index = len(history) - 1
    new_number = history[index]
    while new_number != 0:
        sum+=new_number
        levels.append([None]*(index))
        index-=1
        new_number = get_value(levels, len(levels)-1, index)
        

print(sum)








# for history in histories:
#     levels = [history]
#     current_level = history

#     while not all(value == 0 for value in current_level):
#         next_level = []
#         for index, value in enumerate(current_level):
#             if index < len(current_level) - 1:
#                 next_level.append(current_level[index+1] - value)
#         levels.append(next_level)
#         current_level = next_level
    
