import csv
header = ["Student ID", "Student Name", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
students = []
for i in range(1, 11):
    student_id = input(f"Enter Student {i} ID: ")
    student_name = input(f"Enter Student {i} Name: ")
    marks = []
    for j in range(1, 6):
        subject_mark = float(input(f"Enter marks for Subject {j}: "))
        marks.append(subject_mark)
    students.append([student_id, student_name] + marks)
with open("result.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(students)
with open("result.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    updated_students = []
    for row in reader:
        total_marks = sum([float(row[f"Subject {i}"]) for i in range(1, 6)])
        grade = "A" if total_marks >= 90 else "B" if total_marks >= 80 else "C" if total_marks >= 70 else "D"
        row["Total Marks"] = total_marks
        row["Grade"] = grade
        updated_students.append(row)
with open("result.csv", "w", newline="") as csvfile:
    fieldnames = header + ["Total Marks", "Grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_students)
updated_students.sort(key=lambda x: x["Total Marks"], reverse=True)
print("Top 3 Students:")
for i in range(3):
    print(f"Student ID: {updated_students[i]['Student ID']}, Student Name: {updated_students[i]['Student Name']}, Percentage: {updated_students[i]['Total Marks']}%")
