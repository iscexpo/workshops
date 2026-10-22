"""Small, safe starter example for ISC Expo Workshops."""


def make_greeting(name: str) -> str:
    """Return a friendly greeting for the given display name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "learner"
    return f"Hello, {cleaned_name}! Welcome to ISC Expo Workshops."


def main() -> None:
    print(make_greeting("Python learner"))


if __name__ == "__main__":
    main()
