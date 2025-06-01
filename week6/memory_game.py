import random

NUM_PAIRS = 3

def clear_terminal():
    for _ in range(20):
        print('\n')

def get_valid_index(displayed, first_index=None):
    while True:
        try:
            index = int(input("Enter an index: "))
            if index < 0 or index >= len(displayed):
                print("Invalid index. Try again.")
            elif displayed[index] != '*':
                print("This number has already been matched. Try again.")
            elif first_index is not None and index == first_index:
                print("You entered the same index twice. Try again.")
            else:
                return index
        except ValueError:
            print("Not a number. Try again.")

def main():
    
    truth = []
    for i in range(NUM_PAIRS):
        truth.extend([i, i])
    random.shuffle(truth)
    
    
    displayed = ['*'] * len(truth)
    
    while True:
        clear_terminal()
        print(displayed)
        
        
        if '*' not in displayed:
            print("Congratulations! You won!")
            break
        
        
        idx1 = get_valid_index(displayed)
        idx2 = get_valid_index(displayed, idx1)
        
        # Checking match
        if truth[idx1] == truth[idx2]:
            displayed[idx1] = truth[idx1]
            displayed[idx2] = truth[idx2]
            print("Match!")
        else:
            print(f"Value at index {idx1} is {truth[idx1]}")
            print(f"Value at index {idx2} is {truth[idx2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()
