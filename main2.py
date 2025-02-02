#assign values to variables 
name="Mufasa"
age=30
is_student=False
weight=54.55

print("Name:",name,type(name))
print("Age:",age,type(age))
print("is_student:",is_student,type(is_student))
print("weight:",weight,type(weight))

print("\n After Typecasting:")
age=str(30)
print("Age:", age,type(age))
weight=bool(54.55)
print("weight:", weight,type(weight))