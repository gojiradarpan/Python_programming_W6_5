def NumbersList(filename):
    file = open(filename, "r", encoding="UTF-8")
    Numbers = ""
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            number = line.strip()
            if Numbers == "":
                Numbers = number
            else:
                Numbers = Numbers + ";" + number
    file.close()
    Numbers = Numbers.split(";")
    return Numbers

def Count(filename):
    count = 0
    Numbers = NumbersList(filename)
    for _ in Numbers:
        count +=1
    return count

def Sum(filename):
    total = 0
    for n in NumbersList(filename):
        total += int(n)
    return total

def Greatest(filename):
    Numbers = NumbersList(filename)
    greatest = 0
    for n in Numbers:
        if int(n) > greatest:
            greatest = int(n)
    return greatest

def Average(filename):
    sum = Sum(filename)
    count = Count(filename)
    average = sum / count
    return average

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")

    NumbersList(filename)
    count = Count(filename)
    total = Sum(filename)
    greatest = Greatest(filename)
    average = float(Average(filename))

    print(f"{count};{total};{greatest};{average:.2f}")

    print("\n#### Number analysis - END ####")
    print("Program ending.")

main()
