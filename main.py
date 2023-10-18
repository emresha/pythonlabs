from first_a import main as first_main
from first_b import main as first_main_b
from second_a import main as second_main
from second_b import main as second_main_b
from third import main as third_main
from fourth import main as fourth_main
from fifth import main as fifth_main


initial_list = [int(i) for i in range(16)]
print(initial_list)
print(first_main(initial_list, k=int(input()), element=input()))
print(first_main_b(initial_list, k=int(input()), element=input()))
print(second_main(initial_list, k=int(input())))
print(second_main_b(initial_list, k=int(input())))
other_list = [1, 2, 1, 5, 0, 4, 2, 2, 2]
print(third_main(other_list, k=int(input())))
fourth_list = [-5, -7, -11, -1, -10, -11, -12, -9, -2, -3, -5, -7, -11, -19]
print(fourth_main(fourth_list))
fifth_list = [6, 4, 2, 8, 10, 12, -5, -10, -66, -3]
print(fifth_main(fifth_list))
