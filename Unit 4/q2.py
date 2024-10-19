class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person Created.")

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __del__(self):
        print(f"Person {self.name} Destroyed.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print("Student Created.")

    def getData(self):
        return f"{self.get_details()}, Student ID: {self.student_id}"

    def __del__(self):
        print(f"Student {self.name} Destroyed.")


class Result(Student):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age, student_id)
        self.marks = marks
        print("Result Created.")

    def calculate_HighMarks(self):
        highest = max(self.marks)
        lowest = min(self.marks)
        return highest, lowest

    def dispHighMarks(self):
        highest, lowest = self.calculate_HighMarks()
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")

    def __del__(self):
        print(f"Result for {self.name} Destroyed.")


class HonorsResult(Result):
    def __init__(self, name, age, student_id, marks, honors_classification=""):
        super().__init__(name, age, student_id, marks)
        self.honors_classification = honors_classification
        print("Honors Result Created.")

    def calc_average(self):
        return sum(self.marks) / len(self.marks)

    def determine_honors(self):
        average = self.calc_average()
        if average >= 75:
            self.honors_classification = "First Class"
        elif 60 <= average < 75:
            self.honors_classification = "Second Class"
        else:
            self.honors_classification = "Pass Class"

    def dispHonors(self):
        self.determine_honors()
        print(f"Honors Classification: {self.honors_classification}")

    def __del__(self):
        print(f"Honors Result for {self.name} Destroyed.")


h1 = HonorsResult("Alice", 22, "S123", [85, 78, 92, 88])

print(h1.getData())

h1.dispHighMarks()

h1.dispHonors()

del h1
