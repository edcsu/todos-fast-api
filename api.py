from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcom() -> dict:
	return {"message": "Hello World"}
