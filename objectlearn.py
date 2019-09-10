class Student():
    def __init__ (stud,name,age,idno):
        stud.name=name
        stud.age=age
        stud.idno=idno
    def output(stud):
        print("Name:",stud.name,"\nAge:",stud.age,"\nID no:",stud.idno)

p=Student('Jamsheer','25','1245')
q=Student('Ali','25','1245')
p.output()
q.output()