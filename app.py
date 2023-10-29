#better way

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://halseyfilbin@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return self.first_name

def format_student(student):
    return {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'grade': student.grade
    }

@app.route('/students', methods=["GET"])
def get_all_students():
    students = Student.query.all()
    all_students = [format_student(student) for student in students]
    return jsonify(all_students)

@app.route('/old_students', methods=["GET"])
def get_old_students():
    students = Student.query.filter(Student.age > 20)
    old_students = [format_student(student) for student in students]
    return jsonify(old_students)

@app.route('/young_students', methods=["GET"])
def get_young_students():
    students = Student.query.filter(Student.age < 21)
    young_students = [format_student(student) for student in students]
    return jsonify(young_students)

@app.route('/advance_students', methods=["GET"])
def get_advanced_students():
    students = Student.query.filter(Student.age < 21, Student.grade == 'A')
    advanced_students = [format_student(student) for student in students]
    return jsonify(advanced_students)

@app.route('/student_names', methods=["GET"])
def get_student_names():
    students = Student.query.all()
    student_names = [{"first_name": student.first_name, "last_name": student.last_name} for student in students]
    return jsonify(student_names)

@app.route('/student_ages', methods=["GET"])
def get_student_ages():
    students = Student.query.all()
    student_ages = [{"student_name": f"{student.first_name} {student.last_name}", "age": student.age} for student in students]
    return jsonify(student_ages)

app.run(debug=True)



# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://halseyfilbin@localhost/students"

# db = SQLAlchemy(app)

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20))
#     last_name = db.Column(db.String(20))
#     age = db.Column(db.Integer)
#     grade = db.Column(db.String(1))

#     def __repr__(self):
#         return self.first_name
    
# @app.route('/students', methods = ["GET"])
# def get_students():
#     students = Student.query.all()
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "id": stud.id,
#                 "first_name": stud.first_name,
#                 "last_name": stud.last_name,
#                 "age": stud.age,
#                 "grade": stud.grade
#             }
#         )
#     return jsonify(formatted_students)

# @app.route('/old_students', methods = ["GET"])
# def get_old_students():
#     students = Student.query.filter(Student.age > 20)
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "id": stud.id,
#                 "first_name": stud.first_name,
#                 "last_name": stud.last_name,
#                 "age": stud.age,
#                 "grade": stud.grade
#             }
#         )
#     return jsonify(formatted_students)

# @app.route('/young_students', methods = ["GET"])
# def get_young_students():
#     students = Student.query.filter(Student.age < 21)
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "id": stud.id,
#                 "first_name": stud.first_name,
#                 "last_name": stud.last_name,
#                 "age": stud.age,
#                 "grade": stud.grade
#             }
#         )
#     return jsonify(formatted_students)

# @app.route('/advance_students', methods = ["GET"])
# def get_advance_students():
#     students = Student.query.filter(Student.age < 21, Student.grade == 'A')
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "id": stud.id,
#                 "first_name": stud.first_name,
#                 "last_name": stud.last_name,
#                 "age": stud.age,
#                 "grade": stud.grade
#             }
#         )
#     return jsonify(formatted_students)

# @app.route('/student_names', methods = ["GET"])
# def get_student_names():
#     students = Student.query.all()
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "first_name": stud.first_name,
#                 "last_name": stud.last_name,
#             }
#         )
#     return jsonify(formatted_students)

# @app.route('/student_ages', methods = ["GET"])
# def get_student_ages():
#     students = Student.query.all()
#     formatted_students = []
#     for stud in students:
#         formatted_students.append(
#             {
#                 "student_name": stud.first_name + " " + stud.last_name,
#                 "age": stud.age,
#             }
#         )
#     return jsonify(formatted_students)

# app.run(debug=True)