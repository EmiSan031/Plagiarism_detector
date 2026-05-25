def grade_summary(grades):
    passed = [grade for grade in grades if grade >= 70]
    failed = [grade for grade in grades if grade < 70]
    return {"passed": len(passed), "failed": len(failed)}

print(grade_summary([95, 60, 72, 40, 88]))
