from student import Student

novi_student = Student("Goku", "programiranje", 7.9, False)
print(novi_student.naziv_fakulteta)
#novi_student.ime = "Goku"
#novi_student.ocjena = 7.9

print(novi_student.ime)
print(novi_student.dobar())
novi_student.naziv_fakulteta = "Prirodno Matematicki"
novi_student.smjer = "Fizika"
novi_student.ocjena = 9.0

print(novi_student.ime)
print(novi_student.naziv_fakulteta)
print(novi_student.dobar())
print(novi_student.student_opis())
print(novi_student.student_pisac())