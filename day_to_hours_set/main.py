calculation_to_units = 24
name_of_unit = "hours"


def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter the positive number")
        else:
            print("your input is negative number. Please enter the positive number")
    except ValueError:
        print("your input is not a number. Please enter the number")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, please enter the number of days as a list and I will convert it in hours\n")
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()
