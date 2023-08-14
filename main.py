from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello Sang"}

@app.get("/add/{num1}/{num2}")
async def add(num1:int, num2:int):
    """Add two number together"""

    return {"Sum": num1 + num2}

if __name__=='__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')