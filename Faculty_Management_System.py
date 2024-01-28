class Faculty:
    def __init__(self, id, name, department, designation):
        self.id = id
        self.name = name
        self.department = department
        self.designation = designation

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Designation: {self.designation}"


class FacultyManagementSystem:
    def __init__(self):
        self.faculties = {}

    def add_faculty(self, faculty):
        self.faculties[faculty.id] = faculty
        print(f"Faculty added: {faculty}")

    def view_all_faculties(self):
        if not self.faculties:
            print("No faculties in the system.")
        else:
            for faculty_id, faculty in self.faculties.items():
                print(faculty)

    def search_faculty(self, faculty_id):
        if faculty_id in self.faculties:
            faculty = self.faculties[faculty_id]
            print(f"Faculty found:\n{faculty}")
        else:
            print(f"Faculty with ID {faculty_id} not found.")

    def update_faculty(self, faculty_id, new_designation):
        if faculty_id in self.faculties:
            self.faculties[faculty_id].designation = new_designation
            print(f"Faculty updated:\n{self.faculties[faculty_id]}")
        else:
            print(f"Faculty with ID {faculty_id} not found.")

    def delete_faculty(self, faculty_id):
        if faculty_id in self.faculties:
            deleted_faculty = self.faculties.pop(faculty_id)
            print(f"Faculty deleted:\n{deleted_faculty}")
        else:
            print(f"Faculty with ID {faculty_id} not found.")


if __name__ == "__main__":
    faculty_management_system = FacultyManagementSystem()

    # Example usage
    faculty1 = Faculty(id=1, name="John Doe", department="Computer Science", designation="Professor")
    faculty2 = Faculty(id=2, name="Jane Smith", department="Mathematics", designation="Associate Professor")

    faculty_management_system.add_faculty(faculty1)
    faculty_management_system.add_faculty(faculty2)

    faculty_management_system.view_all_faculties()

    faculty_management_system.search_faculty(1)

    faculty_management_system.update_faculty(1, "Senior Professor")

    faculty_management_system.delete_faculty(2)

    faculty_management_system.view_all_faculties()
