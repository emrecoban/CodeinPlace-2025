def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left.")
        choice = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))
        while choice not in (1, 2):
            choice = int(input("Please enter 1 or 2: "))
        stones -= choice
        if stones > 0:
            print()
            player = 2 if player == 1 else 1
    winner = 2 if player == 1 else 1
    print(f"\n Player {winner} wins!")

if __name__ == '__main__':
    main()
