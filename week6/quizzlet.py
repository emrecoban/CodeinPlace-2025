def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    
    # Loop through each word in the dictionary
    for english_word, spanish_translation in translations.items():
        # Ask the user for the Spanish translation
        user_answer = input(f"What is the Spanish translation for {english_word}? ")
        
        # Check if the answer is correct
        if user_answer.lower() == spanish_translation.lower():
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.")
        
        # Add blank line for visual clarity
        print()
    
    # Print final score
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")



if __name__ == '__main__':
    main()
