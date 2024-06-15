import asyncio

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/wait/{time_}/{words_}")
async def wait_time(time_: float, words_: str):
    ret = await sleep_time(time_, words_)
    return JSONResponse(content=ret)


async def sleep_time(time_, words_):
    print(f"{words_}: sleep {time_} seconds")
    await asyncio.sleep(time_)
    print(f"{words_}: wake up")
    return {"message": f"{words_} slept in {time_} seconds"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
