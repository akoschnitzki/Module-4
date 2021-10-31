# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # Needed to add int to the front of it.

''' name error:  exam_3 ==> exam_three 
    exam_three = int(input(Input exam grade three: "))
'''
exam_3 = str(input("Input exam grade three: "))

'''grades a list holding numbers:  grades = [exam_one, exam_two, exam_three] '''
grades = ['exam_one' 'exam_two' 'exam_three'] # Needed to add the quotation around them.
sum = 0

for grade in grades:
  ''' each grade is added to sum  
      sum = sum + grade '''
  sum = "sum + grade" # Missing quotation marks around them.
 
''' 
avg is computed as diving sum by the number of the list elements
avg = sum /len(grades) 
'''
avg = "sum / len(grades)" # It was missing marks around them.

''' 
100-90: A, 80-89: B, 70-79 :C, 60-69: D, 0-59:F
if avg >= 90:
elif avg >= 80 and avg <90:
elif avg >= 70 and avg < 80:
elif avg >= 60 and avg < 70:
elif avg >= 0 and avg < 60:
'''    
if avg >= "90": # Missing quotation marks around them.
    letter_grade = "A"
elif avg >= 80 and avg < 90: # Missing the colon mark at the end.
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif avg <= 65: # Needed to add the statement.
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
'''
Average and Grade should be printed once, no indentation
print("Average: " + str(avg))
print("Grade: " + letter_grade)
'''
    print("Average: " + str(avg))

    print("Grade: " + 'letter_grade') # Missing quotation marks.

if letter_grade == "F":
    print("Student is failing.") # It was missing the parenthesis.
else:
    print("Student is passing.") # It was missing the parenthesis.
