def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_line = ""
    second_line = ""
    dashed_line = ""
    output_line = ""

    for problem in problems:
        number1, operator, number2 = problem.split()
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (number1.isdigit() and number2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(number1), len(number2)) + 2
        first_line += number1.rjust(width) + "    "
        second_line += operator + " " + number2.rjust(width - 2) + "    "
        dashed_line += "-" * width + "    "

        if show_answers:
            if operator == '+':
                output = str(int(number1) + int(number2))
            else:
                output = str(int(number1) - int(number2))
            output_line += output.rjust(width) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashed_line.rstrip()

    if show_answers:
        arranged_problems += "\n" + output_line.rstrip()

    return arranged_problems

## Tests ##
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')

print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')