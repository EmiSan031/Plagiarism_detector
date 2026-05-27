def total_workouts(sets):
    total = 0
    for item in sets:
        total += item["reps"]
    return total

def average_workouts(sets):
    if not sets:
        return 0
    return total_workouts(sets) / len(sets)

def count_high_workouts(sets, minimum):
    count = 0
    for item in sets:
        if item["reps"] >= minimum:
            count += 1
    return count

def workout_report(sets, minimum):
    total = total_workouts(sets)
    average = average_workouts(sets)
    high_count = count_high_workouts(sets, minimum)
    print(f"Total reps: {total}")
    print(f"Average reps: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_workouts = [{"move": "push", "reps": 20}, {"move": "squat", "reps": 30}, {"move": "row", "reps": 18}]
workout_report(records_workouts, 10)
