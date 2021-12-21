import uvicorn
from fastapi import FastAPI
from fastapi_socketio import SocketManager
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

socket_manager = SocketManager(app=app,
                               async_mode="asgi",
                               cors_allowed_origins="*")


@app.get('/')
def index():
    return '1337'


if __name__ == '__main__':
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=8000,
                debug=True,
                reload=True)
