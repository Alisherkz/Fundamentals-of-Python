from random import randint

my_list = []
for i in range(10):
    my_list.append(randint(0, 300))

print(my_list)

new_list = [el for i, el in enumerate(my_list) if el > my_list[i - 1]]
print(new_list)