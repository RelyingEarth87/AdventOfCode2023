def main():
    firstAndLast = []
    file = open("inputD1.txt", "r")

    lines = file.readlines()

    for i in lines:
        numbers = []
        for j in i:
            if j.isnumeric():
                numbers.append(str(j))
        if numbers != []:
            data = numbers[0] + numbers[-1]
            firstAndLast.append(int(data))
    
    total = 0
    for i in firstAndLast:
        total += i
    print(total)

if __name__ == "__main__":
    main()
