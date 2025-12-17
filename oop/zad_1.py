from typing import List


class Student:
    def __init__(self, name: str, marks: List[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False

        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Weronika", [60, 50, 70])
student2 = Student("Ola", [40, 70, 30])

print(student1.name, student1.is_passed())
print(student2.name, student2.is_passed())
