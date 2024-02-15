def gather_credits(credits_needed: int, *course_data):
    courses_enrolled = []
    credits_achieved = 0
    result = ""

    for course_name, course_credits in course_data:
        if credits_achieved >= credits_needed:
            break
        if course_name in courses_enrolled:
            continue
        courses_enrolled.append(course_name)
        credits_achieved += course_credits

    if credits_achieved >= credits_needed:
        result += f"Enrollment finished! Maximum credits: {credits_achieved}.\nCourses: {', '.join(sorted(courses_enrolled))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {credits_needed - credits_achieved} credits more."

    return result


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

