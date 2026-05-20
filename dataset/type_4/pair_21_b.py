def valid_emails(emails):
    return [email for email in emails if "@" in email and "." in email.rsplit("@", 1)[-1]]

def count_domains(emails):
    return {
        domain: sum(1 for email in emails if email.rsplit("@", 1)[-1].lower() == domain)
        for domain in {email.rsplit("@", 1)[-1].lower() for email in emails}
    }

def email_report(emails):
    valid = valid_emails(emails)
    domains = count_domains(valid)
    print("Total emails:", len(emails))
    print("Valid emails:", len(valid))
    print("Domains:", domains)
    return domains

sample = ["ana@mail.com", "bad-email", "leo@school.edu", "max@mail.com"]
email_report(sample)

def sorted_domain_counts(domains):
    return sorted(domains.items())

summary = count_domains(valid_emails(sample))
print(sorted_domain_counts(summary))

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
