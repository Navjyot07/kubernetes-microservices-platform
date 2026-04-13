from fastapi import FastAPI
import time
import requests


app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from Kubernetes"}


# CPU-bound API
@app.get("/cpu")
def cpu_task(n: int = 5000000):
    total = 0
    for i in range(n):
        total += i
    return {"result": total}


# IO-bound API (simulate DB/API call)
@app.get("/io")
def io_task():
    time.sleep(2)  # simulate DB delay
    return {"message": "IO task completed"}


# External API call (real IO)
@app.get("/external")
def external_call():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return res.json()


# Memory-bound API
@app.get("/memory")
def memory_task(size: int = 10000000):
    data = ["x"] * size
    return {"message": f"Allocated {size} items"}
