def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i-1
        next_element = input_list[i]
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j=j-1
        input_list[j+1] = next_element
list = [21,7,13,67,87,11,136,26]
insertion_sort(list)
print(list)