def main(number):
    sequence = []
    first_number, second_number = 0, 1

    if number >= 1:
        sequence.append(first_number)

    if number >= 2:
        sequence.append(second_number)
                          
    for i in range (2, number):
        result = first_number + second_number
        first_number, second_number = second_number, result
        sequence.append(result)

    for fibonacii_number in sequence:
        print (fibonacii_number)

    return sequence

if __name__ == '__main__':
    while True:
        try:
            number = int(input("choose the number of terms: "))
            if number < 0:
                raise ValueError("Non-negative term exist")
            break
        except ValueError as error:
            print(error)
    main(number)