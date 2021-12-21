import uvicorn
from core import app, router


app.include_router(
    router,
    prefix='/events',
    tags=['Events']
)


if __name__ == '__main__':
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=8000,
                debug=True,
                reload=True)
