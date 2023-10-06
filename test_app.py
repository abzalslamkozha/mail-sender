from fastapi.testclient import TestClient
from app import app
from unittest.mock import Mock, patch
from smtp_config import send_email
from schemas import Message

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_send_email_success():
    smtp_mock = Mock()
    smtp_mock.starttls.return_value = None
    smtp_mock.login.return_value = None
    smtp_mock.sendmail.return_value = None
    smtp_mock.quit.return_value = None

    with patch('smtplib.SMTP', return_value=smtp_mock):
        to = 'recipient@example.com'
        subject = 'Test Subject'
        message = 'Test Message'
        message_request = {'to': to, 'subject': subject, 'message': message}

        result = send_email(Message(**message_request))

    assert result is "success"


def test_send_email_not_valid():
    to = 'invalid_email'
    subject = 'Test Subject'
    message = 'Test Message'
    invalid_request = {'to': to, 'subject': subject, 'message': message}

    response = client.post("/send-email", json=invalid_request)
    assert response.status_code == 422

