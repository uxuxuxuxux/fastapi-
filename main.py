from fastapi import FastAPI

# インスタンス生成
app = FastAPI()

# http://127.0.0.1:8000/items/???にアクセスすると返ってくる。
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}