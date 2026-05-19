# Worksheet 3: Dictionaries, Loops, and User Input
# Name: Rashneet Takhi
# Student ID: 12045112
# ICT105 Worksheet 1
# Author: Tosh

from typing import List, Dict, Tuple


def session5_course_enrollments() -> None:
    """Session 5.1.1: Student Course Enrollment with dictionaries."""
    course_enrollments: Dict[int, List[str]] = {
        1001: ["CS101", "MATH101"],
        1002: ["CS101", "MATH102"],
        1003: ["CS202", "PHY101"],
        1004: ["CS202", "CHEM101"],
        1005: ["BIO101", "HIST101"],
        1006: ["BIO102", "ENGL101"],
        1007: ["ECON101", "PSY101"],
        1008: ["ECON102", "SOC101"],
        1009: ["PSY102", "SOC102"],
        1010: ["CS101", "MATH101"],
    }

    print("Student Course Enrollment")
    for student_id, courses in course_enrollments.items():
        print(f"Student ID {student_id}: enrolled in {courses}")

    print("\nOutput:")
    for student_id, courses in course_enrollments.items():
        print(f"Student ID {student_id} -> {courses}")


def session5_class_schedule() -> None:
    """Session 5.1.1: Class Schedule by department using dictionaries of tuple lists."""
    departments: Dict[str, List[Tuple[str, str]]] = {
        "Computer Science": [
            ("CS101", "Introduction to Computer Science"),
            ("CS202", "Data Structures and Algorithms"),
        ],
        "Mathematics": [
            ("MATH101", "Calculus I"),
            ("MATH102", "Calculus II"),
        ],
        "Physics": [("PHY101", "General Physics I")],
        "Chemistry": [("CHEM101", "General Chemistry I")],
        "Biology": [("BIO101", "Biology I")],
        "History": [("HIST101", "American History I")],
        "English": [("ENGL101", "English Composition I")],
        "Economics": [("ECON101", "Principles of Economics")],
        "Psychology": [("PSY101", "Introduction to Psychology")],
        "Sociology": [("SOC101", "Introduction to Sociology")],
    }

    print("\nClass Schedule")
    for department, course_list in departments.items():
        print(f"Department: {department}")
        for course_id, course_name in course_list:
            print(f"  {course_id} - {course_name}")

    print("\nOutput:")
    for department, course_list in departments.items():
        print(f"{department}: {course_list}")


def session5_lecturer_assignments() -> None:
    """Session 5.1.1: Lecturer Assignments using dictionaries."""
    lecturer_assignments: Dict[str, List[str]] = {
        "Dr. Emily Brown": ["CS101", "MATH102"],
        "Prof. Jane Smith": ["CS202"],
        "Mr. Michael Johnson": ["PHY102"],
        "Prof. David Lee": ["PHY101"],
        "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
        "Dr. Noah Wilson": ["BIO101", "BIO102"],
        "Dr. Emma Davis": ["ENGL101"],
        "Prof. Evelyn Russell": ["ECON101", "ECON102"],
        "Dr. Lucas Sanchez": ["PSY101", "PSY102"],
        "Prof. Isabella Garcia": ["SOC101", "SOC102"],
    }

    print("\nLecturer Assignments")
    for lecturer, courses in lecturer_assignments.items():
        print(f"Lecturer {lecturer}: teaches {courses}")

    print("\nOutput:")
    for lecturer, courses in lecturer_assignments.items():
        print(f"{lecturer} -> {courses}")


def demo_session5() -> None:
    """Demonstration entry point for Session 5 tasks."""
    print("\n=== Session 5: Working with Dictionaries ===")
    session5_course_enrollments()
    session5_class_schedule()
    session5_lecturer_assignments()


def session6_user_input_loop() -> None:
    """Session 6.1: User input loop - build a class list until the user quits."""
    students: List[str] = []
    print("\nSession 6.1: Enter student names. Type 'quit', 'exit', or '0' to finish.")

    while True:
        name = input("Enter student name: ").strip()
        if name.lower() in {"quit", "exit", "0"}:
            print(f"\nExit command received: {name}")
            break
        if name:
            students.append(name)
            print(f"Added {name} to the class list.")

    print("\nFinal class list:")
    for student in students:
        print(f"- {student}")
    print(f"Total students entered: {len(students)}")


def session6_room_capacity_lookup() -> None:
    """Session 6.2: Locate rooms that can support the number of users."""
    rooms = [
        {"room": 101, "capacity": 15, "floor": "Ground", "location": "Building A"},
        {"room": 102, "capacity": 15, "floor": "Ground", "location": "Building A"},
        {"room": 103, "capacity": 20, "floor": "Ground", "location": "Building A"},
        {"room": 104, "capacity": 20, "floor": "Ground", "location": "Building A"},
        {"room": 105, "capacity": 25, "floor": "Ground", "location": "Building A"},
        {"room": 106, "capacity": 25, "floor": "Ground", "location": "Building A"},
        {"room": 107, "capacity": 30, "floor": "Ground", "location": "Building A"},
        {"room": 201, "capacity": 10, "floor": "1st", "location": "Building A"},
        {"room": 206, "capacity": 40, "floor": "1st", "location": "Building A"},
    ]

    print("\nSession 6.2: Enter the minimum number of seats required.")
    while True:
        value = input("Minimum seats required: ").strip()
        if not value.isdigit():
            print("Please enter a valid number.")
            continue
        required = int(value)
        break

    available = [room for room in rooms if room["capacity"] >= required]
    if not available:
        print("No room can support that number of students.")
        return

    chosen = min(available, key=lambda item: item["capacity"])
    print(f"Room {chosen['room']} can support {chosen['capacity']} students.")
    print(f"Floor: {chosen['floor']}, Location: {chosen['location']}")


def session6_exit_control_examples() -> None:
    """Session 6.3: Exit program loop examples with different control techniques."""
    print("\nSession 6.3 (1): Loop with exit commands and final summary.")
    students: List[str] = []
    while True:
        name = input("Enter student name (or quit/exit/0): ").strip()
        if name.lower() in {"quit", "exit", "0"}:
            print(f"Exit command used: {name}")
            break
        if name:
            students.append(name)
            print(f"Added {name}.")
    print(f"Students: {students}")
    print(f"Total students: {len(students)}")

    print("\nSession 6.3 (2): Loop controlled by an active variable.")
    students = []
    active = True
    while active:
        name = input("Enter student name (or 'stop'): ").strip()
        if name.lower() == "stop":
            active = False
            print("Stopping the loop.")
            continue
        if name:
            students.append(name)
            print(f"Added {name}.")
    print(f"Students entered: {students}")

    print("\nSession 6.3 (3): Exit with a break when max capacity is reached.")
    max_cap = 3
    students = []
    while True:
        if len(students) >= max_cap:
            print("Maximum capacity reached.")
            break
        name = input("Enter student name: ").strip()
        if name:
            students.append(name)
            print(f"Added {name}.")
    print(f"Students: {students}")
    print(f"Max capacity was {max_cap}.")


def session6_infinite_loop() -> None:
    """Session 6.4: Infinite loop until CTRL-C is pressed."""
    count = 0
    print("\nSession 6.4: Infinite loop. Press CTRL-C to stop.")
    try:
        while True:
            text = input("Enter text: ")
            count += 1
            print(f"Line {count}: {text}")
    except KeyboardInterrupt:
        print("\nInfinite loop stopped by user.")
        print(f"Total lines entered: {count}")


def main_menu() -> None:
    print("\n=== Advanced Network Security Practice Program ===")
    print("1. Run Session 5 dictionary demonstrations")
    print("2. Run Session 6 user input examples")
    print("3. Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        demo_session5()
    elif choice == "2":
        print("\nSession 6 sub-menu")
        print("a. User input loop")
        print("b. Room capacity lookup")
        print("c. Exit control examples")
        print("d. Infinite loop")
        sub = input("Choose a sub-option: ").strip().lower()
        if sub == "a":
            session6_user_input_loop()
        elif sub == "b":
            session6_room_capacity_lookup()
        elif sub == "c":
            session6_exit_control_examples()
        elif sub == "d":
            session6_infinite_loop()
        else:
            print("Invalid sub-option.")
    else:
        print("Goodbye.")


if __name__ == "__main__":
    main_menu()