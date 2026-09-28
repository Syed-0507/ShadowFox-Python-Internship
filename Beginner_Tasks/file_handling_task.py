# Beginner Task - File Handling

import csv


input_file = "student_marks.csv"
output_file = "student_marks_updated.csv"

subject_columns = [
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Biology",
    "Economics",
    "History",
    "Civics"
]


students = []


# Open the original CSV file in read mode
with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:

        total_marks = 0
        subjects_count = 0

        for subject in subject_columns:

            mark = row[subject].strip()

            # Handle missing marks
            if mark != "":
                total_marks += float(mark)
                subjects_count += 1

        # Calculate average
        if subjects_count > 0:
            average = total_marks / subjects_count
        else:
            average = 0

        # Add new fields to dictionary
        row["total_marks"] = round(total_marks, 2)
        row["Average"] = round(average, 2)

        students.append(row)


# Display student dictionaries
print("Student Records:\n")

for student in students:
    print(student)


# Create a new CSV file
fieldnames = list(students[0].keys())

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)


print("\nNew CSV file created successfully!")
print("File name:", output_file)