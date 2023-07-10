inp = input().split(" ") # split the input into a list of strings
my_list = [int(i) for i in inp[0].split(",")] # split the first element of the list into a list of integers
target = int(inp[1]) # convert the second element of the list into an integer

def find(my_list, target):
    my_dict = {} 
    result = []
    for i in range(len(my_list)): 
        if my_list[i] in my_dict:
            result.append((my_dict[my_list[i]], my_list[i]))  # add the pair to the result list
        else:
            my_dict[target - my_list[i]] = my_list[i]   # add the key-value pair to the dictionary
    return result

print(find(my_list, target))