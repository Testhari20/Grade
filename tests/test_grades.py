from src.grades import average, letter_grade, passed


def test_average_of_scores():
    assert average([80, 90, 100]) == 90


def test_average_of_nothing_is_zero():
    assert average([]) == 0


def test_letter_grades():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(40) == "F"


def test_grade_boundaries():
    assert letter_grade(90) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(60) == "D"


def test_passed():
    assert passed([70, 80]) is True
    assert passed([50, 60]) is False
