# Python Foundations: First Steps

**Level:** Beginner · **Duration:** 90 minutes · **Status:** Draft  
**Audience:** Learners new to programming  
**Maintainer:** [ISC Expo Workshops maintainers](mailto:info@iscexpo.edu.bd) · **Last reviewed:** Not yet reviewed

## Learning outcomes

By the end, learners should be able to:

- Run a short Python program.
- Store and display text and numbers using variables.
- Use a conditional to choose between two outcomes.
- Explain what a simple function takes as input and returns.

## Prerequisites and setup

No previous programming experience is required. Bring a computer where Python 3 is available, or use an approved classroom environment provided by the facilitator. A local editor and terminal are sufficient. Setup may differ by operating system; facilitators should test the environment before class.

Check Python:

```bash
python --version
```

If this command is unavailable, try `python3 --version` or ask the facilitator to help with setup. Do not install unfamiliar software on a managed device without permission.

## Session plan

| Time | Activity | Goal |
|---:|---|---|
| 0–10 min | What is a program? | Connect instructions to everyday examples |
| 10–25 min | Run and change a print statement | Practice editing and executing code |
| 25–40 min | Variables and simple values | Name, store, and display information |
| 40–55 min | Conditions | Make a program choose an outcome |
| 55–70 min | Small function | Reuse a named set of instructions |
| 70–85 min | Mini challenge | Combine concepts independently or in pairs |
| 85–90 min | Reflection | Explain one thing learned and one question |

## Guided activity 1: first output

Create a file named `hello.py`:

```python
print("Hello, ISC Expo!")
print("I am learning by building.")
```

Expected output:

```text
Hello, ISC Expo!
I am learning by building.
```

Run it with `python hello.py` (or `python3 hello.py`). Change the message and run it again.

**Check your learning:** What does `print()` do? What changed when you edited the text?

## Guided activity 2: variables and conditions

```python
learner_name = "A learner"
completed_first_task = True

print(f"Welcome, {learner_name}!")

if completed_first_task:
    print("Ready for the next challenge.")
else:
    print("Keep practicing the first task.")
```

With the values shown above, the output is:

```text
Welcome, A learner!
Ready for the next challenge.
```

Change the value of `learner_name` and try both values (`True` and `False`) for `completed_first_task`. Do not put your real contact details or another person's personal information into public examples.

## Guided activity 3: a small function

```python
def make_greeting(name):
    return f"Welcome, {name}!"

print(make_greeting("Python learner"))
```

Expected output:

```text
Welcome, Python learner!
```

Try changing the argument passed to `make_greeting`. Explain the difference between defining a function and calling it.

## Mini challenge

Create a program that stores a workshop topic and a number of practice tasks, then prints a friendly summary. Add a condition that prints a different message when the number of tasks is greater than zero.

For a starter exercise, run the [hello lab](labs/01-hello.py). The [mini challenge handout](labs/02-mini-challenge.md) includes a sample result and reflection questions.

**Stretch:** Put the summary logic inside a function and write a test for it.

## Troubleshooting

- **`python` command not found:** try `python3`, or use the facilitator's approved environment.
- **Unexpected indentation error:** check the spaces before lines inside `if`, `else`, and `def` blocks.
- **Text does not appear to change:** save the file and ensure you run the same file you edited.
- **Quotation or syntax error:** use matching quotes and parentheses.

## Exit ticket

1. In your own words, what is a variable?
2. What does a condition help a program decide?
3. What would you like to build next?

## Facilitator notes

Allow learners to pair up and explain their thinking. Emphasize experimentation and clear error messages rather than speed. Review all commands and environment setup before delivering this draft workshop.
