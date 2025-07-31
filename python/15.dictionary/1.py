#1.
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}

#1.1.
students[106] = "Frank"
print("After Adding:", students)

#1.2
students[102] = "Bobby"
print("After Updating:", students)

#1.3
print("Student with ID 103:", students[103])

#1.4
nested_students = {
    201: {"name": "George", "grade": "A"},
    202: {"name": "Hannah", "grade": "B"},
    203: {"name": "Ian", "grade": "C"}
}

#1.5
print("Student 202 Name:", nested_students[202]["name"])
print("Student 203 Grade:", nested_students[203]["grade"])

#1.6
print("Student IDs:", students.keys())

#1.7
del students[104]
print("After Deletion:", students)

