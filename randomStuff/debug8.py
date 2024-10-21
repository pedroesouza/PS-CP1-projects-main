
# This function is supposed to add an item to a list, but it produces unexpected results. Find the bug.

def add_to_list(item, my_list=[]):

     my_list.append(item)

     return my_list

print(f"List: {add_to_list(input("What is your item?: "))}")