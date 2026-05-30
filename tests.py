from main import solve_problem

test_cases = [
    "John has 5 apples and gives away 2.",
    "Sarah has 10 candies and gives away 4.",
    "Mike has 8 books and gives away 3."
]

for i, test in enumerate(test_cases):

    print(f"\n🧪 Test {i+1}")
    print("Input:", test)
    print(solve_problem(test))