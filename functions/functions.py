def sub_function(a,b):
    sub=a-b
    print(sub)
    return sub
sub_function(5,6)

##
def call():
    print("My Name is Atharva")
call()   

#create the function to caluate average of 3 numbers
def average(a,b,c):
    aver=(a+b+c)/3
    print(aver)
    return aver
average(3,4,5)

# create the function to print the length of list 
fruits=["apple","banana","orange","watermelon"]
vege=["patato","brinjal","pumpkin"]
def length(list):
    print(len(list))
    return list
length(vege)
length(fruits)

# #print list element in single line
fruits=["apple","banana","orange","watermelon"]
def prit(line):
    for i in line:
        print(i,end=" ")
        
prit(fruits)
 

#calculate the factorial of the number 
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print(fac)
    return fac

factorial(5)

def dollar_to_inr(dollar_amount, exchange_rate):
    inr_amount = dollar_amount * exchange_rate
    print(f"{dollar_amount} USD = ₹{inr_amount}")
    return inr_amount

dollar_to_inr(2, 83)


#function to understand the user input is odd or even
def odd_even(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
    return(num)    

odd_even (num=int(input("enter the number:")))
