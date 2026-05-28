"""Módulo para revisar con pylint."""


class Student:
    """Clase de estudiante."""

    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, grade):
        """Añade una calificación a la lista de notas."""
        self.grades.append(grade)

    def calc_average(self):
        """Calcula el promedio de las notas del estudiante."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Devuelve la calificación en letra según el promedio."""
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

    def check_honor(self):
        """Actualiza el atributo honor si el estudiante tiene promedio mayor a 90."""
        self.honor = self.calc_average() > 90

    def determine_pass_fail(self):
        """Determina si el estudiante aprueba según su promedio."""
        self.is_passed = self.calc_average() >= 60
        return self.is_passed

    def remove_grade_by_index(self, index):
        """Elimina una calificación por índice si está dentro de los límites."""
        if 0 <= index < len(self.grades):
            self.grades.pop(index)
        else:
            print(f"Error: El índice {index} está fuera de los límites.")

    def remove_grade_by_value(self, value):
        """Elimina la primera calificación que coincide con el valor dado."""
        if value in self.grades:
            self.grades.remove(value)
        else:
            print("Error: La calificación" +  {value} +"no existe. No se eliminó.")

    def report(self):
        """Imprime el resumen del estudiante."""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.get_letter_grade())


def startrun():
    """Crea un estudiante y ejecuta las acciones de prueba."""
    a = Student("x", "Peru")
    a.add_grades(100)
    a.calc_average()
    a.check_honor()
    a.report()
    a.determine_pass_fail()


startrun()
