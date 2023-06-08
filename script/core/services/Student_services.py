from fastapi import APIRouter
from script.schema import StudentDatabase
from script.core.handler.handler_student import handler_obj

student_router = APIRouter()


@student_router.post("/create_student/")
def create_student_database(students: StudentDatabase):
    return handler_obj.add_new_student(students)


@student_router.delete("/del_student")
def del_student(new_name: str):
    return handler_obj.del_student(new_name)


@student_router.get("/get_student")
def read_database():
    return handler_obj.view_all_data()


@student_router.get("/get_avg_age")
def get_avg_age():
    return handler_obj.cal_avg_age()
