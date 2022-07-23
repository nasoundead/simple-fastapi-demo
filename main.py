from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from order import index





app = FastAPI()


app.include_router(index.router, prefix='/order')

origins = ['http://localhost',
           'http://localhost:8080']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def read_root():
    return {"message": "ok"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host="localhost",
                port=8000, reload=True, debug=True)
