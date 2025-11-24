import json
import os

class Student:
    def __init__(self, student_id, name, age, grade, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Student(data['id'], data['name'], data['age'], data['grade'], data['email'])

class StudentManager:
    def __init__(self, file_path="students.json"):
        self.students = []
        self.file_path = file_path
        self.load_students()

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        print("-" * 50)
        for s in self.students:
            print(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Grade: {s.grade}, Email: {s.email}")
        print("-" * 50)

    def search_student(self, keyword):
        results = [s for s in self.students if keyword.lower() in s.name.lower() or keyword == s.student_id]
        if not results:
            print("No student found.")
        else:
            for s in results:
                print(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Grade: {s.grade}, Email: {s.email}")

    def update_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(f"Editing Student: {s.name}")
                s.name = input("Enter new name (leave blank to keep): ") or s.name
                try:
                    age = input("Enter new age (leave blank to keep): ")
                    s.age = int(age) if age else s.age
                except ValueError:
                    print("Invalid age input. Keeping old value.")
                s.grade = input("Enter new grade (leave blank to keep): ") or s.grade
                s.email = input("Enter new email (leave blank to keep): ") or s.email
                print("Student updated.")
                return
        print("Student ID not found.")

    def delete_student(self, student_id):
        for i, s in enumerate(self.students):
            if s.student_id == student_id:
                del self.students[i]
                print(f"Student '{s.name}' deleted.")
                return
        print("Student ID not found.")

    def save_students(self):
        with open(self.file_path, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)
        print("Data saved.")

    def load_students(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(item) for item in data]
            print("Data loaded.")
        else:
            print("No existing data file. Starting fresh.")

def display_menu():
    print("""
========= Student Management System =========
1. Add New Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Save to File
7. Exit
============================================
""")

def main():
    manager = StudentManager()
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. Setting to 0.")
                age = 0
            grade = input("Enter student grade: ")
            email = input("Enter student email: ")
            student = Student(student_id, name, age, grade, email)
            manager.add_student(student)
        
        elif choice == '2':
            manager.view_students()
        
        elif choice == '3':
            keyword = input("Enter name or ID to search: ")
            manager.search_student(keyword)

        elif choice == '4':
            student_id = input("Enter student ID to update: ")
            manager.update_student(student_id)

        elif choice == '5':
            student_id = input("Enter student ID to delete: ")
            manager.delete_student(student_id)

        elif choice == '6':
            manager.save_students()

        elif choice == '7':
            manager.save_students()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


