__author__ = 'ilija'


def fibonacci(limit):
    first_number = 1
    second_number = 1
    a_list = [1, 1]
    for n in range(limit):
        first_number, second_number = second_number, first_number + second_number
        a_list.append(second_number)
    return a_list

another_list = fibonacci(100)
reverse_list = another_list[:0:-1]
print reverse_list

def count_even(input_list):
    counter = 0
    for element in input_list:
        if element % 2 == 0:
            counter += 1
    return counter

print count_even(fibonacci(20))



print md5("Elijah")