"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 0, 2, 3, 0, 4, 5, 0]],
            "answer": [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
        },
        {
            "input": [[0, 0, 0, 0]],
            "answer": [0, 0, 0, 0, 0, 0, 0, 0]
        },
        {
            "input": [[100, 10, 0, 101, 1000]],
            "answer": [100, 10, 0, 0, 101, 1000]
        }
    ],
    "Extra": [
        {
            "input": [[1, 2, 3, 4, 5]],
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "input": [[0]],
            "answer": [0, 0]
        },
        {
            "input": [[1, 0, 0, 1, 0, 0, 1, 1, 0]],
            "answer": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
        }
    ]
}
