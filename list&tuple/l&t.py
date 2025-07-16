###LIST###
mark=[95,45,34,98,76,85,65]
print(mark)
print( "is",len(mark))
print(mark[5])

#list method

#append means adding the number 34 in list 
list=[34,54,56]
list.append(32)
print(list)

#sort the given number in ascending to decending 
list=[34,20,56]
(list.sort()) 
print(list)

#sort yhe given number in decending 
list=[34,20,56]
(list.sort(reverse=True))
print(list)

#lets sort the words now 
list=["apple","watermelon","mango","banana"]
(list.sort()) 
print(list)

#lets reverse the list now 
list=[1,2,3,4,5,6]
(list.reverse())
print(list)

#lets insert the element at index
list=[1,2,3,4,5,6]
(list.insert(0,10)) #basic logic here is like  (0,10) 0 here is index and 10 is element
print(list)

#lets remove the element
list=[1,2,3,4,5,6]
(list.remove(2))
print(list)

#lets pop the element means removing it from particular index
list=[1,2,3,4,5,6]
(list.pop(0))  # here 0 means number from index 0 will be remove now which is 1
print(list)




###TUPLE###
a=(1,2,3,4)
print(type(a))


#lets find the index of number in tuple 
a=(1,2,3,4)
print(a.index(2))

#lets count the how many time 3 occur in tuple 
a=(1,2,3,3,3,35,3,)
print(a.count(3))


#assingmment no 1 enter the 3 movies and store it in list 
a=input("enter the movie name ")
b=input("enter the movie name")
c=input("enter the movie name")
list=[]
(list.append(a))
(list.append(b))
(list.append(c))
print(list)

#second way to write same 
list=[]
list.append(input("enter the movie name "))
list.append(input("enter the movie name "))
list.append(input("enter the movie name "))
print(list)

#assingment no 2 check wheater the given element in list are palindrome or not 
list=[1,2,3]
copy_list =list.copy()
copy_list.reverse()
if(copy_list==list):
    print("palindrome")

else:
    print("not palindrome")    


#assingment no 3 count the number of studnet with "a" grade in following tuple 
tuple=("a","b","a","a","b","c","c")
print(tuple.count("a"))

# assingment no 4 sort the following garde using list 
list=["a","b","a","a","b","c","c"]
(list.sort())
print(list)
