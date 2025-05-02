"""
Example of a Fill in the Blank program, like the one from the lesson.
The user will enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story.
"""

def main():
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

if __name__ == "__main__":
    main()
