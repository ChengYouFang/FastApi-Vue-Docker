from celery import Celery
from Data import Data

# 設定Redis
celery = Celery(__name__, broker='redis://redis:6379', backend='redis://redis:6379')


@celery.task()
def my_task(data: Data):
    # 取得原先傳遞的資料
    return {"name": data}
