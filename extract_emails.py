import re

emails = input()

email_regex = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

found_emails = re.findall(email_regex, emails)

for email in found_emails:
    print(email[0])
