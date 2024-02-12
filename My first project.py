print("Hello world")
print('hello')

number = int(input("Enter 3-digit number: "))
#524
n1 = number // 100
# v1
n2 = number // 10 % 10
# v2
# n2 = number % 100 // 10
n3 = number % 10
result = n1 + n2 + n3
print(f"n1: {n1} n2 {n2} n3 {n3}")
print(f"Result: {result}")

#####

number = int(input("Enter 4-digit number: "))
# 4258
n1 = number // 1000
# v1
n2 = number // 100 % 10
# v2
# n2 = number % 100 // 10
n3 = number % 100 // 10
n4 = number % 10
result = n1 + n2 + n3 + n4
print(f"n1: {n1} n2 {n2} n3 {n3} n4 {n4}")
print(f"Result: {result}")

####
first_diagonal =int(input("Enter the first diagonal: *"))
second_diagonal =int(input("Enter the second diagonal: *"))
area = (first_diagonal + second_diagonal) / 2
print("Area:", area)

