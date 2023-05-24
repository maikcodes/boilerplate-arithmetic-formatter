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
        
        try:
            int_first_number = int(first_number)
            int_second_number = int(second_number)
            int_array_problems.append([int_first_number, problem[1] , int_second_number])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
    
    return int_array_problems

def arithmetic_arranger(problems, results=True):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    if results:
        array_problems = check_operations(problems)
        if not array_problems:
            return "Error: Operator must be '+' or '-'."
        
        checked_digits = check_digits(array_problems)
        if type(checked_digits) is str:
            return checked_digits
        
        print(array_problems)        
        print(checked_digits)        


    # return arranged_problems