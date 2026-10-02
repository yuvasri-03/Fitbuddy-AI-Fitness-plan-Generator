import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def regenerate_plan_with_new_goal(user, new_goal):
    model = genai.GenerativeModel('gemini-3.8-flash')
    
    prompt = f"""
    Regenerate a 7-day workout and diet plan for {user[1]} who updated their goal to: {new_goal}.
    Previous Level: {user[5]}, Gender: {user[3]}, Diet Preference: {user[6]}.

    Format output clearly as:
    ---WORKOUT PLAN---
    [New workout plan]

    ---DIET PLAN---
    [New diet plan]
    """
    
    response = model.generate_content(prompt)
    text = response.text
    
    if "---DIET PLAN---" in text:
        parts = text.split("---DIET PLAN---")
        workout = parts[0].replace("---WORKOUT PLAN---", "").strip()
        diet = parts[1].strip()
    else:
        workout = text
        diet = "Updated diet plan."
        
    return workout, diet