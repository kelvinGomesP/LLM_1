from llm import chain
from langserve import add_routes
from fastapi import FastAPI

app = FastAPI(title="Meu App", description="Traduza seu texto")

add_routes(app, chain, path="/tradutor")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
