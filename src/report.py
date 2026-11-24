from src.grades import average, letter_grade


def summary(name, scores):
    """One-line report for a student."""
    avg = average(scores)
    return f"{name}: {avg} ({letter_grade(avg)})"
