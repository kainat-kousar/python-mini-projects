print("    STUDENT GRADE CALCULATOR")
name = input("Enter Student Name: ")

english = float(input("Enter English Marks: "))
math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
urdu = float(input("Enter Urdu Marks: "))

total = english + math + science + computer + urdu
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\nRESULT:")
print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
