# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

my_list = [1,2,3,4,5,6,7,8]

def binary_search(list, el):
    first = 0
    
    mid = list[(len(list) - 1) // 2]
    print("mid is", mid)
    last = len(list) - 1
    
    new_list = list
    
    if el == mid:
        print("found the", mid)
    
    i = 0
    
    while el != mid:

        if el > mid:
            i = i + 1

            mid_index = (len(new_list) - 1) // 2
            new_list = new_list[mid_index:]
            mid = new_list[mid_index]
            print(new_list, "this is mid -", mid,"this is mid_index -", mid_index, "iteration", i)

        elif el < mid:
            mid_index = (len(new_list) - 1) // 2
            new_list = new_list[:mid_index]
            print(new_list, "here this is mid -", mid,"this is mid_index -", mid_index, "iteration", i)
            mid = new_list[mid_index]
            print(new_list, "this is mid -", mid,"this is mid_index -", mid_index, "iteration", i)
    
    if el == mid:
        print("found the", mid)
            
binary_search(my_list, 5)



# note

a = [1,2,3,4,5,6]

mid = ((len(a) - 1) // 2)

print(mid)
print(a[:mid])
print(a[mid + 1:])
