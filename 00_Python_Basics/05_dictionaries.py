# ==============================
# Dictionaries Practice
# ==============================

# Dictionary creation
student = {
    "name": "Umair",
    "age": 22,
    "field": "Artificial Intelligence"
}

print("Student Dictionary:", student)

# Access values
print("Name:", student["name"])
print("Age:", student["age"])
print("Field:", student["field"])

# Update value
student["age"] = 23
print("\nUpdated Age:", student["age"])

# Add new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Remove a key
student.pop("age")
print("After removing age:", student)

# Check if key exists
if "name" in student:
    print("\nKey 'name' exists in dictionary")

# Loop through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)


# ==============================
# Real-Life Example (AI / Data)
# ==============================

# Dataset stored as dictionary
ml_model = {
    "model_name": "Linear Regression",
    "learning_rate": 0.01,
    "epochs": 100,
    "accuracy": 0.92
}

print("\nML Model Details:")
for key, value in ml_model.items():
    print(key, "=>", value)


# ==============================
# Mini Project: Student Grades Manager
# ==============================

students = {}

while True:
    name = input("\nEnter student name (or 'exit' to stop): ")

    if name.lower() == "exit":
        break

    grade = input("Enter grade: ")
    students[name] = grade

print("\nFinal Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)
