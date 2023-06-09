import uvicorn
# from scripts.configuration import Service
from fastapi import FastAPI
from script.core.services.Student_services import student_router

app = FastAPI()
app.include_router(student_router)
if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)