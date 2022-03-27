def day_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter the positive number")
        else:
            print("your input is negative number. Please enter the positive number")
    except ValueError:
        print("your input is not a number. Please enter the number")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, please enter the number and conversion units\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()
