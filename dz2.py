def sum_list_1(dataset: list) -> int:
    cubes = [x ** 3 for x in range(100) if x % 2 != 0]
    print('Cоздан список кубов нечётных чисел {}'.format(cubes))
    my_numbers_sum = 0
    my_numbers_sum_list = []

    # итерация по списку
    for i in range(len(cubes)):
        # print('---print cubes[i]', cubes[i])
        my_str = str(cubes[i])
        my_list = list(my_str)
        # print('print my_list', my_list)
        for i in range(len(my_list)):
            my_list[i] = int(my_list[i])
        # Вычислить сумму чисел (вар.1)
        '''
        my_numbers_sum = sum(my_list)
        print(my_numbers_sum)
        '''
        # Вычислить сумму чисел (вар.2)
        for i in range(len(my_list)):
            my_numbers_sum = my_numbers_sum + my_list[i]
print(list)



