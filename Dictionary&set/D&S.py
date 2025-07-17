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
