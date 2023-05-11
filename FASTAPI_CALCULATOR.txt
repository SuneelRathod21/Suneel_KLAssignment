from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"The addition of two numbers is: ": num1 + num2}


@app.get("/sub/{num1}/{num2}")
def sub(num1: int, num2: int):
    return {"The subtraction of two number is:": num1 * num2}


@app.get("/mul/{num1}/{num2}")
def mul(num1: int, num2: int):
    return {"The multiplication of two number is:": num1 * num2}


@app.get("/div/{num1}/{num2}")
def div(num1: int, num2: int):
    try:
        return {"the division of two number is:": num1 / num2}
    except:
        return {"divide by zero exception"}
