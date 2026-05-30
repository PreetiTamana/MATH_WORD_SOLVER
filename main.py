import re

def solve_problem(text):

    words = text.split()
    name = words[0]
        

    numbers = list(map(int, re.findall(r'\d+', text)))

    if "give" in text.lower():
        result = numbers[0] - numbers[1]
        
        explanation = f"""
        
Step 1: {name} starts with {numbers[0]} apples.
Step 2: and gives away {numbers[1]} apples.

{numbers[0]} - {numbers[1]} = {result}
Answer: {result} apples
"""
        
    elif "buys" or "gets" or "receives" in text.lower():  
        result = numbers[0] + numbers[1]

        explanation = f"""
        
Step 1: {name} starts with {numbers[0]} apples.
Step 2: and gives away {numbers[1]} apples.

{numbers[0]} + {numbers[1]} = {result}
Answer: {result} apples
"""

    else:
        explanation = "Operation not supported yet."

    return explanation

 


def main():

    print("\n🧠 MATH WORD PROBLEM SOLVER")
    print("-" * 40)

    while True:

        text = input("\nEnter math problem (or 'exit'): ")

        if text.lower() == "exit":
            break

        solution = solve_problem(text)

        print("\n📘 Solution:")
        print(solution)


if __name__ == "__main__":
    main()