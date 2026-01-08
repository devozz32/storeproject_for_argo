import os
from fastapi import FastAPI

app = FastAPI(title="My Service", version="1.0.0")

@app.get("/")
def hello():
    return {"message": "hello from my server"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)

