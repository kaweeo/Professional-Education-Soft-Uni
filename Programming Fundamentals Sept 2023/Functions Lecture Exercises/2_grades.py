
def grade_converter(grade: float) -> str:
    if grade >= 2.00 and grade < 3.00:
        return "Fail"
    if grade >= 3.00 and grade < 3.5:
        return "Poor"
    if grade >= 3.5 and grade < 4.5:
        return "Good"
    if grade >= 4.5 and grade < 5.5:
        return "Very Good"
    if grade >= 5.5 and grade <= 6:
        return "Excellent"

grade_input = float(input())
print(grade_converter(grade_input))
