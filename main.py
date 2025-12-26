from models.student import Student
from models.subject import Subject

def main():
    print("=== Student Grader CLI Demo ===\n")

    # Create initial subjects

    english = Subject("English", 100, 75, "Mr. Smith")
    mathematics = Subject("Mathematics", 100, 88, "Dr. Johnson")
    physics = Subject("Physics", 100, 92, "Dr. Brown")
    chemistry = Subject("Chemistry", 100, 81, "Ms. Davis")
    biology = Subject("Biology", 100, 85, "Dr. Wilson")
    history = Subject("History", 100, 70, "Mr. Taylor")
    geography = Subject("Geography", 100, 78, "Ms. Clark")
    computerScience = Subject("Computer Science", 100, 95, "Dr. White")
    art = Subject("Art", 100, 90, "Ms. Lewis")
    physicalEducation= Subject("Physical Education", 100, 100, "Coach Martin")

    subList1 = [english,chemistry,geography]
    subList2 = [physics,mathematics,history]
    subList3 = [biology,computerScience]

    # Create a student
    
    student1 = Student("Alice", 12, subList1)
    student2 = Student("Bob", 14, subList2)
    student3 = Student("Charlie", 13, subList3)

    # Show basic info

    print(student1)
    print(f"Average Grade: {student1.averageGrade()}\n")
    print(student2)
    print(f"Average Grade: {student2.averageGrade()}\n")
    print(student3)
    print(f"Average Grade: {student3.averageGrade()}\n")

    # List subjects
    student1.listSubjects()
    student2.listSubjects()
    student3.listSubjects()

    # Add a new subject
    print("\n--- Adding Subject ---\n")

    student1.addSubject(art)
    student1.listSubjects()

    student3.addSubject(physicalEducation)
    student3.listSubjectsDetails

    # Remove a subject by index
    print("\n--- Removing Subject ---")
    student2.removeSubject(1)
    student2.listSubjectsDetails()

    print("\n=== Demo Complete ===")

    print("\n=== Doc Strings Start===\n")
    print("=== Student ===\n")
    print(Student.__doc__)
    print("\n===========\n")
    print("=== Subject ===\n")
    print(Subject.__doc__)
    print("\n===========\n")
    print("\n=== Doc Strings End===\n")


if __name__ == "__main__":
    main()
