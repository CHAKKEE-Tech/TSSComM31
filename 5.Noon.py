#Data Type
name = "Napat Ruangchaisit"
age = 14
sex ="Female"
student = True
list_name = ["ice","pluem",15,20,25]
list_friend =["yuta","ploy","mac","grace","copter"]

print(type(name),name)
print(type(age),age)
print(type(sex),sex)
print(type(student),student)
print(list_name[0])
print(list_friend[3])

#Operator
num1 = 34
num2 = 45
print (num1+num2)
print (num1-num2)
print (num1*num2)
print (num1/num2)

#Loop Condition
for i in range(10):
    print(i)
    
for i in range(10):
    i = i+1
    if i>5 and i<8:
        print(i)

napat_age = 14
first_name = "Napat"
last_name = "Ruangchaisit"
friend = "Yuta"
for i in range(napat_age):
    if i > 9:
        print(first_name,last_name,friend)
