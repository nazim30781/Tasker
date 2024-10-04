from fastapi import APIRouter

router = APIRouter(
    prefix="tasks",
    tags=["Task"]
)


@router.get("/getAllTasks")
async def get_all_tasks():
    pass


@router.post("/createTask")
async def create_task():
    pass


@router.get("/getUnfulfilledTasks")
async def get_unfulfilled_tasks():
    pass
