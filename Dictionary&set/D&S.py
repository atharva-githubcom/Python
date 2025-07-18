#Dictionary
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}
print(info)

#to print particular key pair
info={
    "key":"value",
    "name":"Atharva ",
    "Rollno":"58",
    "subject":["maths","english"],
}
print(info["key"]) # here it will only print the value which is present inside the key

#lets add some value externally in dictionary
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}
info["surname"]="Gite"
print(info)

#null dictonary here value is stored after creating the dictonary
null_dic={}
null_dic["name"]="sahil"
print(null_dic)

#Nested dictonary
student={
    "name":"atharva",
    "rollno":"58",
    "score":{
        "maths":89,
        "engish":70
    }
}
print(student)

#function/ methods in dictonary
#.key
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}

print(info.keys()) # here it will print the key like key,name,rollno,subject

#.values
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}
print(info.values())

#.get
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}
print(info.get("name"))

#.update
info={
    "key":"value",
    "name":"Atharva Gite",
    "Rollno":"58",
    "subject":["maths","english"],
}
(info.update({"city":"nashik"}))
print(info)


###SET###

set1={1,3,8,0}
print(set1)
print(type(set1))

#creating empty set
collection=set()
print(type(collection))

#Set Methods

#.add
set2={1,2,3,4,5}
set2.add(10)
print(set2)

#.remove
set3={1,2,3,4,5}
set3.remove(4)
print(set3)

#.clear
set4={1,2,3,4,5}
set4.clear()
print(set4)

#.pop
collection={"hello","world","AI&DS"}
print(collection.pop())

#union
set1={1,2,3}
set2={2,3,4,5,1}
print(set1.union(set2))
print(set1)
print(set2)

#intersection
set1={1,2,3,4}
set2={1,4,5}
print(set1.intersection(set2))


# assignemnt no 1 store the following in dictonary externally
dict={
    "name":"Atharva",
    "std":"10",
}
dict["Rollno"]="58"
print(dict)

#assingment no 2 give  2 value in the list use list or tuple 
dict={
    "name":"Atharva",
    "hobbies":["crickrt","football"]

}
print(dict)

#assingment no 3 given is list of subjects for students.assume one classroom is required for 1 subject . how many classroom are needed for by all student 
set={"python","python","C++","java","C++","java","python"}
print(len(set))

#assingment no 3 take marks from user of subject and store it in dictonary 
marks={} #creating empty dictonary 

x=int(input("enter the marks of eng"))
marks.update({"eng":x})

y=int(input("enter the marks of sci"))
marks.update({"sci":y})

z=int(input("enter the marks of math"))
marks.update({"Math":z})

print(marks)


# assingment no 4 find out way to store 9 and 9.0 as separte values in set 
number={
    ("int",5),
    ("float",5.0)
}
print(number)
