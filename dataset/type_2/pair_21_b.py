def tally_hosts(addresses):
    hosts = {}
    for address in addresses:
        pieces = address.split("@")
        if len(pieces) == 2:
            host = pieces[1].lower()
            if host not in hosts:
                hosts[host] = 0
            hosts[host] += 1
    return hosts

def clean_addresses(addresses):
    kept = []
    for address in addresses:
        if "@" in address and "." in address.split("@")[-1]:
            kept.append(address)
    return kept

def address_report(addresses):
    kept = clean_addresses(addresses)
    hosts = tally_hosts(kept)
    print(f"Entries checked: {len(addresses)}")
    print(f"Accepted entries: {len(kept)}")
    print(f"Host counts: {hosts}")
    return hosts

records = ["ivy@work.net", "wrong", "sam@site.org", "tom@work.net"]
address_report(records)

def sorted_domain_counts(domains):
    rows = []
    for domain in sorted(domains):
        rows.append((domain, domains[domain]))
    return rows

summary = count_domains(valid_emails(sample)) if 'sample' in globals() else {}
print(sorted_domain_counts(summary))
