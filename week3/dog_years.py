# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    dog_age = int(input("Enter an age in calendar years: "))
    result = dog_age * 7.18
    print("That's " + str(result) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
