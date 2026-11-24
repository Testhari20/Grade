def average(scores):
    """Return the average of the scores rounded to 2 places (0 when there are none)."""
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)


def letter_grade(score):
    """Map a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def passed(scores, pass_mark=60):
    """True when the average reaches the pass mark."""
    return average(scores) >= pass_mark
