#while
count=1
while count<=10:
    print("Atharva")
    count+=1

a=1
while a<=5:
    print("kemcho")
    a+=1   


#print number 1 to 100 in loop 
i=1
while i<=100:
    print("numbers",i)
    i+=1  

#print number 100 to 1 in loop 
i=100
while i>=1:
    print("numbers",i)
    i-=1      


#print table of n number
i=1
while i<=10:
    print("table of 3 is ",3*i)
    i+=1

#print the list element is loop
num = [1, 2, 3, 4, 5, 6, 7, 8]    
index = 0
while index < len(num):
    print(num[index])
    index += 1


#sreach the number from the tuple 
num = (1, 2, 3, 4, 5, 66, 77, 8, 9)
s = 77
i = 0
while i < len(num):
    if (num[i] == s):
        print("The number found:", s)
        
    i += 1


    ###FOR###

list=[1,2,3,4,5,6,7]
for a in list:
    print(a)    


#print the element from the list using for loop 

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for val in list:
    print(val)    


#find  the element from the list using for loop 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x = 11

for val in list:
    if val == x:
        print("The number found is", val)
        break
else:
    print("Number not found")


#range 
for a in range(5):
    print(a)


for b in range(1,4):
    print(b)


for c in range(1,5,2):
    print(c)

lis=range(10)
for i in lis:
    print(i)   


#lets print even numbers

for i in range (10):
    if i%2==0:
        print("number is even",i)
        
#lets print numbers 1 to 100
 
for i in range(100):
    print(i)


#lets print numbers 100 to 1
 
for i in range(100,0,-1):
    print(i)



#print the table of n number 
n=3
for i in range (1,11):
    print("the table:",n*i)

#print the sum on n 
n=5
sum=0
for i in range (1,n+1):
    sum+=i
print(sum)           
