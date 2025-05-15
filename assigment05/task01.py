student_marks = {
"alice":85,
"Bob": 78,
"Charlie": 92,
   
}
name = (input("Enter the name of the student :"))

if name in student_marks:
    print(f"{name}'s marks are : {student_marks[name]}")
else:
    print("student no found in reecords. ")