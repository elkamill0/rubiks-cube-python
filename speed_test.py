import timeit

test_values = [5, 33, 9, 17, 69, 97, 73, 81, 0, 42, 100]

# 1. dict.get() słownik
dict_map = {5: 33, 33: 9, 9: 17, 17: 5, 69: 97, 97: 73, 73: 81, 81: 69}
def dict_get_m(x):
    return dict_map.get(x, x)

# 2. if-elif-else
def if_elif_m(x):
    if x == 5:
        return 33
    elif x == 33:
        return 9
    elif x == 9:
        return 17
    elif x == 17:
        return 5
    elif x == 69:
        return 97
    elif x == 97:
        return 73
    elif x == 73:
        return 81
    elif x == 81:
        return 69
    else:
        return x

# 3. arith (bool multiplication)
def arith_m(x):
    return ((x == 5) * 33 +
            (x == 33) * 9 +
            (x == 9) * 17 +
            (x == 17) * 5 +
            (x == 69) * 97 +
            (x == 97) * 73 +
            (x == 73) * 81 +
            (x == 81) * 69 +
            (x not in [5, 33, 9, 17, 69, 97, 73, 81]) * x)

# 4. lista par - linearny search
pairs = [(5, 33), (33, 9), (9, 17), (17, 5), (69, 97), (97, 73), (73, 81), (81, 69)]
def list_of_pairs_m(x):
    for k, v in pairs:
        if x == k:
            return v
    return x

setup_code = '''
from __main__ import dict_get_m, if_elif_m, arith_m, list_of_pairs_m, test_values
'''

repeat = 5
number = 100000

print("Testing performance with", number, "calls, repeated", repeat, "times...\n")

time_dict = timeit.repeat('for x in test_values: dict_get_m(x)', setup=setup_code, number=number, repeat=repeat)
print("dict_get_m     :", min(time_dict), "sec")

time_if = timeit.repeat('for x in test_values: if_elif_m(x)', setup=setup_code, number=number, repeat=repeat)
print("if_elif_m      :", min(time_if), "sec")

time_arith = timeit.repeat('for x in test_values: arith_m(x)', setup=setup_code, number=number, repeat=repeat)
print("arith_m        :", min(time_arith), "sec")

time_list_pairs = timeit.repeat('for x in test_values: list_of_pairs_m(x)', setup=setup_code, number=number, repeat=repeat)
print("list_of_pairs_m:", min(time_list_pairs), "sec")



