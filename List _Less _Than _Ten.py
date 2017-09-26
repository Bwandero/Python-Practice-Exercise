"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5."""

#declare the list
x=[1,2,3,4,6,5,7,8,9,10]
#ask the user to enter a number
enter=int(input("Enter a number of your choice:"))
#declare a empty list
new_list=[]
#loop through the list
for lists in x:
    #check if the list is less than five
    if lists < enter:
        new_list.append(lists)
#print out the new list
print (new_list)
