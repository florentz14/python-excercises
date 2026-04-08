import re


email_regex = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", flags=re.IGNORECASE)
sample = "Contact us at data.team@example.com or admin@company.org"
emails = email_regex.findall(sample)

print("Regex email matches:")
print(emails)
