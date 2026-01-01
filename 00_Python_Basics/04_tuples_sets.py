# ==============================
# Tuples Practice
# ==============================

"""
colors = ("red", "green", "blue")
print(colors)

# Access element
print(colors[0])  # red
"""


# Tuple creation
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Access tuple elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuple with different data types
student_info = ("Umair", 22, "AI")
print("Student Info:", student_info)

# Length of tuple
print("Length of tuple:", len(student_info))

# Loop through tuple
print("\nLooping through tuple:")
for item in student_info:
    print(item)



# ==============================
# Sets Practice
# ==============================

# Set creation (duplicates are removed automatically)
numbers = {1, 2, 3, 4, 4, 5, 5}
print("\nSet of numbers:", numbers)

# Add element to set
numbers.add(6)
print("After adding 6:", numbers)

# Remove element from set
numbers.remove(3)
print("After removing 3:", numbers)

# Another set
even_numbers = {2, 4, 6, 8}

# Set operations
print("\nUnion:", numbers.union(even_numbers))
print("Intersection:", numbers.intersection(even_numbers))
print("Difference:", numbers.difference(even_numbers))


# ==============================
# Real-life Example (AI/Data Use)
# ==============================

# Removing duplicate values from dataset
data = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_data = set(data)

print("\nOriginal Data:", data)
print("Unique Data:", unique_data)

