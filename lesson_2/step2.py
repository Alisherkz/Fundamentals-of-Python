my_list = [0, 1, 2, 3, 4, 5]
m = 1

for i in range(0, len(my_list), 2):
   my_list[m], my_list[i] = my_list[i], my_list[m]
   print("Стало - ", i, my_list)
   i+=2
   m+=2