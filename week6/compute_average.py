def main():
    number_list = load_numbers_from_file("numbers.txt")
    # Calculate the average of the numbers
    if len(number_list) > 0:
        average = sum(number_list) / len(number_list)
        print(f"Average: {average}")
    else:
        print("No numbers found in file")


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()
