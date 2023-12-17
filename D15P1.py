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

def main():
    file = open('inputD15.txt', 'r')

    lines = file.readlines()
    sequences = lines[0].strip().split(',')
    
    hashes = []
    for sequence in sequences:
        current_hash = do_hash(sequence)
        hashes.append(current_hash)
    
    print(sum(hashes))

if __name__ == '__main__':
    main()
