from script.utility.mongoDB import Students
from script.schema import Student


def add_student(student: Student):
    student_dict = student.dict()
    result = Students.insert_one(student_dict)
    return {"id": "Student added successfully"}


def get_all_students():
    student = Students.find({})
    details = []
    for document in student:
        detail = {'id': document['id'], 'name': document['name'], 'address': document['address']}
        details.append(detail)
    return {"details": details}


def update_student(std_id: int, student: Student):
    result = Students.update_one({"id": std_id}, {"$set": student.dict()})
    if result.modified_count > 0:
        return {"message": "Student updated successfully"}
    else:
        return {"error": "Student not found"}


def delete_student(std_id: int):
    if std_id in Students.find({}):
        try:
            Students.delete_one({"id": std_id})
            return {"message": "Student deleted successfully"}
        except Exception as e:
            return {"error": "Student not found"}
    else:
        return {"error": "Nothing to delete"}
