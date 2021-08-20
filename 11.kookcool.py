#data type
name = "thammayuth chuasuwan"
age = 13
gender = "male"
student = True

print(type(name), name)
print(type(age), age)
print(type(gender), gender)
print(type(student), student)

list_friend = ["por", "long", "music", "prem", "mac"]

print(list_friend)
print(list_friend[4])

#operator
number1 = 34
number2 = 45
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 % number2)

#loop condition
for i in range(10):
    i = i+1
    if i>5 and i<8:
        print(i)

kookcool_age = 13
firstname = "thammayuth"
lastname = "chuasuwan"
friend = "music"
for i in range(kookcool_age):
    if i>9:
        print(firstname, lastname, friend)
