from ai import call_gpt

def main():
    get_name = input("Enter your name: ")
    get_topic = input("Enter a topic: ")
    print("Creating your haiku...")

    send_to_ai = call_gpt(f"Write a haiku. Name: {get_name} Topic: {get_topic}")
    print(send_to_ai)


if __name__ == "__main__":
    main()
