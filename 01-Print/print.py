print("Hello World..")

# printing variable
name="siva"
print(name)

# printing multiple variables
first_name="Siva"
second_name="Prasad"
last_name="Batta"
print(first_name,second_name,last_name) #o/p:Siva Prasad Batta -> Here the default seperator is 'space'

# Formatted print (f-string)
print(f"Full Name: {first_name} {second_name} {last_name}") #o/p: Full Name: Siva Prasad Batta
#addition
num1=2
num2=32
print(num1+num2)

name = "siva"
print(f"My Name is {name}") #o/p: My Name is siva

name = "prasad"
age = 35
print(f"My name is {name}, my age {age}") #o/p: My name is prasad, my age 35

a = 10
b = 20
print(f"Sum of a+b is {a+b}") #o/p: Sum of a+b is 30

num1 = 100
num2 = 200
print(f"sum of two numbers is {num1+num2}") #o/p: sum of two numbers is 300

# Decimal formatting
a = 3.24123
print(a) #o/p: 3.24123
print(f"a.2f") #o/p: a.f2
print(f"{a:.2f}") #o/p: 3.24
print(f"a:.3f") #o/p: a:.3f
print(f"{a:.3f}") #o/p: 3.241
print(f"value of 'a' up to 4 decimals is {a:.4f}") #o/p: value of 'a' up to 4 decimals is 3.2412

# Width formatting
num = 7
print(f"Number: {num:5}") #o/p: Number:     7 --> before variable value it took width space,here 5 spaces

name="siva"
age=35
print(f"{name}{age:10}") #o/p: siva        35 --> here 10 spaces

#Python లో old .format() method ని f-string కి ముందు ఎక్కువగా use చేసేవారు.
#ఇది Python 2.7 మరియు 3.x లో పని చేస్తుంది.


# seperator & Line end
num1=100
num2=200
num3=300
print(num1,num2,num3) #o/p: 100 200 300
print(num1,num2,num3,sep='-',end="\n") #o/p: 100-200-300

print(num1,num2,num3,sep=' ', end='hi') #o/p: 100 200 300hi

day=20
month=2
year=2026
# print(f"todays date is:{day},{month},{year},sep='-',end='\n'") --> error
print(f"Todays DATE is:",day,month,year,sep="-",end="\n") # o/p: Todays DATE is:-20-2-2026