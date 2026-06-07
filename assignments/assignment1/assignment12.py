def shutdown_computer():
    answer = input("Do you want to shutdown the computer? (yes/no): ")

    if answer.lower() == "yes":
        print("Shutting down...")

    elif answer.lower() == "no":
        print("Shutdown aborted.")

    else:
        print("Sorry, I didn't understand your answer.")

shutdown_computer()