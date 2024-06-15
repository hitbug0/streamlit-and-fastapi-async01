import asyncio

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalculationRequest(BaseModel):
    x: int


@app.post("/calculate")
async def calculate(request: CalculationRequest):
    result = await long_computation(request.x)
    return {"result": result}


async def long_computation(x):
    await asyncio.sleep(5)  # Simulating a long computation
    return x * x
