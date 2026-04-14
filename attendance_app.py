import os
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import date

# --- Configuration ---
TEACHER_PASSWORD = "admin123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENTS_FILE = os.path.join(BASE_DIR, "students.txt")
ATTENDANCE_FILE = os.path.join(BASE_DIR, "attendance.txt")

# --- Data functions ---

def ensure_data_files():
    """Ensure that the data files exist.

    Creates the student and attendance files if they do not already exist.
    """
    try:
        for path in (STUDENTS_FILE, ATTENDANCE_FILE):
            if not os.path.exists(path):
                with open(path, "a", encoding="utf-8"):
                    pass
    except OSError as e:
        messagebox.showerror("File Error", f"Unable to access data files:\n{e}")


def load_students():
    """Return a dict of student_id -> student_name."""
    students = {}
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "," not in line:
                    continue
                student_id, name = line.split(",", 1)
                students[student_id.strip()] = name.strip()
    except OSError:
        # If file cannot be read, return empty dict.
        pass
    return students


def save_student(student_id: str, name: str):
    """Append a new student record to the students file."""
    try:
        with open(STUDENTS_FILE, "a", encoding="utf-8") as f:
            f.write(f"{student_id},{name}\n")
    except OSError as e:
        messagebox.showerror("File Error", f"Unable to save student:\n{e}")


def load_attendance():
    """Return a list of (date_str, student_id, status) attendance records."""
    records = []
    try:
        with open(ATTENDANCE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "," not in line:
                    continue
                parts = line.split(",")
                if len(parts) < 3:
                    continue
                records.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    except OSError:
        pass
    return records


def save_attendance(date_str: str, student_id: str, status: str):
    """Append an attendance line to the attendance file."""
    try:
        with open(ATTENDANCE_FILE, "a", encoding="utf-8") as f:
            f.write(f"{date_str},{student_id},{status}\n")
    except OSError as e:
        messagebox.showerror("File Error", f"Unable to save attendance:\n{e}")


# --- GUI Helpers ---

def center_window(win: tk.Tk | tk.Toplevel, width: int = 460, height: int = 360):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")


# --- Application ---

class AttendanceApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Student Attendance Management")
        self.root.resizable(False, False)
        center_window(self.root, 460, 300)
        ensure_data_files()
        self.show_login()

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_root()

        frame = ttk.Frame(self.root, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Select your role", font=(None, 16, "bold")).pack(pady=(0, 12))

        role_var = tk.StringVar(value="teacher")
        ttk.Radiobutton(frame, text="Teacher", variable=role_var, value="teacher").pack(anchor="w")
        ttk.Radiobutton(frame, text="Student", variable=role_var, value="student").pack(anchor="w")

        password_frame = ttk.Frame(frame)
        student_frame = ttk.Frame(frame)

        password_var = tk.StringVar()
        student_id_var = tk.StringVar()

        def render_fields(*_):
            for w in password_frame.winfo_children():
                w.destroy()
            for w in student_frame.winfo_children():
                w.destroy()

            if role_var.get() == "teacher":
                ttk.Label(password_frame, text="Teacher password:").pack(anchor="w")
                ttk.Entry(password_frame, textvariable=password_var, show="*").pack(fill="x")
                password_frame.pack(fill="x", pady=(12, 0))
                student_frame.forget()
            else:
                ttk.Label(student_frame, text="Student ID:").pack(anchor="w")
                ttk.Entry(student_frame, textvariable=student_id_var).pack(fill="x")
                student_frame.pack(fill="x", pady=(12, 0))
                password_frame.forget()

        role_var.trace_add("write", render_fields)
        render_fields()

        def on_login():
            role = role_var.get()
            if role == "teacher":
                if password_var.get().strip() != TEACHER_PASSWORD:
                    messagebox.showerror("Login Failed", "Incorrect teacher password.")
                    return
                self.show_teacher_menu()
            else:
                sid = student_id_var.get().strip()
                if not sid:
                    messagebox.showerror("Input Error", "Please enter a student ID.")
                    return
                students = load_students()
                if sid not in students:
                    messagebox.showerror(
                        "Not Found",
                        "Student ID not found. Ask your teacher to register you first.",
                    )
                    return
                self.show_student_menu(sid)

        ttk.Button(frame, text="Login", command=on_login).pack(pady=(18, 0))

    def show_teacher_menu(self):
        self.clear_root()
        self.root.title("Teacher - Attendance Management")

        frame = ttk.Frame(self.root, padding=18)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Teacher Menu", font=(None, 16, "bold")).pack(pady=(0, 14))

        ttk.Button(frame, text="Register Student", width=28, command=self.register_student).pack(pady=6)
        ttk.Button(frame, text="Mark Attendance (Today)", width=28, command=self.mark_attendance).pack(pady=6)
        ttk.Button(frame, text="View Attendance", width=28, command=self.view_attendance_menu).pack(pady=6)
        ttk.Button(frame, text="Logout", width=28, command=self.logout).pack(pady=(16, 0))

    def show_student_menu(self, student_id: str):
        self.clear_root()
        self.root.title("Student - Attendance Viewer")

        frame = ttk.Frame(self.root, padding=18)
        frame.pack(fill="both", expand=True)

        students = load_students()
        name = students.get(student_id, "(unknown)")

        ttk.Label(frame, text=f"Hello, {name}", font=(None, 16, "bold")).pack(pady=(0, 12))
        ttk.Label(frame, text=f"Student ID: {student_id}").pack(pady=(0, 16))

        ttk.Button(
            frame,
            text="View My Attendance",
            width=26,
            command=lambda: self.view_student_attendance(student_id),
        ).pack(pady=6)
        ttk.Button(frame, text="Logout", width=26, command=self.logout).pack(pady=(14, 0))

    def logout(self):
        self.root.title("Student Attendance Management")
        self.show_login()

    def register_student(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Register Student")
        dlg.resizable(False, False)
        center_window(dlg, 400, 220)

        frame = ttk.Frame(dlg, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Student ID:").pack(anchor="w")
        student_id_var = tk.StringVar()
        ttk.Entry(frame, textvariable=student_id_var).pack(fill="x")

        ttk.Label(frame, text="Student Name:").pack(anchor="w", pady=(10, 0))
        student_name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=student_name_var).pack(fill="x")

        def on_register():
            student_id = student_id_var.get().strip()
            name = student_name_var.get().strip()
            if not student_id or not name:
                messagebox.showerror("Input Error", "Both ID and name are required.")
                return
            students = load_students()
            if student_id in students:
                messagebox.showwarning(
                    "Already Registered",
                    "This student ID is already registered."
                )
                return
            save_student(student_id, name)
            messagebox.showinfo(
                "Registered",
                f"Student '{name}' (ID: {student_id}) registered successfully.",
            )
            dlg.destroy()

        ttk.Button(frame, text="Register", command=on_register).pack(pady=(14, 0))

    def mark_attendance(self):
        students = load_students()
        if not students:
            messagebox.showinfo("No Students", "There are no students registered yet.")
            return

        today = date.today().isoformat()
        dlg = tk.Toplevel(self.root)
        dlg.title("Mark Attendance")
        dlg.resizable(False, False)
        center_window(dlg, 520, 520)

        frame = ttk.Frame(dlg, padding=14)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=f"Mark Attendance for {today}", font=(None, 14, "bold")).pack(pady=(0, 10))

        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        vars_by_id = {}
        for sid, name in sorted(students.items(), key=lambda i: i[1].lower()):
            var = tk.BooleanVar(value=True)
            vars_by_id[sid] = var
            row = ttk.Frame(scroll_frame)
            row.pack(fill="x", pady=2)
            ttk.Checkbutton(row, variable=var).pack(side="left")
            ttk.Label(row, text=f"{sid} - {name}").pack(side="left", padx=8)

        def on_save():
            for sid, var in vars_by_id.items():
                status = "Present" if var.get() else "Absent"
                save_attendance(today, sid, status)
            messagebox.showinfo("Saved", "Attendance has been recorded.")
            dlg.destroy()

        ttk.Button(frame, text="Save Attendance", command=on_save).pack(pady=(10, 0))

    def view_attendance_menu(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("View Attendance")
        dlg.resizable(False, False)
        center_window(dlg, 460, 360)

        frame = ttk.Frame(dlg, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="View Attendance", font=(None, 14, "bold")).pack(pady=(0, 10))

        ttk.Button(frame, text="View Full Class", width=28, command=self.view_full_class).pack(pady=6)
        ttk.Button(
            frame,
            text="View One Student",
            width=28,
            command=lambda: self.view_student_prompt(dlg),
        ).pack(pady=6)
        ttk.Button(frame, text="Close", width=28, command=dlg.destroy).pack(pady=(14, 0))

    def view_full_class(self):
        records = load_attendance()
        if not records:
            messagebox.showinfo("No Records", "No attendance records have been saved yet.")
            return

        students = load_students()
        self._show_attendance_table(records, students, title="Class Attendance")

    def view_student_prompt(self, parent):
        students = load_students()
        if not students:
            messagebox.showinfo("No Students", "There are no students registered yet.")
            return

        student_id = simpledialog.askstring(
            "Student ID", "Enter student ID:", parent=parent)
        if not student_id:
            return

        student_id = student_id.strip()
        if student_id not in students:
            messagebox.showerror("Not Found", "Student ID not found.")
            return

        self.view_student_attendance(student_id)

    def view_student_attendance(self, student_id: str):
        students = load_students()
        student_name = students.get(student_id, "(unknown)")

        records = [r for r in load_attendance() if r[1] == student_id]
        if not records:
            messagebox.showinfo("No Records", "No attendance records for this student.")
            return

        self._show_attendance_table(records, students, title=f"Attendance for {student_name} ({student_id})")

    def _show_attendance_table(self, records, students, title: str):
        dlg = tk.Toplevel(self.root)
        dlg.title(title)
        dlg.resizable(True, True)
        center_window(dlg, 620, 440)

        frame = ttk.Frame(dlg, padding=12)
        frame.pack(fill="both", expand=True)

        columns = ("date", "student_id", "name", "status")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=14)
        tree.heading("date", text="Date")
        tree.heading("student_id", text="ID")
        tree.heading("name", text="Name")
        tree.heading("status", text="Status")
        tree.column("date", width=120, anchor="center")
        tree.column("student_id", width=90, anchor="center")
        tree.column("name", width=220)
        tree.column("status", width=90, anchor="center")

        for date_str, sid, status in sorted(records):
            name = students.get(sid, "(unknown)")
            tree.insert("", "end", values=(date_str, sid, name, status))

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ttk.Button(frame, text="Close", command=dlg.destroy).pack(pady=(8, 0))


def main():
    root = tk.Tk()
    AttendanceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
