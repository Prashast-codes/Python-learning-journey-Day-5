# Question no. 4 . : print even number in between 1 to 10 :
i = 1

while i <= 10 :
    if i % 2 == 0 :
        print(i)
    i += 1

# Question no. 5. : print number 1 upto 20 but :
# > if number is divisible by 3 then print fizz.
# > if number is divisible by 5 then print buzz.
# > ohterwise print the number itself.

number = 1
while number <= 20  :
    if number % 3 == 0 :
        print("fizz")
    elif number % 5 == 0 :
        print("buzz")
    else :
        print(number)
    number += 1 

# Question no. 6 : create a multiplication table :

number = int(input("Enter a number :"))
i = 1
while  i <= 10 :
    print(number,"x",i,"=",number*i )
    i += 1 

# Question no. 7 : reverse the table :

number = int(input("Enter a number : "))
i = 10
while i >= 1 :
    print(number,"x",i,"=",number*i)
    i -= 1  