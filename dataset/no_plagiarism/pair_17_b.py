def schedule_conflict(first, second):
    first_start, first_end = first
    second_start, second_end = second
    return first_start < second_end and second_start < first_end

print(schedule_conflict((9, 11), (10, 12)))
