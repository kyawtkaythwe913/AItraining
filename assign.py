students = [
{"name": "Aung Aung","Age":19,"Study _hour": 8,"Score": 90},
{"name": "Su Su", "Age": 20, "Study _hour": 10, "Score": 88},
{"name": "Mg Mg", "Age": 18, "Study _hour": 5, "Score": 30},
{"name": "Hla Hla", "Age": 21, "Study _hour": 7, "Score": 75},
{"name": "Ko Ko", "Age": 22, "Study _hour": 6, "Score": 55},
]
for student in students:
    def classify_grade(score):
        if score < 0 or score > 100:
            return "Invalid"
        elif score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Pass"
        else:
            return "Fail"
    print("Name:" ,student["name"])
    print("Age:" ,student["Age"])
    print("Study Hours:" ,student["Study _hour"])
    print("Score:" ,student["Score"])
    print("Grade:" ,classify_grade(student["Score"]))
def calculate_average(scores):
    if len (scores) == 0:
        return 0
    return sum(scores) / len(scores)
def count_passed(students):
    passed_count = 0
    for student in students:
        if classify_grade(student["Score"]) != "Fail":
            passed_count += 1
    return passed_count

scores = [student["Score"] for student in students]
average_score= sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

passed=sum(1 for score in scores if score >= 40)
failed=sum(1 for score in scores if score < 40)
top_Student = max(students, key=lambda student: student["Score"])

print("total students:", len(students))
print("average score:", average_score)
print("highest score:", highest_score)
print("lowest score:", lowest_score)
print("passed students:", passed)
print("failed students:", failed)
print("top student:", top_Student["name"])