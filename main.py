from app import app 
from flask import Flask,request,jsonify
from flask_cors import CORS 
from config import db 
from models import Employee, Department,Project

with app.app_context():
    db.create_all()
    """
    department1 = Department(name = "GL", location = "DEFIETCH")
    department2 = Department(name = "MRI", location = "DEFIETCH")
    department3 = Department(name = "SR", location = "DEFIETCH-II")

    employee1 = Employee(firstName="TOTO",lastName= "tata",department = department1)
    employee2 = Employee(firstName="MOI",lastName= "Lui")
    employee3 = Employee(firstName="MOI",lastName= "Toi")

    #department1.employees.append(employee1)
    db.session.add(department1)
    db.session.add(department2)
    db.session.add(department3)
    db.session.add(employee1)
    db.session.commit()
    """

""" Les methodes et routes """
    #### Les methodes d'ajout, liste, 
###--------------Pour la class Employee---------------------------------
@app.route('/employee/add', methods=['POST'])
def add_employee():
    try:
        json = request.json
        firstName = json['firstName']
        lastName = json['lastName']
        departmentId = json['departmentId']
        if firstName and lastName and request.method == 'POST':
            employee = Employee(firstName=firstName,lastName= lastName)
            if departmentId :
                department = Department.query.filter_by(id=departmentId).first()
                print(department)
                employee.department= department
            db.session.add(employee)
            db.session.commit()
            resultat = jsonify('Employee ajouté ♠♦')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
########-----------------Liste des Employee--------------------------


@app.route('/employees', methods=['GET'])
def all_employees():
    try:
        employees = Employee.query.all()
        data = [{"id": employee.id, "firstName": employee.firstName,"lastName":employee.lastName} for employee in employees]
        resultat = jsonify({"statut_code": 200,"users": data })
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
###------------------Delete Employee---------------------

@app.route('/employee/delete/', methods=['POST'])
def delete_employee():
    try:
        json = request.json
        id = json['id']
        employee = Employee.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()
        resultat = jsonify('Employee supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
######--------------------------update employee---------------------------------------
@app.route('/employee/update/', methods=['POST', 'GET'])
def update_employee():
    try:
        data = request.json
        id = data["id"]
        firstName = data["firstName"]
        lastName = data["lastName"]
        employee = Employee.query.filter_by(id=id).first()
        if id and firstName and lastName and request.method == 'POST':
            employee.firstName = firstName
            employee.lastName = lastName
            db.session.commit()
            resultat = jsonify('Employee mise à jour')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()



###---------------Pour la class Department
@app.route('/department/add', methods=['POST'])
def add_department():
    try:
        json = request.json
        name = json['name']
        location = json['location']
        if name and location and request.method == 'POST':
            department = Department(name=name,location = location, employees = [])

            db.session.add(department)
            db.session.commit()
            resultat = jsonify('Department ajouté ♠♦')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
##############---------------Liste des departments---------------------###########


@app.route('/departments', methods=['GET'])
def all_department():
    try:
        departments = Department.query.all()
        data = [{"id": department.id, "name": department.name,"location": department.location} for department in departments]
        resultat = jsonify({"statut_code": 200,"users": data })
        #resultat = jsonify(data)
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


########---------------Delete department---------------------

@app.route('/department/delete/', methods=['POST'])
def delete_department():
    try:
        json = request.json
        id = json['id']
        department = Department.query.filter_by(id=id).first()
        db.session.delete(department)
        db.session.commit()
        resultat = jsonify('department supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


###--------Pour la class Projet--------------------
@app.route('/project/add', methods=['POST'])
def add_project():
    try:
        json = request.json
        name = json['name']
        if name  and request.method == 'POST':
            project = Project(name=name)
            db.session.add(project)
            db.session.commit()
            resultat = jsonify('Project ajouté ♠♦')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
######-----------------------Liste des projects-----------------------------

@app.route('/projects', methods=['GET'])
def all_project():
    try:
        projects = Project.query.all()
        data = [{"id": project.id, "name": project.name} for project in projects]
        resultat = jsonify({"statut_code": 200,"users": data })
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
########---------------Delete project---------------------

@app.route('/project/delete/', methods=['POST'])
def delete_project():
    try:
        json = request.json
        id = json['id']
        project = Project.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()
        resultat = jsonify('Project supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
######--------------------------update project---------------------------------------
@app.route('/project/update/', methods=['POST', 'GET'])
def update_project():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        project = Project.query.filter_by(id=id).first()
        if id and name  and request.method == 'POST':
            project.firstName = name
            db.session.commit()
            resultat = jsonify('project mise à jour')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ == '__main__'):
    #app.run(host="192.168.1.176",port="3000")
    app.run(host=" 192.168.181.76",port="6000")