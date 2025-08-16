from fastapi import FastAPI
from app.auth import router as auth_router
from app.otp import router as otp_router
from app.protected import router as protected_router

app = FastAPI()

# Register routers
app.include_router(auth_router)
app.include_router(otp_router)
app.include_router(protected_router)
