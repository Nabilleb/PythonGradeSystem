def create_class_journal(records):
    class_journal = {}
    for name, grade in records:
        if name not in class_journal:
            class_journal[name] = []
        class_journal[name].append(grade)
    return class_journal

def get_name_grades(records):

    for name, grade in records.items():
        print(f"student name : {name} student grades: {grade} ")

records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

journal = create_class_journal(records)

get_name_grades(journal)


