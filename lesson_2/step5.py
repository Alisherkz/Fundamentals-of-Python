my_list = [7, 5, 3, 3, 2]
new_element = int(input("new element: "))

for i in range(len(my_list)):

    if new_element < my_list[i]:
        tmp = new_element 
        new_element = my_list[i]
        my_list[i] = tmp
    else: print(my_list.append(new_element))

#print(my_list)
