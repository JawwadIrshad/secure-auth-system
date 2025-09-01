from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.auth import users_db, hash_password

router = APIRouter()
otp_store = {}

class OTPRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    new_password: str

@router.post("/send-otp")
def send_otp(req: OTPRequest):
    if req.email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    import uuid
    otp = str(uuid.uuid4())[:6]
    otp_store[req.email] = otp
    print(f"OTP for {req.email}: {otp}")
    return {"message": "OTP has sent to (simulated)"}

@router.post("/reset-password")
def reset_password(req: ResetPasswordRequest):
    if otp_store.get(req.email) != req.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    users_db[req.email]["hashed_password"] = hash_password(req.new_password)
    del otp_store[req.email]
    return {"message": "Password has been reset successful"}
