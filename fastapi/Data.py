from pydantic import BaseModel


# 定義資料結構
class Data(BaseModel):
    name: str
