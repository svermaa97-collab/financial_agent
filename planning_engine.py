def calculate_savings(user_input):
    import re
    numbers = [int(s) for s in re.findall(r'\d+', user_input)]
    
    if "save" in user_input or "goal" in user_input:
        if len(numbers) >= 2:
            goal_amount = numbers[0]
            months = numbers[1]
            monthly_saving = goal_amount // months
            return f"To save {goal_amount} in {months} months, invest {monthly_saving} per month."
        return "Please provide your goal amount and duration in months."
    
    if "expense" in user_input or "spend" in user_input:
        if len(numbers) >= 1:
            expense = numbers[0]
            return f"Noted your monthly expense: {expense}."
        return "Please provide your expense amount."

    return "I can help you plan your savings. Ask me a question!"
