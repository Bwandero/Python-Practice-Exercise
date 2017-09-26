"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""
#declare the list
x=range(1,99)
#ask the user for input
num =int(input("Enter a number "))
#declare an empty list
new_list=[]
#loop through the list
for number in x:
    if number % num ==0:
        new_list.append( number)
print(new_list)
