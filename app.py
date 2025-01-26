from functools import reduce


STARTING_MESSAGE = "Starting mean/medium script..."
NUMBER_PROMPT = "Please enter each number, When finished press enter"
FUNCTION_PROMPT = (
    "What kind of operation whould you like?\n1.) Mean\n2.) Median\n3.) Mode"
)


# Returns the mean of a list of floats and integers
def mean(array):
    return float(reduce(lambda x, y: x + y, array)) / len(array)


# Returns the median of a list of floats and integers
def median(array):
    return sorted(array)[len(array) // 2]


# Returns the mode of a list of floats and integers
def mode(array):
    numbers = {}  # Dict to keep track of repeating numbers

    for number in array:  # Loop through the list
        if number in numbers:  # The number has repeated
            numbers[number] += 1
        else:  # First time number has appeared in the loop
            numbers[number] = 1

    frequency = max(numbers.values())  # Returns the max value in the dict
    if frequency == 1:  # Return none if there has not been a repeating number
        return None

    # List comprehension that returns the list of numbers that are the most frequent repeating numbers.
    mode = [key for key, value in numbers.items() if value == frequency]
    # Format output if there is only one mode
    if len(mode) == 1:
        return mode[0]
    return mode


# Get user input
def get_input():
    iterable = []
    print(NUMBER_PROMPT)

    while True:
        number = input()

        # Convert input to a Integer or a Floating point number
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
    function_entries = {"1": "mean", "2": "median", "3": "mode"}

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
    )  # Call chosen operation from user with data provided by user.

    # Make the output look pretty.
    try:
        if answer.is_integer():
            print(f"The {func} of {iterable} is {int(answer)}")
    except AttributeError:
        print(f"The {func} of {iterable} is {answer}")


if __name__ == "__main__":
    main()
