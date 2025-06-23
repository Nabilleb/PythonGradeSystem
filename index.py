import statistics

# Function to create a class journal with student names as keys and list of grades as values
def create_class_journal(records):
    """
    Creates a dictionary where keys are student names and values are lists of their grades.
    """
    class_journal = {}
    for name, grade in records:
        if name not in class_journal:
            class_journal[name] = []
        class_journal[name].append(grade)
    return class_journal

# Function to print each student's name, their grades, and their average grade
def get_name_grades_with_avg(journal):
    """
    Prints student names, their grades, and their average grade.
    Also prints the student with the highest average and the most consistent student by range.
    """
    student_avg_grade = {}
    for name, grades in journal.items():
        avg = sum(grades) / len(grades)
        student_avg_grade[name] = avg
        print(f"Student Name: {name} | Grades: {grades} | Average: {avg:.2f}")
    
    print(highest_avg(student_avg_grade))
    print(most_consistent_by_range(journal))

# Function to find the student with the highest average grade
def highest_avg(avg_dict):
    """
    Returns the student with the highest average grade.
    """
    max_avg = 0
    student_name = ""
    for name, avg in avg_dict.items():
        if avg > max_avg:
            max_avg = avg
            student_name = name
    return f"Highest average is {student_name} with {max_avg:.2f}"

# Function to find the most consistent student by smallest difference between highest and lowest grades
def most_consistent_by_range(journal):
    """
    Returns the student with the smallest range (difference between highest and lowest grades).
    """
    min_diff = float('inf')
    consistent_student = ""

    for name, grades in journal.items():
        grade_range = max(grades) - min(grades)
        if grade_range < min_diff:
            min_diff = grade_range
            consistent_student = name

    return f"Most consistent (by smallest diff) is {consistent_student} with a difference of {min_diff}"

# Function to find students who had at least one grade below a given threshold
def students_with_grade_below(journal, threshold=70):
    """
    Returns a list of students who have at least one grade below the specified threshold.
    """
    students = []
    for name, grades in journal.items():
        if any(grade < threshold for grade in grades):
            students.append(name)
    return students

# Sample list of records (student name and grade pairs)
records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

# Create the journal from records
journal = create_class_journal(records)

# Print grades, averages, and consistency information
get_name_grades_with_avg(journal)

# Find and print students with at least one grade below 70
below_70_students = students_with_grade_below(journal, 70)
print("\nStudents with at least one grade below 70:", below_70_students)
