from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
import uvicorn
import logging
from datetime import datetime

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Enhanced Task API")

# Tambahkan CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model untuk Task dengan validasi
class Task(BaseModel):
    id: Optional[int] = Field(None, gt=0, description="Unique task ID")
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: Optional[str] = Field(None, max_length=500, description="Task description")
    completed: bool = Field(False, description="Task completion status")
    created_at: datetime = Field(default_factory=datetime.now)

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty or only whitespace")
        return v.strip()

    @field_validator("description")
    @classmethod
    def description_must_not_be_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("Description cannot be empty or only whitespace")
        return v.strip() if v else None

# Simulasi database sederhana
tasks_db: List[Task] = []
current_id = 1

def get_next_id() -> int:
    global current_id
    id = current_id
    current_id += 1
    return id

@app.get("/tasks", response_model=List[Task])
async def get_tasks(
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    search: Optional[str] = Query(None, description="Search tasks by title or description")
):
    """Mengembalikan daftar tugas dengan opsi filter dan pencarian."""
    try:
        filtered_tasks = tasks_db
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == completed]
        if search:
            search = search.lower()
            filtered_tasks = [
                task for task in filtered_tasks
                if search in task.title.lower() or (task.description and search in task.description.lower())
            ]
        logger.info(f"Retrieved {len(filtered_tasks)} tasks")
        return filtered_tasks
    except Exception as e:
        logger.error(f"Error retrieving tasks: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Mengembalikan tugas berdasarkan ID."""
    try:
        for task in tasks_db:
            if task.id == task_id:
                logger.info(f"Retrieved task with ID {task_id}")
                return task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        logger.error(f"Error retrieving task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """Membuat tugas baru."""
    try:
        task.id = get_next_id()
        tasks_db.append(task)
        logger.info(f"Created task with ID {task.id}")
        return task
    except Exception as e:
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    """Memperbarui tugas berdasarkan ID."""
    try:
        for index, task in enumerate(tasks_db):
            if task.id == task_id:
                updated_task.id = task_id  # Ensure ID remains the same
                tasks_db[index] = updated_task
                logger.info(f"Updated task with ID {task_id}")
                return updated_task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        logger.error(f"Error updating task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Menghapus tugas berdasarkan ID."""
    try:
        for index, task in enumerate(tasks_db):
            if task.id == task_id:
                tasks_db.pop(index)
                logger.info(f"Deleted task with ID {task_id}")
                return {"message": "Task deleted successfully"}
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)