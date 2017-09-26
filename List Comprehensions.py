"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x=[even for even in a if even %2 == 0]

print (x)

"""new_even=[]
for even in a:
    if even % 2 == 0:
        new_even.append(even)
print (new_even)"""

