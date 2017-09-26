"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""
x=str(input("Enter any string:"))
p=x[::-1]
if p ==x:
    print("%r is a Palindrome"%x)
else:
    print("%r is not a palindrome"%x)
