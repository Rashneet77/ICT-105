# Name: Rashneet Takhi
# Student ID: 12045112
# ICT105 Worksheet 2

# =========================
# SESSION 3
# =========================

# ===== QUESTION 1: LISTS BASIC =====
courses = [
    "Physics I",
    "Introduction t o Programming",
    "Biology I",
    "Calculus II",
    "English Composition I",
    "Microeconomics",
    "Chemistry I",
    "History I",
    "Linear Algebra",
    "Psychology I",
    "Data Structures and Algorithms",
    "Introduction to Philosophy",
    "Calculus I",
    "Macroeconomics",
    "Discrete Mathematics"
]

print("Original course list:")
print(courses)


# ===== QUESTION 2: SORTED() =====
print("\nAlphabetical order:")
print(sorted(courses))

print("\nReverse alphabetical order:")
print(sorted(courses, reverse=True))


# ===== QUESTION 3: REVERSE() =====
courses_copy = courses.copy()

courses_copy.reverse()
print("\nReversed list:")
print(courses_copy)

courses_copy.reverse()
print("\nBack to original:")
print(courses_copy)


# ===== QUESTION 4: SORT() =====
courses_copy2 = courses.copy()

courses_copy2.sort()
print("\nSorted using sort():")
print(courses_copy2)

courses_copy2.sort(reverse=True)
print("\nReverse sorted using sort():")
print(courses_copy2)


# ===== QUESTION 5A: EXPRESSION OF INTEREST =====
sorted_courses = sorted(courses)

print("\nThe following courses are available for expression of interest:")
for course in sorted_courses:
    print(course)


# ===== QUESTION 5B: REPLACE COURSE =====
courses_update = courses.copy()

withdrawn = courses_update[2]
courses_update[2] = "Chemistry I"

print("\nNOTICE:")
print(withdrawn, "has been withdrawn.")
print("Replaced with:", courses_update[2])


# ===== QUESTION 5C: ADD COURSES =====
courses_update.insert(0, "History I")
courses_update.insert(3, "Psychology I")
courses_update.append("Microeconomics")

print("\nUpdated courses:")
for c in courses_update:
    print(c)


# ===== QUESTION 5D: REMOVE COURSES =====
removed1 = courses_update.pop()
removed2 = courses_update.pop()
removed3 = courses_update.pop(1)
removed4 = courses_update.pop(2)

print("\nRemoved courses:")
print(removed1)
print(removed2)
print(removed3)
print(removed4)

print("\nRemaining courses:")
for c in courses_update:
    print(c)


# ===== QUESTION 6: TUPLES AND LOOPS =====
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I")
]

course_names = []

for course in course_tuples:
    course_id, course_name = course
    course_names.append(course_name)

print("\nCourse names from tuples:")
print(course_names)


# =========================
# SESSION 4
# =========================

# ===== QUESTION 7: CONDITIONAL + LOOP =====
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

while True:
    user_input = input("\nEnter course ID (1-15), 0, or quit: ")

    if user_input == "quit" or user_input == "0":
        print("Exited program.")
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    course_id = int(user_input)

    if course_id < 1 or course_id > 15:
        print("Course ID out of range.")
        continue

    found = False

    for item in departments:
        if item[0] == course_id:
            print(f"Course ID {course_id} is in {item[1]} department.")
            found = True
            break

    if not found:
        print("Course not found.")


# ===== QUESTION 8: COURSE INFO SYSTEM =====
courses_data = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"]
]

user_input = input("\nEnter course ID to get info: ")

if user_input.isdigit():
    cid = int(user_input)
    found = False

    for c in courses_data:
        if c[0] == cid:
            print("\nCourse found:")
            print("Name:", c[1])
            print("Department:", c[2])
            print("Prerequisite:", c[3])
            found = True
            break

    if not found:
        print("Course ID not found.")
else:
    print("Invalid input.")