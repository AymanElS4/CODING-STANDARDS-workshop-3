class Student:
    """Clase de estudiante."""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, g):
        self.grades.append(g)

    def calc_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def checkHonor(self):
        if self.calc_average() > 90:
            self.honor = True

    def remove_grade_by_index(self, index):
        if 0 <= index < len(self.grades):
            self.grades.pop(index)
        else:
            print(f"Error: El índice {index} está fuera de los límites.")

    def remove_grade_by_value(self, value):
        if value in self.grades:
            self.grades.remove(value)
        else:
            print(f"Error: La calificación '{value}' no existe. No se eliminó nada.")

    def report(self):  
        """Imprime el resumen del estudiante."""

        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + get_letter_grade(self))


def startrun():
    """Crea un estudiante y ejecuta las acciones de prueba."""

    a = Student("x", "")
    a.add_grades(100)
    a.calc_average()
    a.checkHonor()
    a.report()


startrun()
