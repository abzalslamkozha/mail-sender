from fastapi import FastAPI
from schemas import Message
from smtp_config import send_email

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/send-email")
async def send_email_endpoint(message: Message):
    result = send_email(message)

    if result == "success":
        response = "Email sent successfully!"
    else:
        response = f"Email could not be sent. Error: {str(result)}"

    return {"message": response}
