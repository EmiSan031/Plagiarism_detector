def reads_same(phrase):
    normalized = phrase.lower().replace(" ", "")
    return normalized == normalized[::-1]

def strip_non_alpha(phrase):
    filtered = ""
    for ch in phrase:
        if ch.isalpha() or ch == " ":
            filtered += ch
    return filtered

def symmetry_report(phrase):
    normalized = phrase.lower().replace(" ", "")
    sanitized = strip_non_alpha(phrase).lower().replace(" ", "")
    symmetry_check = reads_same(phrase)
    print(f"Input phrase    : '{phrase}'")
    print(f"Normalized form : '{normalized}'")
    print(f"Normalized length: {len(normalized)}")
    print(f"Reads same way  : {symmetry_check}")
    if symmetry_check:
        print(f"  -> '{phrase}' is symmetric!")
    else:
        print(f"  -> '{phrase}' is NOT symmetric.")
    print(f"Opening char    : '{normalized[0] if normalized else 'N/A'}'")
    print(f"Closing char    : '{normalized[-1] if normalized else 'N/A'}'")

sample_phrases = ["oso", "mundo", "kayak", "codigo"]
for sample in sample_phrases:
    symmetry_report(sample)
    print()
