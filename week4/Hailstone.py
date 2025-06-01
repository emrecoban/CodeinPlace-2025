def main():
    n = int(input("Enter a number: "))
    count = 0
    while n != 1:
        if n % 2 == 0:
            new_n = n // 2
            print(f"{n} is even, so I take half: {new_n}")
        else:
            new_n = 3 * n + 1
            print(f"{n} is odd, so I make 3n + 1: {new_n}")
        n = new_n
        count += 1
    #print(f"The process took {count} steps to reach 1.")

if __name__ == "__main__":
    main()
