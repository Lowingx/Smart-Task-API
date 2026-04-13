from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ────────────────────────────────
# - Base
# ────────────────────────────────
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

# ────────────────────────────────
# - Criar a tarefa
# ────────────────────────────────
class TaskCreate(TaskBase):
    due_data: Optional[datetime] = None
    
# ────────────────────────────────
# - Atualizar a tarefa
# ────────────────────────────────
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None
    
# ────────────────────────────────
# - Resposta
# ────────────────────────────────
class TaskResponse(TaskBase):
    id: int
    status: str
    priority_score: int
    priority_level: str
    created_at: datetime
    due_date: Optional[datetime]
    
    class Config:
        from_attributes = True