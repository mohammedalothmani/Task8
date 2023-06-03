import subject_module
import student_module

subject = subject_module.Subject

subject1 = subject('math', 70)
subject2 = subject('arabic', 70)
subject3 = subject('Eng', 70)

studant = student_module.Student

studant1 = studant('mohammed', 20, 'gaza')
studant2 = studant('ali', 20, 'gaza')
studant3 = studant('ahmad', 20, 'gaza')

studant1.add_mark(75)
studant1.add_mark(80)
studant1.add_mark(90)

studant2.add_mark(60)
studant2.add_mark(75)
studant2.add_mark(68)

studant3.add_mark(90)
studant3.add_mark(95)
studant3.add_mark(88)

averg1 = studant1.calc_aver()
averg2 = studant2.calc_aver()
averg3 = studant3.calc_aver()
studant1 = studant1
