from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base

from app.routes.auth_routes import router as auth_router
from app.routes.task_routes import router as task_router
from app.routes.admin_routes import router as admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Primetrade Assignment API",
    version="1.0.0",
    description="REST API with JWT Authentication, RBAC and Task CRUD"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(admin_router)


@app.get("/")
def root():
    return {
        "message": "API Running"
    }