
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


def sum_of_args(*args):
    result = 0
    for x in args:
        result += x
    return result


def concatenate(**kwargs):
    print(f'kwargs={kwargs}')
    result = ''
    for x in kwargs.values():
        result += x
    return result


def sum_of_3(a, b, c):
    return a + b + c


if __name__ == '__main__':
    list_of_ints = [1, 2, 3]
    sum1 = my_sum(list_of_ints)
    print(sum1)
    sum2 = sum_of_args(10, 11, 12)
    print(sum2)
    str1 = concatenate(a='This', b='Is', c='An', d='Example', e='!')
    print(str1)

    my_list = [44, 55, 66]
    print(my_list)
    print(*my_list)
    sum3 = sum_of_3(*my_list)
    print(sum3)

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]
    list_sum = sum_of_args(*list1, *list2, *list3)
    print(list_sum)

    my_list = [1, 2, 3, 4, 5, 6, 7]
    a, *b, c = my_list
    print(f'my_list={my_list} a={a} b={b} c={c}')

    my_first_dict = {"A": 1, "B": 2}
    my_second_dict = {"C": 3, "D": 4}
    my_merged_dict = {**my_first_dict, **my_second_dict}

    print(f'first={my_first_dict} second={my_second_dict} merged={my_merged_dict}')

    name = [*'John Anderson']
    print(f'name={name}')
