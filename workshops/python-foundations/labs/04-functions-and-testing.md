# Lab 4: Functions and Testing

**Goal:** understand how a function receives inputs and how tests protect behavior.

## 1. Read the function

The function receives a topic and an activity count. It returns a string containing the summary. The `if` / `else` selects the final message.

## 2. Run the program

From the repository root:

```bash
python examples/python_foundations/workshop_summary.py
```

Compare the output with the example README.

## 3. Run the tests

```
python -m unittest discover -s examples/python_foundations/tests -v
```

A passing test means the actual result matched the expected result for that case. Tests do not prove every possible input is correct; they check the cases you have written.

## 4. Extend the example

Try these changes on your own branch:

1. Add a test for a topic with leading and trailing spaces.
2. Add a test for an empty topic.
3. Change the zero-activity message and update the test to match.
4. Run all tests again and explain which behavior each test protects.

## Reflection

- What is the difference between a parameter and an argument?
- Why does a function use `return` here?
- What did the tests catch that simply running the example might not catch?

Keep each experiment small, and run the tests after changing the code.
