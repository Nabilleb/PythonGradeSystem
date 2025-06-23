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
    print (student_avg_grade)

# Sample list of records
records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]
 


# Create the journal and display the results
journal = create_class_journal(records)
get_name_grades_with_avg(journal)
