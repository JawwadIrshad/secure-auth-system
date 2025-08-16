# 🔐 Secure Role-Based Auth System (Modular FastAPI)

## 📂 Folder Structure

```
secure-auth-system/
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── otp.py
│   └── protected.py
├── requirements.txt
└── README.md
```

## ✅ Features

- Register and login with password hashing
- JWT token for auth
- Role-based authorization
- Send OTP (simulated)
- Reset password with OTP

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then go to: http://127.0.0.1:8000/docs

Test the full flow: register → login → get token → access protected → send OTP → reset password

## 📥 Submission

Zip and submit this project or upload demo video showing the full flow.
