"""FastAPI Main entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, conversations, customers
from .core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(conversations.router)
app.include_router(customers.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
