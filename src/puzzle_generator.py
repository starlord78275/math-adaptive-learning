import random 

def generate_puzzle(difficulty):
    """
    Generates a math puzzel based on difficulty level.

    Args:
        difficulty (str): 'easy', 'medium', or 'hard'

    Returns: 
        tuple: (question_string, correct_answer)


    """

    if difficulty == "easy":
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operation = random.choice(['+','-'])

        if operation == '+':
            answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        else:
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
            question = f"{num1} - {num2} = ?"
        
    elif difficulty == "medium":
        num1 = random.randint(1,20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-','*'])

        if operation == '+':
            answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        elif operation == '-':
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
            question = f"{num1} - {num2} = ?"
        else:
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            answer = num1 * num2
            question = f"{num1} * {num2} = ?"

    else:
        operation = random.choice(['+','-','*','/'])

        if operation == '+':
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        elif operation == '-':
            num1 = random.randint(20, 50)
            num2 = random.randint(1, 20)
            answer = num1 - num2
            question = f"{num1} - {num2} = ?"

        elif operation == '*':
            num1 = random.randint(5, 15)
            num2 = random.randint(5, 15)
            answer = num1 * num2
            question = f"{num1} × {num2} = ?"
        else:
            answer = random.randint(2, 10)
            num2 = random.randint(2, 10)
            num1 = answer * num2
            question = f"{num1} ÷ {num2} = ?"
    
    return question, answer