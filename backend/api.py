from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/chat")
def chat(message: dict):
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # use string import path, not the variable itself
        host="127.0.0.1",
        port=8000,
        reload=True,  # 👈 enables hot reload
    )