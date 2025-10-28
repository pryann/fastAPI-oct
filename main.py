from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}


# @app.get("/items/")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
