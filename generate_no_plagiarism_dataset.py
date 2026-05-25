"""Generate a deterministic negative-class dataset for non-plagiarized pairs."""

from __future__ import annotations

from pathlib import Path


PROGRAMS = [
    """def count_vowels(text):
    total = 0
    for char in text.lower():
        if char in "aeiou":
            total += 1
    return total

print(count_vowels("programming"))
""",
    """def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

print(merge_intervals([(1, 3), (2, 5), (8, 9)]))
""",
    """def fahrenheit_to_celsius(values):
    converted = []
    for value in values:
        converted.append((value - 32) * 5 / 9)
    return converted

print(fahrenheit_to_celsius([32, 68, 104]))
""",
    """def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("Never odd or even"))
""",
    """def inventory_value(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

print(inventory_value([{"price": 10, "quantity": 3}, {"price": 4, "quantity": 2}]))
""",
    """def rolling_average(numbers, window):
    result = []
    for index in range(len(numbers) - window + 1):
        result.append(sum(numbers[index:index + window]) / window)
    return result

print(rolling_average([2, 4, 6, 8, 10], 3))
""",
    """def parse_csv_line(line):
    values = []
    current = ""
    for char in line:
        if char == ",":
            values.append(current.strip())
            current = ""
        else:
            current += char
    values.append(current.strip())
    return values

print(parse_csv_line("name, age, city"))
""",
    """def unique_words(text):
    words = text.lower().split()
    return sorted(set(words))

print(unique_words("data science data mining"))
""",
    """def compound_interest(principal, rate, years):
    balance = principal
    for _ in range(years):
        balance *= 1 + rate
    return round(balance, 2)

print(compound_interest(1000, 0.05, 3))
""",
    """def rotate_left(values, steps):
    if not values:
        return []
    steps %= len(values)
    return values[steps:] + values[:steps]

print(rotate_left([1, 2, 3, 4, 5], 2))
""",
    """def grade_summary(grades):
    passed = [grade for grade in grades if grade >= 70]
    failed = [grade for grade in grades if grade < 70]
    return {"passed": len(passed), "failed": len(failed)}

print(grade_summary([95, 60, 72, 40, 88]))
""",
    """def normalize_scores(scores):
    highest = max(scores)
    if highest == 0:
        return scores
    return [score / highest for score in scores]

print(normalize_scores([10, 20, 40]))
""",
    """def word_lengths(sentence):
    lengths = {}
    for word in sentence.split():
        lengths[word] = len(word)
    return lengths

print(word_lengths("machine learning project"))
""",
    """def find_duplicates(values):
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)

print(find_duplicates([1, 2, 2, 3, 4, 4]))
""",
    """def encode_rle(text):
    if not text:
        return []
    result = []
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            result.append((current, count))
            current = char
            count = 1
    result.append((current, count))
    return result

print(encode_rle("aaabbc"))
""",
    """def matrix_trace(matrix):
    total = 0
    for index in range(min(len(matrix), len(matrix[0]))):
        total += matrix[index][index]
    return total

print(matrix_trace([[1, 2], [3, 4]]))
""",
    """def shopping_discount(total, member):
    if total >= 100 and member:
        return total * 0.8
    if total >= 100:
        return total * 0.9
    return total

print(shopping_discount(120, True))
""",
    """def flatten_once(groups):
    result = []
    for group in groups:
        for item in group:
            result.append(item)
    return result

print(flatten_once([[1, 2], [3], [4, 5]]))
""",
    """def password_strength(password):
    score = 0
    score += any(char.islower() for char in password)
    score += any(char.isupper() for char in password)
    score += any(char.isdigit() for char in password)
    score += len(password) >= 8
    return score

print(password_strength("Code2026"))
""",
    """def format_phone(number):
    digits = "".join(char for char in number if char.isdigit())
    if len(digits) != 10:
        return digits
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

print(format_phone("5551234567"))
""",
    """def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]

print(transpose([[1, 2, 3], [4, 5, 6]]))
""",
    """def top_students(records, minimum):
    result = []
    for name, grade in records:
        if grade >= minimum:
            result.append(name)
    return result

print(top_students([("Ana", 90), ("Luis", 65)], 80))
""",
    """def safe_divide(values, divisor):
    if divisor == 0:
        return []
    return [value / divisor for value in values]

print(safe_divide([10, 20, 30], 5))
""",
    """def count_extensions(files):
    counts = {}
    for filename in files:
        extension = filename.split(".")[-1]
        counts[extension] = counts.get(extension, 0) + 1
    return counts

print(count_extensions(["a.py", "b.txt", "c.py"]))
""",
    """def tax_bracket(income):
    if income < 10000:
        return "low"
    if income < 50000:
        return "middle"
    return "high"

print(tax_bracket(42000))
""",
    """def remove_outliers(values, limit):
    average = sum(values) / len(values)
    return [value for value in values if abs(value - average) <= limit]

print(remove_outliers([10, 11, 12, 100], 20))
""",
    """def schedule_conflict(first, second):
    first_start, first_end = first
    second_start, second_end = second
    return first_start < second_end and second_start < first_end

print(schedule_conflict((9, 11), (10, 12)))
""",
    """def title_case(text):
    words = []
    for word in text.split():
        words.append(word[:1].upper() + word[1:].lower())
    return " ".join(words)

print(title_case("hello WORLD"))
""",
    """def closest_value(values, target):
    best = values[0]
    for value in values[1:]:
        if abs(value - target) < abs(best - target):
            best = value
    return best

print(closest_value([2, 8, 13, 21], 10))
""",
    """def split_even_odd(values):
    even = []
    odd = []
    for value in values:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    return even, odd

print(split_even_odd([1, 2, 3, 4, 5]))
""",
    """def moving_total(values):
    total = 0
    result = []
    for value in values:
        total += value
        result.append(total)
    return result

print(moving_total([3, 1, 4]))
""",
    """def acronym(phrase):
    letters = []
    for word in phrase.split():
        if word:
            letters.append(word[0].upper())
    return "".join(letters)

print(acronym("object oriented programming"))
""",
    """def clamp_values(values, low, high):
    result = []
    for value in values:
        result.append(max(low, min(high, value)))
    return result

print(clamp_values([-2, 4, 12], 0, 10))
""",
    """def group_by_length(words):
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups

print(group_by_length(["ai", "code", "data"]))
""",
    """def make_histogram(values):
    histogram = {}
    for value in values:
        histogram[value] = histogram.get(value, 0) + 1
    return histogram

print(make_histogram(["red", "blue", "red"]))
""",
    """def apply_bonus(salaries, percent):
    updated = {}
    for name, salary in salaries.items():
        updated[name] = salary * (1 + percent)
    return updated

print(apply_bonus({"Ana": 100, "Luis": 80}, 0.1))
""",
    """def diagonal_difference(matrix):
    left = 0
    right = 0
    size = len(matrix)
    for index in range(size):
        left += matrix[index][index]
        right += matrix[index][size - index - 1]
    return abs(left - right)

print(diagonal_difference([[1, 2], [3, 4]]))
""",
    """def filter_prefix(words, prefix):
    result = []
    for word in words:
        if word.startswith(prefix):
            result.append(word)
    return result

print(filter_prefix(["car", "cat", "dog"], "ca"))
""",
    """def cart_total(items):
    subtotal = sum(price for price, quantity in items for _ in range(quantity))
    shipping = 0 if subtotal > 50 else 5
    return subtotal + shipping

print(cart_total([(10, 2), (15, 1)]))
""",
    """def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))

print(reverse_words("one two three"))
""",
]


def main() -> None:
    output_dir = Path("dataset/no_plagiarism")
    output_dir.mkdir(parents=True, exist_ok=True)

    for index in range(30):
        first = PROGRAMS[index]
        second = PROGRAMS[index + 10]
        pair_number = f"{index + 1:02d}"
        (output_dir / f"pair_{pair_number}_a.py").write_text(first, encoding="utf-8")
        (output_dir / f"pair_{pair_number}_b.py").write_text(second, encoding="utf-8")

    print(f"Generated 30 non-plagiarism pairs in {output_dir}")


if __name__ == "__main__":
    main()
