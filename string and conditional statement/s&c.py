#concatenation
str1="Atharva"
str2="Gite"
print(str1 + " " +str2)

#length of string
print(len(str1))

#indexing
str="atharva gite"
ch =str[2]
print(ch)
#slicing
print(str[1:4])

#function use for string 
str1="good night good"
print(str1.capitalize())
print(str1.replace("night","morning"))
print(str1.count("good"))

#assingmnet no1 take input user's frist name and print its length 
#str=(input("enter the name of user:")) 
#print(len(str))


# assingment no2 find  accurance of $ in the string 
str3="this $$$$$$ my atharva is name "
print(str3.count("$"))






#####2 conditional statment
age=16
if(age>=18):
    print("can vote for:")
else:
    print("cannot")    


##
light="blue"
if(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
elif(light=="red"):
    print("stop")    
else:
    print("broken") 


###
marks=int(input("enter the marks of student:"))
if(marks>=90):
    grade="a" 
elif(marks >= 80 and marks < 90):
    grade="b"
elif(marks >=70 and marks < 80):
    grade="c"
else:
    grade="fail"
print("the grade you have scored is :",grade)  


## nesting statement
age=34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")                

## assingment no 3 check number is odd or even 
num=int(input("enter the number:"))
if(num%2==0):
    print("number is even ")
else:    
    print(" number is odd")   

## assingment no 4 check from 3 number which is great

a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
if(a>b and a>c):
    print("a is big",a)
elif(b>a and b>c):
    print("b is big one",b)
else:
    print("c is big one",c)


# assingment no 5 check the number is multiple of 7 or not 

a=int(input("enter the number1:"))
if(a%7==0):
    print("multiple of 7",a)
else:
    print("is not multiple of 7",a) 


# assingment no2 find  accurance of $ in the string 
str3="this $$$$$$ my atharva is name "
print(str3.count("$"))
