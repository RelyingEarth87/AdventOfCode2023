import re

def main():
    firstAndLast = []
    file = open("inputD1.txt", "r")

    lines = file.readlines()

    integerStrings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for line in lines:
        finalNumbers = []
        stringIndexes = []
        stringIndexesUpdated = []
        indexes = []
        for char in range(len(line)):
            if line[char].isnumeric():
                indexes.append(char)
        for ints in integerStrings:
             index = [i.start() for i in re.finditer(ints, line)]
             stringIndexes.append(index)
        for num in stringIndexes:
            if num != []:
                stringIndexesUpdated.append(num)
        for i in stringIndexesUpdated:
            for j in i:
                indexes.append(j)

        sortedIndexes = sorted(indexes)
        for j in sortedIndexes:
            if line[j].isnumeric():
                finalNumbers.append(line[j])
            else:
                searchString = line[j] + line[j+1] + line[j+2]
                for k in range(len(integerStrings)):
                    if searchString in integerStrings[k]:
                        finalNumbers.append(k)

        data = str(finalNumbers[0]) + str(finalNumbers[-1])
        firstAndLast.append(data)
    
    total = 0
    for i in firstAndLast:
        total += int(i)
    
    print(total)





if __name__ == '__main__':
    main()
