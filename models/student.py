from models.subject import Subject
class Student:
    """
    Represents a student with personal information and enrolled subjects.

    A Student object tracks the student's name, age, and the list of subjects
    they are enrolled in. Each subject is represented by a `Subject` instance,
    which contains grading and teacher information. Input values are validated
    to ensure correctness and consistency.

    Attributes
    ----------
    name : str
        The student's name (3–30 characters).
    age : int
        The student's age (1–30 years).
    subjects : list of Subject
        A list of `Subject` instances representing the student's enrolled subjects.

    Methods
    -------
    name : property
        Get or set the student's name with validation.
    age : property
        Get or set the student's age with validation.
    subjects : property
        Get or set the list of subjects. Returns an empty list if no subjects exist.
    """
    def __init__(self,name: str ,age :int, subjects: list):
        self.name = name
        self.age = age
        self.subjects = subjects

    @property
    def name(self) -> str:
        return self.__name 
    
    @name.setter
    def name(self,value: str) -> None:
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError("student name must be string")
        if len(value) > 2 and len(value) <= 30:
            self.__name = value
        else:
            raise ValueError("student name length must be between 3 - 30")
        
    @property
    def age(self) -> float:
        return float(self.__age)
    
    @age.setter
    def age(self,value: int) -> None:
        if not isinstance(value,int):
            raise TypeError("age must be an integer")
        if value > 0 and value <= 30:
            self.__age = value
        else:
            raise ValueError("age value must be between 0 - 30")
        
    @property
    def subjects(self) -> list:
        if not self.__subjects:
            return []
        return self.__subjects
    
    @subjects.setter
    def subjects(self,value: list) -> None:
        if not isinstance(value,list):
            raise TypeError("subjects must be a list")
        if not value:
            return ValueError("list can not be empty")
        for i in range(len(value)):
            if not isinstance(value[i],Subject):
                raise TypeError("subjects list must contain only subjects")
        self.__subjects = value
            
    def averageGrade(self) -> str:
        if not self.subjects:
            return 0.0
        totalMaxGrade = 0.0
        totalGrade = 0.0
        for i in range(len(self.subjects)):
            totalGrade += self.subjects[i].grade
            totalMaxGrade += self.subjects[i].maxGrade 
        return f"{round(totalGrade/totalMaxGrade,2)*100}%"
    
    def __str__(self) -> str:
        return f'student: {self.name.title()} | age: {self.age} | subjects: {len(self.subjects)}'
    
    def listSubjects(self) -> None:
        if not self.subjects:
            return f"{self.name.title()} has no subjects"
        print("----------------\n")
        print(f"{self.name.title()}'s Subjects:\n")
        for i,n in enumerate(self.subjects,1):
            print(f"{i}. Subject: {n.name.title()} | Grade Percentage: {n.averageGrade()}%\n")
        print("----------------\n")

    def listSubjectsDetails(self) -> None:
        if not self.subjects:
            return f"{self.name.title()} has no subjects"
        print("----------------\n")
        print(f"{self.name}'s Subjects:\n")
        for i,n in enumerate(self.subjects,1):
            print(f"{i}. {str(n)}\n")
        print("----------------\n")

    def addSubject(self,subject: Subject) -> None:
        if not isinstance(subject,Subject):
            raise TypeError("must be a subject")
        self.subjects.append(subject)
        print(f"Added: {subject.name.title()}\n")

    def removeSubject(self,index:int) -> None:
        if not self.subjects:
            return f"{self.name.title()} has no subjects"
        if not isinstance(index,int):
            raise TypeError("must be a integer")
        if index < 1 or index > len(self.subjects):
            raise ValueError(f"subject index must be between 1 - {len(self.subjects)}")
        removedSubject = self.subjects.pop(index - 1)
        print(f"Removed: {removedSubject.name.title()}\n")
        
