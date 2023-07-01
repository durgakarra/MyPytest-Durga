
# 1. Numeric literals
a = 0b1010
b= 0x12c
c = 0o130
d = 150

#floating literals
float_1 = 100.10
float_2 = 120.456

#complex literals
x = 3.14j
y = 4.3j

print(a,b,c,d)
print(float_1, float_2)
print(x,y)

#string literals
char = "Welcome to the new world"
multiline_str = """ This is the multipline string with more chars"""
unicode = u"\u000dcnic\uf00123"
raw_str = r"\my string"

print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#boolean literals
x = (1==True)
y = (2==False)
a=True +4
b=False +10

print("x is :",x)
print("y is :",y)

print(a)
print(b)

#special listerals
drink = "Available"
food = None

def menu(x):
    if x== drink:
        print("drink")
    else:
        print(food)
menu(drink)
#menu(food)

#list of collections
a = ["[1,2,3],'apple',123.10"]#list
b= "(tuple, (1,2,3))" #tuple
c={'a','e','i','o','u'} #set
d={'a':'Apple','b':"Orange",'c':'Mango'}

print(a,b,c,d)


