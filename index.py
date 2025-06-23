# Function to create a class journal with student names as keys and list of grades as values
def create_class_journal(records):
    class_journal = {}
    for name, grade in records:
        if name not in class_journal:
            class_journal[name] = []
        class_journal[name].append(grade)
    return class_journal

# Function to print each student's name, grades, and their average
def get_name_grades_with_avg(journal):
    student_avg_grade = {}
    for name, grades in journal.items():
        avg = sum(grades) / len(grades)
        student_avg_grade[name] = avg
        print(f"Student Name: {name} | Grades: {grades} | Average: {avg:.2f}")
    
    print(highest_avg(student_avg_grade))
    print(most_consistent_by_range(journal))

# Function to get the student with the highest average
def highest_avg(avg_dict):
    max_avg = 0
    student_name = ""
    for name, avg in avg_dict.items():
        if avg > max_avg:
            max_avg = avg
            student_name = name
    return f"Highest average is {student_name} with {max_avg:.2f}"

# Function to find the student with smallest range (most consistent)
def most_consistent_by_range(journal):
    min_diff = float('inf')
    consistent_student = ""

    for name, grades in journal.items():
        grade_range = max(grades) - min(grades)
        if grade_range < min_diff:
            min_diff = grade_range
            consistent_student = name

    return f"Most consistent (by smallest diff) is {consistent_student} with a difference of {min_diff}"

# Sample list of records
records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

# Create the journal and display the results
journal = create_class_journal(records)
get_name_grades_with_avg(journal)
