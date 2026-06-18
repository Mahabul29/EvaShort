import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import PORT, HOST

app = FastAPI()

# Automatically detect where your files are located
if os.path.exists("public"):
    STATIC_DIR = "public"
else:
    STATIC_DIR = "."

# 1. Route for the home page (/)
@app.get("/")
async def read_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Backend running. index.html not found."}

# 2. Dynamic Route for all other pages (e.g., /calculator.html)
@app.get("/{page_name}")
async def get_page(page_name: str):
    file_path = os.path.join(STATIC_DIR, page_name)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail=f"{page_name} not found")

# 3. Mount static files so styles and script bundles can load
if STATIC_DIR == "public":
    app.mount("/public", StaticFiles(directory="public"), name="public")
else:
    app.mount("/assets", StaticFiles(directory="."), name="assets")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT)
    
