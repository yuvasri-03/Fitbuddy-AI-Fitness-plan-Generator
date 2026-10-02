from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas import UserRequest
from app.database import (
    save_user_plan,
    get_user_plan,
    get_all_users,
    update_user_goal_and_plan
)
from app.gemini_generator import generate_fitness_plan
from app.updated_plan import regenerate_plan_with_new_goal
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@router.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    fitness_goal: str = Form(...),
    experience_level: str = Form(...),
    dietary_preference: str = Form(...)
):
    user_data = UserRequest(
        name=name,
        age=age,
        gender=gender,
        fitness_goal=fitness_goal,
        experience_level=experience_level,
        dietary_preference=dietary_preference
    )

    workout, diet = generate_fitness_plan(user_data)
    user_id = save_user_plan(user_data, workout, diet)

    return RedirectResponse(
        url=f"/result/{user_id}",
        status_code=303
    )


@router.get("/result/{user_id}", response_class=HTMLResponse)
def show_result(request: Request, user_id: int):
    user = get_user_plan(user_id)

    if not user:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"user": user}
    )


@router.get("/users", response_class=HTMLResponse)
def list_users(request: Request):
    users = get_all_users()

    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"users": users}
    )


@router.post("/update/{user_id}")
def update_goal(
    user_id: int,
    new_goal: str = Form(...)
):
    user = get_user_plan(user_id)

    if user:
        new_workout, new_diet = regenerate_plan_with_new_goal(
            user,
            new_goal
        )

        update_user_goal_and_plan(
            user_id,
            new_goal,
            new_workout,
            new_diet
        )

    return RedirectResponse(
        url=f"/result/{user_id}",
        status_code=303
    )
