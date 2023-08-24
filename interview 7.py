#nested list to single list
nested_list =[[1,2,3],[4,5],[6,7,8]]
single_list =[]
for i in nested_list:
    for j in i:
        single_list.append(j)
print(single_list)