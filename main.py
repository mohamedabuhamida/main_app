from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def welcome_message():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/predict")
def predict_image():
    return {"message": "This "}