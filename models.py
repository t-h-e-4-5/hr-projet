from config import db 

"""  Création des class (les tables) et les liens(ManyToMany, ManyToOne, OneToMany)  """

"""
Les types 
Integer
String()
Text
DateTime
Float
Boolean
LargeBinary
PickleType

Les proprietes

primary_key
nullable
index
unique
"""
    ### La table Employee ###
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    firstName = db.Column(db.String(120),nullable = False)
    lastName = db.Column(db.String(120),nullable = False)
        ### Liaison ### OneToMany
    departmentId = db.Column(db.Integer, db.ForeignKey('department.id'), nullable = True)
    department = db.relationship('Department', foreign_keys = [departmentId])
        ### OneToOne
    isHeadOf = db.Column(db.Integer, db.ForeignKey('department.id'), nullable = True)
    manager = db.relationship('Department', foreign_keys = [isHeadOf])

    ### La table Departement ###
class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120),nullable = False)
    location = db.Column(db.String(120),nullable = False)
        ### Liaison ### 'Employee' c'est la class ### backref(variable virtuel 'department' qui sera crée dans la class Employee )
            ### Role de backref on sauras pas qu'elle colone sera la relation ###
    #employees = db.relationship('Employee', backref = 'depart')
        #### OneToOne
    #head = db.relationship('Employee', backref = 'headOfDepartment')

    ### La table Project ###
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120),nullable = False)

    ### ManyToMany
projectMembers = db.Table('project_members',
                db.Column('employee_id', db.ForeignKey('employee.id'),primary_key = True),
                db.Column('project_id', db.ForeignKey('project.id'),primary_key = True)
                        )