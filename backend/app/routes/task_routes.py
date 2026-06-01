from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate
from app.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=int(user["sub"])
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    tasks = (
        db.query(Task)
        .filter(Task.owner_id == int(user["sub"]))
        .all()
    )

    return tasks


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    db_task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == int(user["sub"])
        )
        .first()
    )

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db_task.title = task.title
    db_task.description = task.description

    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    db_task = (
        db.query(Task)
        .filter(
        Task.id == task_id,
        Task.owner_id == int(user["sub"])
    )
        .first()
    )

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(db_task)
    db.commit()

    return {
        "message": "Task deleted"
    }