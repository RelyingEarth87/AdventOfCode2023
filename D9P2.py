def calc_next(history):
    steps = {
        1: history.copy()
    }
    sequence = history
    counter = 2
    while sum(sequence) != 0:
        next_steps = []
        for i in range(len(sequence) - 1):
            diff = sequence[i+1] - sequence[i]
            next_steps.append(diff)
        sequence = next_steps
        steps[counter] = sequence
        counter += 1

    steps[len(steps)].insert(0, 0)
    counter = len(steps) - 1
    while counter > 0:
        diff = steps[counter+1][0]
        next_num = steps[counter][0] - diff
        steps[counter].insert(0, next_num) 
        counter -= 1

    return steps[1][0]
        

def main():
    file = open('inputD9.txt', 'r')

    lines = file.readlines()

    next_hists = []
    for line in lines:
        history = line.strip().split()
        history = [int(i) for i in history]
        next_hist = calc_next(history)
        next_hists.append(next_hist)
    
    print(sum(next_hists))


if __name__ == '__main__':
    main()