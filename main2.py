#assign values to variables
name="Mufasa"
age=30
is_student=False
weight=54.55

#print the variables with their data types
print("Age:",age,type(age))
print("is_student:",is_student,type(is_student))
print("weight:",weight,type(weight))

#typecasting
print("/n After Typecasting:-")
age=str(30)
print("Age:", age,type(age))
weight=bool(54.55)
print("weight:", weight,type(weight))