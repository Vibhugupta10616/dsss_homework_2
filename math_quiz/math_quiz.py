import random

def random_input(min, max):
    """
    Choose a Random integer as Input.
    """
    try:
        min = int(min)    #check if the input is an integer
        max = int(max)    #check if the input is an integer
    except ValueError:
        raise ValueError("Please provide valid integers as input.")
    
    return random.randint(min, max)


def random_operator():
    """
    Choose a Random integer as Input.
    """
    return random.choice(['+', '-', '*'])


def operation(n1, n2, o):
    problem = f"{n1} {o} {n2}"
    if o == '+': ans = n1 + n2
    elif o == '-': ans = n1 - n2
    else: ans = n1 * n2
    return problem, ans

def math_quiz():
    """
    Conducts a math quiz game where the user is presented with random math problems.
    """

    score = 0
    t_q = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = random_input(1, 10); n2 = random_input(1, 5.5); o = random_operator()

        PROBLEM, ANSWER = operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
