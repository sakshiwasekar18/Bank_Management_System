from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def checkhealth():
  return{
    "message":"fastapi is working"
  }