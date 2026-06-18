import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import PORT, HOST

app = FastAPI()

# 1. Determine where your frontend files live
if os.path.exists("public"):
    STATIC_DIR = "public"
else:
    STATIC_DIR = "."  # Root folder fallback

# 2. Serve the home page (index.html)
@app.get("/")
async def read_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": f"index.html not found in '{STATIC_DIR}'. Please check your file placement."}

# 3. Mount static files so CSS, JS, and Images load properly
if STATIC_DIR == "public":
    app.mount("/public", StaticFiles(directory="public"), name="public")
else:
    # If files are in root, serve everything else dynamically
    app.mount("/assets", StaticFiles(directory="."), name="assets")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT)
    
