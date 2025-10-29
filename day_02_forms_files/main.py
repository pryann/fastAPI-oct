from pathlib import Path
from fastapi import FastAPI, UploadFile
import uvicorn


app = FastAPI()

# create uploads directory if not exists
# os.makedirs("uploads", exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload_file(file: UploadFile):
    safe_filename = Path(file.filename).name
    upload_dir = Path("uploads")
    # create uploads directory if not exists
    upload_dir.mkdir(exist_ok=True)
    file_path = upload_dir / safe_filename

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "filename": safe_filename,
        "location": str(file_path),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
