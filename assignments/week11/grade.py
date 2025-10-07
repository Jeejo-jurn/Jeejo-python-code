"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_students):
    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student #{i + 1}: ")
        scores = []
        for j in range(3):
            score = float(input(f"Enter score {j + 1} for {name}: "))
            scores.append(score)
        students.append({'name': name, 'score': scores})
    return students

def calculate_averages(students):
    for student in students:
        total = 0
        for score in student['score']:
            total += score
        average = total / len(student['score'])
        student['average'] = average

def display_result(students):
    print("\nStudent Results:")
    for student in students:
        status = "PASS" if student['average'] >= passing_grade else "FAIL"
        print(f"{student['name']}: Average = {student['average']:.2f}, Status = {status}")

num = int(input("Enter number of students: "))
students = input_students(num)
calculate_averages(students)
display_result(students)

        