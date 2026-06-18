import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import PORT, HOST

app = FastAPI()

# Mount your public folder so all your HTML/CSS/JS files load properly
if os.path.exists("public"):
    app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/")
async def read_index():
    # Serves your main index.html file from the public directory
    index_path = os.path.join("public", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Welcome to EvaShort! Put your index.html inside a 'public' folder."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
  
