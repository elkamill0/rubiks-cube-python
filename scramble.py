import convert
from random import randint


def generate_scramble(length: int) -> list[int]:
    output = [randint(0,5)]
    num = randint(0,5)
    while num == output[-1]:
        num = randint(0,5) 
    output.append(num)
    
    for _ in range(2, length):
        num = randint(0,5)
        if output[-1]^1 == output[-2]:
            while num == output[-1] or num == output[-1]^1:
                num = randint(0,5)
        while output[-1] == num:
            num = randint(0,5)
        output.append(num)
    
    return convert.convert([x * 3 + randint(0,2) for x in output], convert.int_to_move)
