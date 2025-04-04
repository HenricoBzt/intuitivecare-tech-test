from app.backend.database import Base, engine
from app.backend.router import operadoras
from app.backend.population import population_operadoras
from contextlib import asynccontextmanager

from fastapi import FastAPI

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await population_operadoras("app/backend/csv/operadoras_ativas.csv")
    yield
    await engine.dispose()

app = FastAPI(title='INTUITIVECARE FASTAPI',lifespan=lifespan)
app.include_router(operadoras.router)




@app.get("/")
def read_root():
    return {"API": "Welcome to the API To Intuitive Care"}
