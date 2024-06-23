from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    __people = []

    def __init__(self, name):
        self.__name = name

    def add_person(self, person):
        self.__people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__people:
            person.describe()

    def count_doctor(self):
        number_of_doctors = 0
        for person in self.__people:
            if isinstance(person, Doctor):
                number_of_doctors += 1
        return number_of_doctors

    def sort_age(self):
        self.__people.sort(key=lambda person: person._yob, reverse=True)

    def compute_average(self):
        number_of_teachers = 0
        total_age_teachers = 0
        for person in self.__people:
            if isinstance(person, Teacher):
                number_of_teachers += 1
                total_age_teachers += person._yob
        return total_age_teachers / number_of_teachers


student1 = Student("Student A", 2010, 7)

teacher1 = Teacher("Teacher A", 1969, 'Math')
teacher2 = Teacher("Teacher B", 1995, 'History')

doctor1 = Doctor("Doctor A", 1945, 'Endocringologists')
doctor2 = Doctor("Doctor B", 1975, 'Cardiologists')

ward1 = Ward('Ward 1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"Number of Doctors: {ward1.count_doctor()}")

print("After sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"Average year of birth (teachers): {ward1.compute_average()}")
