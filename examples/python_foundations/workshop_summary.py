"""Build a simple workshop summary using variables, conditions, and a function."""


def build_summary(topic: str, activity_count: int) -> str:
    """Return a summary for a topic with a non-negative activity count."""
    cleaned_topic = topic.strip()
    if not cleaned_topic:
        raise ValueError("topic must not be empty")
    if activity_count < 0:
        raise ValueError("activity_count must not be negative")

    if activity_count > 0:
        next_step = "Let's begin with the first activity!"
    else:
        next_step = "The activities still need to be prepared."

    return (
        f"Workshop: {cleaned_topic}\n"
        f"Activities planned: {activity_count}\n"
        f"{next_step}"
    )


def main() -> None:
    """Run the example with sample workshop data."""
    print(build_summary("Python Foundations", 3))


if __name__ == "__main__":
    main()
