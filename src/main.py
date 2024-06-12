import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get1")
async def get1():
    ret = await long_time()
    return JSONResponse(content=ret)

async def long_time():
    print("long:  start")
    await asyncio.sleep(3)
    print("long:  end")
    return {"message": "long end"}


@app.get("/get2")
async def get2():
    ret = await short_time()
    return JSONResponse(content=ret)

async def short_time():
    print("short: start")
    await asyncio.sleep(0.01)
    print("short: end")
    return {"message": "short end"}






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
