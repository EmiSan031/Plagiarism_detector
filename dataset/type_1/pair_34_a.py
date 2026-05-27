def total_patients(patients):
    total = 0
    for item in patients:
        total += item["age"]
    return total

def average_patients(patients):
    if not patients:
        return 0
    return total_patients(patients) / len(patients)

def count_high_patients(patients, minimum):
    count = 0
    for item in patients:
        if item["age"] >= minimum:
            count += 1
    return count

def patient_report(patients, minimum):
    total = total_patients(patients)
    average = average_patients(patients)
    high_count = count_high_patients(patients, minimum)
    print(f"Total age: {total}")
    print(f"Average age: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_patients = [{"name": "Iris", "age": 34}, {"name": "Noe", "age": 52}, {"name": "Leo", "age": 29}]
patient_report(records_patients, 10)
