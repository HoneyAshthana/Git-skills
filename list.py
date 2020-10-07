a = [1,1,2,3,5,8,13,21,34,55,89]
no = int(raw_input('Choose a no : '))
new_list = []
for i in a:

    if i < no :
        new_list.append(i)
print new_list

