from fastapi import APIRouter
from script.core.handler.handler_student import add_student
from script.schema import Student
from script.utility.mongoDB import Students
from script.core.handler.handler_student import add_student, get_all_students, update_student, delete_student

student_router = APIRouter()


# Insert a student
@student_router.post("/addStudent/")
def course(student: Student):
    try:
        return add_student(student)
    except Exception as e:
        return {"error": str(e)}


# Get all students from Mongodb
@student_router.get("/getAllStudents")
def course():
    try:
        return get_all_students()
    except Exception as e:
        return {"error": str(e)}

        # updating the student record


@student_router.put("/updateStudent/{std_id}")
def course(std_id: int, student: Student):
    try:
        return update_student(std_id, student)
    except Exception as e:
        return {"error": str(e)}

        # Delete Student


@student_router.delete("/deleteStudentById/{std_id}")
def course(std_id: int):
    try:
        return delete_student(std_id)
    except Exception as e:
        return {"error": str(e)}
