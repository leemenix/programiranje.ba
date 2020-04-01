class Student:
	naziv_fakulteta = "Elektrotehnicki"
	pisac = "nije definisan"
	def __init__(self,ime,smjer,ocjena,brucos):
		self.ime = ime
		self.smjer = smjer
		self.ocjena = ocjena
		self.brucos = brucos

	def dobar(self):
		if self.ocjena > 8:
			return True
		else:
			return False

	def student_opis():
		print(f({self.naziv_fakulteta}, {self.ime}, {self.smjer}, {self,ocjena}, {self.brucos}, {self.pisac}))

	def student_pisac():
		print(self.pisac)