import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

if __name__ == '__main__':
    main()
