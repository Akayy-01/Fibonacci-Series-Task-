#FIBONACCI SERIES IN PYTHON
def fibonacci(i):
    if i<=1:
        return i
    else:
        return(fibonacci(i-1)+fibonacci(i-2))

num=int(input("Enter the number\n"))
if num<=0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:",end="")
for i in range(num):
    print(fibonacci(i),end=" ")
    
