import random


def rand_int(min, max):
    """
    Generate random integer.
    """
    return random.randint(min, max)          #Returns two random integers between the given min and max.


def rand_op():
    """
    Generate random operator. 
    """
    return random.choice(['+', '-', '*'])     # Returns +, - or * randomly.


def rand_prob(n1, n2, o):
    """
    Generate random problem and its answer.
    """
    p = f"{n1} {o} {n2}"
    if o == '-': a = n1 - n2
    elif o == '+': a = n1 + n2
    else: a = n1 * n2 
    return p, a                                #'p' is the problem and 'a' is the answer.

def math_quiz():
    """
    Runs the math quiz game.
    """
    s = 0
    t_q = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range (t_q):                  #Used to generate a certain number of problems.
        n1 = rand_int(1, 10); n2 = rand_int(1, int(5.5)); o = rand_op()

        PROBLEM, ANSWER = rand_prob(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}") #Displays the final score.

if __name__ == "__main__":
    math_quiz()
