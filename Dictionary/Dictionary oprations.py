
# create dictionary

my_dic ={}
print(type(my_dic))
print(my_dic)

my_dic = {"name":"Durga", "age":42,"Company": "Siemens"}
print(my_dic)

#Accessing values:
print(my_dic["name"])


#updating the value
my_dic["age"]=44
print(my_dic)

my_dic = {"name":"Purnima", "age":40, "Company":"Mediskin"}
print(my_dic)

my_dic["City"] = "NY"
print(my_dic)

#Deleting the key
del my_dic["age"]
del my_dic["name"]
print(my_dic)

#mixed Dic
my_dic={"name":"KD","age":42,"Bool":"True","float":34.12, list[1,2,3,4,5]}
