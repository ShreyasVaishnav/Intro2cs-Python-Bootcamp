def calc_math_expression(num1, num2, operator):
    try: 
        if operator!= "+" or operator!= "-" or operator!= "*" or operator!= ":":
            return None
        elif operator == "+":
            result = (float(num1) + float(num2))
        elif operator == "-":
            result = (float(num1) - float(num2))
        elif operator == "*": 
            result = (float(num1)*float(num2))
        elif operator==":":
            result = (float(num1)/float(num2))
        else:
            return None
    except:
        return None


def calc_math_expression_from_str(str_input):
    str_input = str_input.split()
    num_1 = str_input[0]
    operator_ = str_input[1]
    num_2 = str_input[2]
    return(calc_math_expression(num_1, num_2, operator_))

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    num_list = []
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    num_list.sort()
    large_num = num_list[-1]
    small_num = num_list[0]
    result_tule = (large_num, small_num)
    return result_tule

from math import sqrt
def quadratic_equation_solver(a, b, c):
    try:
        x1 = ((-b) + sqrt((b ** 2) - 4 * a * c) / 2 * a)
        x2 = ((-b) - sqrt((b ** 2) - 4 * a * c) / 2 * a)
    except:
        return (None, None)
    
    if ((b**2)-(4*a*c)) > 0:
        result = (x1, x2)
    elif ((b**2)-(4*a*c)) == 0:
        result = (x1, x2)
    else:
        result = (None, None)
    
    return result

def quadratic_equation_solver_from_user_input():
    user_input = input().split()
    if user_input[0]== "0":
        print(" 'A' cannot be Zero! ")
    else:
        print("OK")

    a = float(user_input[0])
    b = float(user_input[1])
    c = float(user_input[2])
    return(quadratic_equation_solver(a, b ,c))

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    temp_list = [temp_1, temp_2, temp_3]
    result = []
    for temp in temp_list:
        if temp > min_temp:
            result.append(temp)
        if len(result) >= 2:
            return True
        else:
            return False
        

calc_math_expression_from_str("10 : 2") == 5.0
calc_math_expression_from_str("10 : -2") == -5.0
calc_math_expression_from_str("-10 : -2") == 5.0
calc_math_expression_from_str("-10 : 2") == -5.0
calc_math_expression_from_str("10 + 2") == 12.0
calc_math_expression_from_str("100 - 39.3") == 60.7
calc_math_expression_from_str("5 : 2") == 2.5
calc_math_expression_from_str("5 : 0") is None
calc_math_expression_from_str("10 333 2") is None
calc_math_expression_from_str("10 ^ 2") is None


find_largest_and_smallest_numbers(5, 1, 10) == (10, 1)
find_largest_and_smallest_numbers(2.5, 2.5, 7) == (7, 2.5)
find_largest_and_smallest_numbers(7, 2.5, 2.5) == (7, 2.5)
find_largest_and_smallest_numbers(-5, -5, -5) == (-5, -5)
find_largest_and_smallest_numbers(10, -1, 10) == (10, -1)
find_largest_and_smallest_numbers(-2, 5, -2) == (5, -2)
find_largest_and_smallest_numbers(3, 20, -2) == (20, -2)
find_largest_and_smallest_numbers(7, 10, 0) == (10, 0)
find_largest_and_smallest_numbers(10, 7, 0) == (10, 0)
find_largest_and_smallest_numbers(0, 10.01, 10) == (10.01, 0)

quadratic_equation_solver(1, 1.5, -1) == (0.5, -2)
quadratic_equation_solver(1, -8, 16) == (4, None)
quadratic_equation_solver(1, -2, 34.5) == (None, None)
quadratic_equation_solver(4, -12, 9) == (3/2, None)


temp_checker(26, 38, 90, 20) is True
temp_checker(10, 10, 10, 10) is False
temp_checker(10, 11, 10, 11) is True
temp_checker(-1, -9, 0, 1) is True
temp_checker(0, 90, 0, 1) is True

print("All tests passed")

