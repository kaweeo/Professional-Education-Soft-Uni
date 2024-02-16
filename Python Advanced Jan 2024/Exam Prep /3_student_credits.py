def students_credits(*course_data):
    student_stats_dict = {}
    total_student_credits_count = 0
    result = ""

    for course in course_data:
        course_name, course_credits, max_test_points, student_points = course.split("-")
        student_course_credits = (int(student_points) / int(max_test_points)) * int(course_credits)
        if not course_name in student_stats_dict.keys():
            student_stats_dict[course_name] = 0
        student_stats_dict[course_name] += student_course_credits
        total_student_credits_count += student_course_credits

    if total_student_credits_count >= 240:
        result += f"Diyan gets a diploma with {total_student_credits_count:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_student_credits_count:.1f} credits more for a diploma.\n"

    sorted_student_stats_dict = dict(sorted(student_stats_dict.items(), key=lambda kvp: -kvp[1]))
    for k, v in sorted_student_stats_dict.items():
        result += f"{k} - {v:.1f}\n"

    return result

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
