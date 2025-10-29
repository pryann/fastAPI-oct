from pathlib import Path
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

# create uploads directory if not exists
# os.makedirs("uploads", exist_ok=True)

# http://localhost:8000/uploads/FILENAME
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


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


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = Path("uploads") / filename

    if file_path.exists() and file_path.is_file():
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="application/octet-stream",  # force download
        )
    raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
