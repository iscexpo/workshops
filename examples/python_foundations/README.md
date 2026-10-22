# Python Foundations: Workshop Summary Example

This small, dependency-free program practices variables, conditionals, functions,
formatted strings, and basic input validation.

## Run

From the repository root:

```bash
python examples/python_foundations/workshop_summary.py
```

Expected output:

```
Workshop: Python Foundations
Activities planned: 3
Let's begin with the first activity!
```

## Test

```
python -m unittest discover -s examples/python_foundations/tests -v
```

The tests cover a positive activity count, zero activities, whitespace in a topic, an empty topic, and a negative count.

## Try changing it

1. Change the topic and run the program again.
2. Change the activity count to `0`.
3. Explain which condition selects the message.
4. Add a test for another behavior before changing the program.

The example is intentionally small so learners can read and explain each part.
