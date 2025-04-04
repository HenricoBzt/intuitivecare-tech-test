from app.backend.database import Base, engine
from app.backend.router import operadoras
from app.backend.population import population_operadoras
from contextlib import asynccontextmanager
"""
Import the CORSMiddleware from FastAPI to handle Cross-Origin Resource Sharing (CORS) configurations.

This middleware allows configuring cross-origin requests, enabling web applications 
to make requests to the API from different domains by setting appropriate HTTP headers.
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await population_operadoras("app/backend/csv/operadoras_ativas.csv")
    yield
    await engine.dispose()

app = FastAPI(title='INTUITIVECARE FASTAPI',lifespan=lifespan)
app.include_router(operadoras.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)




@app.get("/")
def read_root():
    return {"API": "Welcome to the API To Intuitive Care"}
