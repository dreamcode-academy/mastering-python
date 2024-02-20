shopping_list = ["apples"]

# Append: Add an element to the end of the list
# shopping_list.append(item)
shopping_list.append("bread")
print(shopping_list)

# Insert: Add an element at a specified position.
# shopping_list.insert(index, item)
shopping_list.insert(0, "milk")
print(shopping_list)

# Remove: Remove the first element of the list whose value is equal to x.
#s hopping_list.remove(item)
shopping_list.remove("bread")
print(shopping_list)

# Pop: Remove the element at the given position in the list and return it.
# popped_item = shopping+list.pop()
print("Pop:")
bought_item = shopping_list.pop()
print(bought_item)
print(shopping_list)

# Sort: Sort the list items in place.
# shopping_list.sort()
print("Sort():")
shopping_list.extend([ "eggs", "rice", "chicken"])
print(shopping_list)
shopping_list.sort()
print(shopping_list)