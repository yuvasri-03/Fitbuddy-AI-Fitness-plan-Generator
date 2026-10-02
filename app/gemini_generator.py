from app.schemas import UserRequest

def generate_fitness_plan(user_data: UserRequest):
    workout = """Day 1: Upper Body (Pushups, Dumbbell Press)
Day 2: Lower Body (Squats, Lunges)
Day 3: Core & Cardio (Plank, Jumping Jacks)"""

    diet = """Breakfast: Oatmeal with fruits & nuts
Lunch: Brown Rice with Grilled Protein & Veggies
Dinner: Salad with Lean Protein"""

    return workout, diet