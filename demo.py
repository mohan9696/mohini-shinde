d1 = {'a': 2, 'b': 0, 'c': 0, 'd': 4, 'e': None}
output_dict = {key: value for key, value in d1.items() if value not in [0, None]}

print(output_dict)

l1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [num for num in l1 if num % 2 == 0]
print(l2)





