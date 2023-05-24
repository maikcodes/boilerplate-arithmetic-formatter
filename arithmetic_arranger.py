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
    for problem in array_problems:
        if (type(problem[0]) is str) and (type(problem[2]) is str):
            return False
    return True

def arithmetic_arranger(problems, results=True):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    if results:
        array_problems = check_operations(problems)
        if not array_problems:
            return "Error: Operator must be '+' or '-'."
        
        if not check_digits(array_problems):
            return 'Error: Numbers must only contain digits.'
        
        print(array_problems)        


    # return arranged_problems