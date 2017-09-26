"""write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes."""

a = range(1,50)
b = range(1,100)
c=[y for y in set(a) if y in set(b)]
print (c)
