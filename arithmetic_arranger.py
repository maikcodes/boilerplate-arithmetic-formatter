import re


def check_operation(problem):
    pattern = r'[-+]'
    if not re.search(pattern, problem):       
        return (False, problem)
    
    return (True, problem.split())


def check_operations(problems):
    array_problems = []
    for problem in problems:
        valid_operation, array_problem = check_operation(problem)
        if not valid_operation:
            return False
        
        array_problems.append(array_problem)

    return array_problems
    
def check_digits(array_problems):
    max_digits = 4
    int_array_problems = []
    for problem in array_problems:
        first_number = problem[0]
        second_number = problem[2]
        if (len(first_number) > max_digits or len(second_number) > max_digits):
            return 'Error: Numbers cannot be more than four digits.'
        
        if first_number.isdigit() and second_number.isdigit():
            int_array_problems.append([int(first_number), problem[1] , int(second_number)])
        else:
            return 'Error: Numbers must only contain digits.'
        
    
    return int_array_problems

def operate(operator, first_number, second_number):
    if(operator == '+'):
        return first_number + second_number

    return first_number - second_number

def graph(array_operations, show_results=False):
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''

    for problem in array_operations:
        first_number = problem[0]
        operator = problem[1]
        second_number = problem[2]

        first_number_length = len(str(first_number))
        second_number_length = len(str(second_number))

        if(first_number_length < second_number_length):
            second_row += f'{operator} {second_number}    '
            max_space = second_number_length + 2
            third_row += f'{"".rjust(max_space, "-")}    '
            first_row += f'{"".ljust(max_space - first_number_length, " ")}{first_number}    '
            result = operate(operator, first_number, second_number)
            fourth_row += f'{"".ljust(max_space - len(str(result)), " ")}{result}    '

        else:
            first_row += f'  {first_number}    '
            max_space = first_number_length + 2
            second_row += f'{operator}{"".ljust(max_space - second_number_length - 1, " ")}{second_number}    '
            third_row += f'{"".rjust(max_space, "-")}    '
            result = operate(operator, first_number, second_number)
            fourth_row += f'{"".ljust(max_space - len(str(result)), " ")}{result}    ' 

    first_row = first_row.rstrip()
    second_row = second_row.rstrip()
    third_row = third_row.rstrip()
    fourth_row = fourth_row.rstrip()

    if show_results:
        return first_row + '\n' + second_row + '\n' + third_row + '\n' + fourth_row
    else:    
        return first_row + '\n' + second_row + '\n' + third_row

def arithmetic_arranger(problems, results=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    array_problems = check_operations(problems)
    if not array_problems:
        return "Error: Operator must be '+' or '-'."
    
    checked_digits = check_digits(array_problems)
    if type(checked_digits) is str:
        return checked_digits
    
    arranged_problems = graph(checked_digits, results)

    return arranged_problems