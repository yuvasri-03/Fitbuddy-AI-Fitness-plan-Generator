from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    name: str
    age: int
    gender: str
    fitness_goal: str
    experience_level: str
    dietary_preference: str

class PlanResponse(BaseModel):
    id: int
    name: str
    workout_plan: str
    diet_plan: str

class UpdateGoalRequest(BaseModel):
    fitness_goal: str