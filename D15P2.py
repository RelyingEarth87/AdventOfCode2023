def do_hash(sequence):
    current_value = 0
    for char in sequence:
        value = ord(char)
        current_value += value
        current_value *= 17
        current_value = current_value % 256
    
    if current_value >= 256:
        raise ValueError
    
    return current_value

def hashmap(sequences):
    boxes = {}
    for i in range(255):
        boxes[i] = []


    for lens in sequences:
        if '=' in lens:
            index = lens.find('=')
            label = lens[0:index]
            focal_length = int(lens[index + 1:])
            box_num = do_hash(label)
            curr_lens = [label, focal_length]

            slot = 0
            while slot <= len(boxes[box_num]):
                box = boxes[box_num]

                if box == []:
                    box.append(curr_lens)
                    break
                elif label == box[slot][0]:
                    box[slot][1] = focal_length
                    break
                elif slot == len(box) - 1:
                    box.append(curr_lens)
                    break
                slot += 1
        elif '-' in lens:
            index = lens.find('-')
            label = lens[:index]
            box_num = do_hash(label)
            slot = 0
            while slot < len(boxes[box_num]):
                box = boxes[box_num]
                if box == []:
                    break
                elif label == box[slot][0]:
                    box.remove(box[slot])
                    break
                slot += 1

    hashmaps = []
    i = 0
    while i < len(boxes):
        box = boxes[i]
        lenses = box
        if lenses != []:
            curr_lens = 0
            while curr_lens < len(lenses):
                hashmap = (i + 1) * (curr_lens + 1) * lenses[curr_lens][1]
                hashmaps.append(hashmap)
                curr_lens += 1
        i += 1

    return hashmaps

def main():
    file = open('inputD15.txt', 'r')

    lines = file.readlines()
    sequences = lines[0].strip().split(',')
    
    hashmaps = hashmap(sequences)
    
    print(sum(hashmaps))


if __name__ == '__main__':
    main()
