import random

def main():
    selected = int(input("How many sides does your dice have? "))
    finding = random.randint(1,selected)
    print("Your roll is " + str(finding))

if __name__ == '__main__':
    main()
