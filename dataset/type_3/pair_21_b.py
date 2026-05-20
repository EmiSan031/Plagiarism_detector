def count_domains(emails):
    domains = {}
    skipped = 0
    for email in emails:
        parts = email.strip().split("@")
        if len(parts) == 2 and parts[0]:
            domain = parts[1].lower()
            if domain not in domains:
                domains[domain] = 0
            domains[domain] += 1
        else:
            skipped += 1
    print(f"Skipped emails: {skipped}")
    return domains

def valid_emails(emails):
    result = []
    for email in emails:
        clean = email.strip()
        if "@" in clean and "." in clean.split("@")[-1]:
            result.append(clean)
    return result

def email_report(emails):
    valid = valid_emails(emails)
    domains = count_domains(valid)
    print(f"Checked emails: {len(emails)}")
    print(f"Valid emails: {len(valid)}")
    print(f"Domains: {domains}")
    return domains

sample = [" ana@mail.com ", "bad-email", "leo@school.edu", "max@mail.com"]
email_report(sample)
