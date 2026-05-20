def count_domains(emails):
    domains = {}
    for email in emails:
        parts = email.split("@")
        if len(parts) == 2:
            domain = parts[1].lower()
            if domain not in domains:
                domains[domain] = 0
            domains[domain] += 1
    return domains

def valid_emails(emails):
    result = []
    for email in emails:
        if "@" in email and "." in email.split("@")[-1]:
            result.append(email)
    return result

def email_report(emails):
    valid = valid_emails(emails)
    domains = count_domains(valid)
    print(f"Total emails: {len(emails)}")
    print(f"Valid emails: {len(valid)}")
    print(f"Domains: {domains}")
    return domains

sample = ["ana@mail.com", "bad-email", "leo@school.edu", "max@mail.com"]
email_report(sample)

def sorted_domain_counts(domains):
    rows = []
    for domain in sorted(domains):
        rows.append((domain, domains[domain]))
    return rows

summary = count_domains(valid_emails(sample)) if 'sample' in globals() else {}
print(sorted_domain_counts(summary))
