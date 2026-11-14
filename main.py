SEPARATOR = ";"

def readValues(filename):
    # Reads the numbers from the file and returns them as one string, e.g. "43;10"
    file = open(filename, "r", encoding="UTF-8")
    Values = ""
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            number = line.strip()
            if Values == "":
                Values = number
            else:
                Values = Values + SEPARATOR + number
    file.close()
    return Values

def Count(Numbers):
    count = 0
    for _ in Numbers:
        count +=1
    return count

def Sum(Numbers):
    total = 0
    for n in Numbers:
        total += int(n)
    return total

def Greatest(Numbers):
    greatest = 0
    for n in Numbers:
        if int(n) > greatest:
            greatest = int(n)
    return greatest

def Average(Numbers):
    sum = Sum(Numbers)
    count = Count(Numbers)
    average = sum / count
    return average

def analyseValues(Values):
    Numbers = Values.split(SEPARATOR)
    count = Count(Numbers)
    total = Sum(Numbers)
    greatest = Greatest(Numbers)
    average = float(Average(Numbers))

    result = "Count;Sum;Greatest;Average\n"
    result += f"{count};{total};{greatest};{average:.2f}\n"
    return result

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')

    Values = readValues(filename)
    result = analyseValues(Values)
    print(result)

    print("#### Number analysis - END ####")
    print("Program ending.")

main()