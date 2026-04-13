from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def create_task(db: Session, task_data: TaskCreate):
    task = Task(
        title = task_data.title,
        descripition = task_data.description,
        due_data = task_data.due_data,
    )
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task
    
    