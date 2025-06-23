import statistics

# Function to create a class journal from records
def create_class_journal(records):
    class_journal = {}
    for name, grade in records:
        if name not in class_journal:
            class_journal[name] = []
        class_journal[name].append(grade)
    return class_journal

# Function to analyze and return all class data as text
def generate_report_text(journal):
    lines = []
    student_avg_grade = {}

    lines.append("=== Student Grades and Averages ===")
    for name, grades in journal.items():
        avg = sum(grades) / len(grades)
        student_avg_grade[name] = avg
        lines.append(f"Student Name: {name} | Grades: {grades} | Average: {avg:.2f}")

    lines.append("")
    lines.append(highest_avg(student_avg_grade))
    lines.append(most_consistent_by_range(journal))

    below_70 = students_with_grade_below(journal, 70)
    lines.append(f"\nStudents with at least one grade below 70: {below_70}")
    lines.append(f"Total grades entered across the class: {total_grades_entered(journal)}")
    lines.append(f"Class average grade: {class_average(journal):.2f}")

    return "\n".join(lines)

# Function to find student with highest average
def highest_avg(avg_dict):
    max_avg = 0
    student_name = ""
    for name, avg in avg_dict.items():
        if avg > max_avg:
            max_avg = avg
            student_name = name
    return f"Highest average is {student_name} with {max_avg:.2f}"

# Function to find most consistent student by grade range
def most_consistent_by_range(journal):
    min_diff = float('inf')
    consistent_student = ""
    for name, grades in journal.items():
        grade_range = max(grades) - min(grades)
        if grade_range < min_diff:
            min_diff = grade_range
            consistent_student = name
    return f"Most consistent (by smallest diff) is {consistent_student} with a difference of {min_diff}"

# Function to find students with a grade below a threshold
def students_with_grade_below(journal, threshold=70):
    students = []
    for name, grades in journal.items():
        if any(grade < threshold for grade in grades):
            students.append(name)
    return students

# Function to count all grades
def total_grades_entered(journal):
    return sum(len(grades) for grades in journal.values())

# Function to calculate the class average
def class_average(journal):
    all_grades = [grade for grades in journal.values() for grade in grades]
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)

# Sample input records
records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

# Create journal and generate report
journal = create_class_journal(records)
report_text = generate_report_text(journal)

# Save the report to a text file
with open("class_report.txt", "w") as file:
    file.write(report_text)

print("✅ Report generated and saved to 'class_report.txt'")
