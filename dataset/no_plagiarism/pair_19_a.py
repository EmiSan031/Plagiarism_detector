def password_strength(password):
    score = 0
    score += any(char.islower() for char in password)
    score += any(char.isupper() for char in password)
    score += any(char.isdigit() for char in password)
    score += len(password) >= 8
    return score

print(password_strength("Code2026"))
