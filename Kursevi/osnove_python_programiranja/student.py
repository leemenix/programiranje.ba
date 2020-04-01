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

	def student_opis(self):
		print(f"Ime studenta: {self.ime}, Naziv fakulteta: {self.naziv_fakulteta}, Smjer: {self.smjer}, Ocjena: {self.ocjena}, Brucos: {self.brucos}, Pisac: {self.pisac}")

	def student_pisac(self):
		print(self.pisac)