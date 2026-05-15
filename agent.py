while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI: Bye 👋")
            break

        response = call_llm({"input": user_input})
        print("AI:", response["response"])

    except EOFError:
        print("\nAI: Input closed. Exiting safely 👋")
        break