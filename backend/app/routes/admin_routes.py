from fastapi import APIRouter, Depends

from app.auth import require_admin

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def admin_dashboard(
    admin=Depends(require_admin)
):
    return {
        "message": "Welcome Admin"
    }