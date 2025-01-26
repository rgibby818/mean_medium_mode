from functools import reduce


STARTING_MESSAGE = "Starting mean/medium script..."
NUMBER_PROMPT = "Please enter each number, When finished press enter"
FUNCTION_PROMPT = "What kind of operation whould you like?\n1.) Mean\n2.) Median"


# Returns the mean of a list of floats and integers
def mean(array):
    return float(reduce(lambda x, y: x + y, array)) / len(array)


# Returns the median of a list of floats and integers
def median(array):
    return sorted(array)[len(array) // 2]


# Get user input
def get_input():
    iterable = []
    print(f"{NUMBER_PROMPT}")

    while True:
        number = input()

        # Convert input to a Integer or a Floating put number
        try:
            if float(number).is_integer():
                iterable.append(int(number))
            else:
                iterable.append(float(number))

        except ValueError:
            if number == "":
                if (
                    len(iterable) != 0
                ):  # If no input is recived, User is done entering inputs.
                    break
                print(
                    "No valid numbers inputted. To exit press CTRL + C"
                )  # User has not inputted any numbers. Reprompt
            else:
                print("Invalid input. Numbers only")  # Wrong input Loop again
    return iterable


# User picks what function to call mean or median
def get_function():
    function_entries = {"1": "mean", "2": "median"}

    print(f"{FUNCTION_PROMPT}")
    while True:
        function_type = input().lower()

        if function_type in function_entries.keys():  # If user does 1 or 2
            return function_entries[function_type]

        if function_type in function_entries.values():  # If user does mean or median
            return function_type

        print("Invalid option, please try again\n")
        print(FUNCTION_PROMPT)


def main():
    print(f"{STARTING_MESSAGE}")

    iterable, func = (
        get_input(),
        get_function(),
    )  # Gather list data and operation type from user.
    answer = globals()[func](
        iterable
    )  # Call choicen operation from user with data provided by user.

    # Make the output look pretty.
    if answer.is_integer():
        print(f"The {func} of {iterable} is {int(answer)}")
    else:
        print(f"The {func} of {iterable} is {answer}")


if __name__ == "__main__":
    main()
