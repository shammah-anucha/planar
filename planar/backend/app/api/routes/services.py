from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_services() -> List[dict]:
    services = [
        {"id": 1, "name": "First service", "time": "11:00am"},
        {"id": 2, "name": "Second service", "time": "13:00pm"},
        {"id": 3, "name": "Third service", "time": "17:00pm"},
    ]

    return services
