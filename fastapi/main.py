from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from enum import IntEnum
from worker import my_task
from Data import Data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskStatus(IntEnum):
    NONE = 0
    SUCCESS = 1
    PENDING = 2
    FAILURE = 3
    RETRY = 4
    STARTED = 5


@app.get('/get_task_result/{uuid}', status_code=200)
async def get_task_result(uuid: str):
    # 取得執行結果
    task = AsyncResult(uuid)
    if task.status == 'SUCCESS':
        return JSONResponse({"status": TaskStatus.SUCCESS.value, "result": task.result})
    elif task.status == 'PENDING':
        return JSONResponse({"status": TaskStatus.PENDING.value})
    elif task.status == 'FAILURE':
        return JSONResponse({"status": TaskStatus.FAILURE.value})
    elif task.status == 'RETRY':
        return JSONResponse({"status": TaskStatus.RETRY.value})
    elif task.status == 'STARTED':
        return JSONResponse({"status": TaskStatus.STARTED.value})
    else:
        return JSONResponse({"status": TaskStatus.NONE.value})


@app.post("/create_task", status_code=200)
async def create_task(data: Data):
    result = my_task.delay(data.name)
    return JSONResponse({"id": result.id})