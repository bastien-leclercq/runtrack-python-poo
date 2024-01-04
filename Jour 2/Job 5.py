class Student:
    def __init__(self, name, surname, student_number, credit=0):
        self._name = name
        self._surname = surname
        self._student_number = student_number
        self._credit = credit

    def add_credit(self, credit):
        if credit > 0:
            self._credit += credit
        else:
            print("Can't add negative credit number!")

    def studentEval(self):
        if self._credit >= 90:
            return 'Excellent'
        elif self._credit >= 80:
            return 'Très bien.'
        elif self._credit >= 70:
            return 'Bien'
        elif self._credit >= 60:
            return 'Passable'
        else:
            return 'Insuffisant'

    def studentInfo(self):
        print('Nom =', self._name, '\nPrénom =', self._surname, '\nid =', self._student_number, '\nNiveau =',
              self.studentEval())

