from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import threading
import uvicorn

backend = FastAPI()
frontend = FastAPI()

# CORS settings for the backend
backend.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Allow only GET methods
    allow_headers=["*"],  # Allow all headers
)

@backend.get("/status")
def read_status():
    return {"STATUS": "UP"}

@backend.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

frontend.mount("/", StaticFiles(directory="static", html=True), name="static")

def run_backend():
    uvicorn.run(backend, host="0.0.0.0", port=8000)

def run_frontend():
    uvicorn.run(frontend, host="0.0.0.0", port=80)

if __name__ == "__main__":
    backend_thread = threading.Thread(target=run_backend)
    frontend_thread = threading.Thread(target=run_frontend)
    
    backend_thread.start()
    frontend_thread.start()

    backend_thread.join()
    frontend_thread.join()
