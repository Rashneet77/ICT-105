# Name: Rashneet Takhi
# Student ID: 12045112
# ICT105 Worksheet 5
# Advanced Network Security - Session 9 & 10
# Author: Tosh



from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
SUMMARY_FILE = DATA_DIR / "python_summary.txt"
LEARNING_FILE = DATA_DIR / "learning_students.txt"
STUDENTS_CSV = DATA_DIR / "students.csv"
STUDENTS_C1 = DATA_DIR / "students_c1.txt"
STUDENTS_C2 = DATA_DIR / "students_c2.txt"
ERROR_LOG = DATA_DIR / "error.log"
FAVOURITE_NUMBER_FILE = DATA_DIR / "favorite_number.json"
REMEMBERED_NUMBER_FILE = DATA_DIR / "remembered_number.json"
USER_PROFILE_FILE = DATA_DIR / "user_profile.txt"
USER_PROFILE_JSON = DATA_DIR / "user_profile.json"


class ExerciseOne:
    def __init__(self, file_path: Path = SUMMARY_FILE) -> None:
        self.file_path = file_path

    def write_summary(self) -> None:
        content = (
            "Python is a powerful programming language that supports object-oriented programming, "
            "easy file handling, and clear error management.\n"
            "Using try-except blocks helps programs avoid crashes and provide friendly messages when "
            "things go wrong.\n"
            "Good debugging practices include tracing execution flow, using print statements or "
            "a debugger, and validating assumptions at each step.\n"
        )
        try:
            self.file_path.write_text(content, encoding="utf-8")
            print(f"Created summary file: {self.file_path}")
        except (OSError, PermissionError) as exc:
            print(f"Unable to write summary file: {exc}")

    def read_all(self) -> None:
        try:
            content = self.file_path.read_text(encoding="utf-8")
            print("\n--- Read entire file content ---")
            print(content)
        except FileNotFoundError:
            print(f"Error: file not found: {self.file_path}")
        except PermissionError:
            print(f"Error: permission denied reading {self.file_path}")

    def read_lines(self) -> None:
        try:
            with self.file_path.open("r", encoding="utf-8") as fp:
                lines = fp.readlines()
            print("\n--- Read file line by line ---")
            for idx, line in enumerate(lines, start=1):
                print(f"Line {idx}: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: file not found: {self.file_path}")
        except PermissionError:
            print(f"Error: permission denied reading {self.file_path}")


class ExerciseTwo:
    def __init__(self, file_path: Path = LEARNING_FILE) -> None:
        self.file_path = file_path

    def replace_learner_with_student(self) -> None:
        if not self.file_path.exists():
            print(f"Error: file not found: {self.file_path}")
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as fp:
                for line in fp:
                    modified = re.sub(
                        r"\blearners?\b",
                        lambda match: "Student" if match.group(0)[0].isupper() else "student",
                        line,
                        flags=re.IGNORECASE,
                    )
                    print(modified.rstrip())
        except PermissionError:
            print(f"Error: permission denied reading {self.file_path}")


class ExerciseThree:
    def prompt_and_add(self) -> None:
        try:
            first = input("Enter the first number: ").strip()
            second = input("Enter the second number: ").strip()
            total = int(first) + int(second)
            print(f"Result: {total}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


class ExerciseFour:
    def run_calculator(self) -> None:
        print("Repeatable calculator. Type 'q' to quit.")
        while True:
            first = input("First number: ").strip()
            if first.lower() == "q":
                break
            second = input("Second number: ").strip()
            if second.lower() == "q":
                break
            try:
                total = int(first) + int(second)
                print(f"Total: {total}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        print("Calculator session ended.")


class ExerciseFive:
    def split_students(self) -> None:
        try:
            with STUDENTS_CSV.open("r", encoding="utf-8", newline="") as csv_file:
                reader = list(csv.reader(csv_file))
            if not reader:
                raise ValueError("Student CSV is empty")

            header = reader[0]
            rows = reader[1:]
            midpoint = len(rows) // 2 or 1
            self._write_split(rows[:midpoint], STUDENTS_C1, header)
            self._write_split(rows[midpoint:], STUDENTS_C2, header)
            print(f"Created {STUDENTS_C1.name} and {STUDENTS_C2.name}")
        except FileNotFoundError:
            print(f"Error: missing CSV file: {STUDENTS_CSV}")
        except PermissionError:
            print(f"Error: permission denied reading {STUDENTS_CSV}")
        except ValueError as exc:
            print(f"Error: {exc}")

    def _write_split(self, rows: list[list[str]], path: Path, header: list[str]) -> None:
        path.write_text(
            "\n".join(
                [
                    ",".join(header),
                    *[",".join(row) for row in rows],
                ]
            ),
            encoding="utf-8",
        )

    def read_file(self, path: Path, silent: bool = False) -> None:
        try:
            content = path.read_text(encoding="utf-8")
            print(f"\n--- Contents of {path.name} ---")
            print(content)
        except FileNotFoundError:
            message = f"Friendly error: missing file {path.name}."
            if silent:
                sys.stderr.write(f"{message}\n")
            else:
                print(message)
        except PermissionError:
            message = f"Permission denied for {path.name}."
            if silent:
                sys.stderr.write(f"{message}\n")
            else:
                print(message)

    def read_both_files(self, silent: bool = False) -> None:
        self.read_file(STUDENTS_C1, silent=silent)
        self.read_file(STUDENTS_C2, silent=silent)


class ExerciseSix:
    def store_favourite_number(self) -> None:
        try:
            favourite = input("Enter your favourite number: ").strip()
            data = {"favourite_number": int(favourite)}
            with FAVOURITE_NUMBER_FILE.open("w", encoding="utf-8") as fp:
                json.dump(data, fp)
            print(f"Saved favourite number to {FAVOURITE_NUMBER_FILE.name}")
        except ValueError:
            print("Please enter a valid integer.")
        except PermissionError:
            print(f"Error: permission denied writing {FAVOURITE_NUMBER_FILE}")

    def display_favourite_number(self) -> None:
        try:
            with FAVOURITE_NUMBER_FILE.open("r", encoding="utf-8") as fp:
                data = json.load(fp)
            print(f"Your favourite number is {data['favourite_number']}.")
        except FileNotFoundError:
            print("No favourite number found. Run the store function first.")
        except (json.JSONDecodeError, KeyError):
            print("The favourite number file is corrupt or missing expected data.")
        except PermissionError:
            print(f"Error: permission denied reading {FAVOURITE_NUMBER_FILE}")


class ExerciseSeven:
    def remember_favourite_number(self) -> None:
        if REMEMBERED_NUMBER_FILE.exists():
            try:
                with REMEMBERED_NUMBER_FILE.open("r", encoding="utf-8") as fp:
                    data = json.load(fp)
                print(f"I remember your favourite number is {data['favourite_number']}.")
                return
            except (json.JSONDecodeError, KeyError):
                print("Saved data is invalid. Please enter your favourite number again.")

        try:
            favourite = int(input("Enter your favourite number: ").strip())
            with REMEMBERED_NUMBER_FILE.open("w", encoding="utf-8") as fp:
                json.dump({"favourite_number": favourite}, fp)
            print("Your favourite number has been saved.")
        except ValueError:
            print("Please enter a valid integer.")
        except PermissionError:
            print(f"Error: permission denied writing {REMEMBERED_NUMBER_FILE}")


class ExerciseEight:
    def create_profile(self) -> None:
        student_id = input("Enter a student ID: ").strip()
        profile = {"student_id": student_id}
        try:
            with USER_PROFILE_FILE.open("w", encoding="utf-8") as fp:
                json.dump(profile, fp)
            print(f"Saved student ID to {USER_PROFILE_FILE.name}")
        except PermissionError:
            print(f"Error: permission denied writing {USER_PROFILE_FILE}")

    def load_profile(self) -> dict[str, str] | None:
        try:
            with USER_PROFILE_FILE.open("r", encoding="utf-8") as fp:
                return json.load(fp)
        except FileNotFoundError:
            print(f"Profile file {USER_PROFILE_FILE.name} does not exist.")
            return None
        except json.JSONDecodeError:
            print(f"Profile file {USER_PROFILE_FILE.name} contains invalid JSON.")
            return None
        except PermissionError:
            print(f"Error: permission denied reading {USER_PROFILE_FILE}")
            return None

    def add_details(self) -> None:
        profile = self.load_profile()
        if profile is None:
            return

        dob = input("Enter student DOB: ").strip()
        email = input("Enter student email: ").strip()
        profile.update({"dob": dob, "email": email})
        try:
            with USER_PROFILE_FILE.open("w", encoding="utf-8") as fp:
                json.dump(profile, fp)
            print(f"Updated profile saved to {USER_PROFILE_FILE.name}")
        except PermissionError:
            print(f"Error: permission denied writing {USER_PROFILE_FILE}")

    def show_summary(self) -> None:
        profile = self.load_profile()
        if not profile:
            return
        print("\n--- Profile Summary ---")
        print(f"Student ID: {profile.get('student_id', 'N/A')}")
        print(f"DOB: {profile.get('dob', 'N/A')}")
        print(f"Email: {profile.get('email', 'N/A')}")


def create_sample_files() -> None:
    if not LEARNING_FILE.exists():
        LEARNING_FILE.write_text(
            "Every learner must complete their assignments on time. A good learner always seeks to learn more.\n"
            "Learners are the future leaders.\n",
            encoding="utf-8",
        )
        print(f"Created sample file: {LEARNING_FILE.name}")

    if not STUDENTS_CSV.exists():
        STUDENTS_CSV.write_text(
            "student_id,name,class,email\n"
            "S1001,Aisha,Class 1,aisha@example.com\n"
            "S1002,Ben,Class 1,ben@example.com\n"
            "S1003,Cara,Class 2,cara@example.com\n"
            "S1004,David,Class 2,david@example.com\n"
            "S1005,Elena,Class 1,elena@example.com\n"
            "S1006,Fahad,Class 2,fahad@example.com\n",
            encoding="utf-8",
        )
        print(f"Created sample file: {STUDENTS_CSV.name}")

    if not USER_PROFILE_FILE.exists():
        USER_PROFILE_FILE.write_text(
            json.dumps({"student_id": "S1001"}, indent=2), encoding="utf-8"
        )
        print(f"Created starter profile file: {USER_PROFILE_FILE.name}")


def main() -> None:
    create_sample_files()
    menu = {
        "1": "Exercise 1: File read/write with error handling",
        "2": "Exercise 2: Replace learner with student",
        "3": "Exercise 3: Add two numbers with ValueError handling",
        "4": "Exercise 4: Repeatable calculator",
        "5": "Exercise 5: Split students and read files",
        "6": "Exercise 6: Save and read favourite number",
        "7": "Exercise 7: Remember favourite number",
        "8": "Exercise 8: Create and update user profile",
        "q": "Quit",
    }

    while True:
        print("\nSession 9 Exercise Menu")
        for key, description in menu.items():
            print(f"{key}. {description}")
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            break

        if choice == "1":
            ex = ExerciseOne()
            ex.write_summary()
            ex.read_all()
            ex.read_lines()
        elif choice == "2":
            ExerciseTwo().replace_learner_with_student()
        elif choice == "3":
            ExerciseThree().prompt_and_add()
        elif choice == "4":
            ExerciseFour().run_calculator()
        elif choice == "5":
            ex5 = ExerciseFive()
            if not STUDENTS_C1.exists() or not STUDENTS_C2.exists():
                ex5.split_students()
            print("\nReading both student files with friendly output:")
            ex5.read_both_files(silent=False)
            print("\nReading both student files silently and logging errors to stderr:")
            ex5.read_both_files(silent=True)
        elif choice == "6":
            ex6 = ExerciseSix()
            ex6.store_favourite_number()
            ex6.display_favourite_number()
        elif choice == "7":
            ExerciseSeven().remember_favourite_number()
        elif choice == "8":
            ex8 = ExerciseEight()
            ex8.create_profile()
            ex8.add_details()
            ex8.show_summary()
        else:
            print("Invalid choice. Please select a valid option.")

    print("Goodbye!")


if __name__ == "__main__":
    main()
 