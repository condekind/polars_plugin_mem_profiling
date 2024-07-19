import csv
import random
import string
from urllib.parse import urlunparse
import sys

# Possible values for the "extract" field
extract_values = [
    "scheme",
    "username",
    "password",
    "host",
    "port",
    "path",
    "query",
    "fragment",
]


# Function to generate a random string of given length
def random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Function to generate a random URL
def generate_random_url():
    scheme = random.choice(["http", "https", "ftp"])
    username = random_string(5) if random.random() < 0.5 else ""
    password = random_string(5) if username and random.random() < 0.5 else ""
    host = random_string(10) + random.choice([".com", ".net", ".io"])
    #port = str(random.randint(1024, 65535)) if random.random() < 0.5 else ""
    path = "/" + random_string(10) if random.random() < 0.5 else ""
    query = "q=" + random_string(5) if random.random() < 0.5 else ""
    fragment = random_string(5) if random.random() < 0.5 else ""

    return urlunparse(
        (
            scheme,
            f"{username}:{password}@{host}" if username and password else host,
            path,
            "",
            query,
            fragment,
        )
    )


num_rows = 100
if len(sys.argv) > 1:
    num_rows = int(sys.argv[1])

# Open a new CSV file to write
with open(f"urls_{num_rows:_}.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["URLs", "extract"])

    # Generate and write 1 million rows
    cnt0, cnt1 = 0, 0
    for _ in range(num_rows):
        cnt0 += 1
        if cnt0 == 100000:
            cnt0 = 0
            cnt1 += 1
            print(f"{cnt1*100000/num_rows*100:04}%")
        url = generate_random_url()
        extract = random.choice(extract_values)
        writer.writerow([url, f"{extract}"])

print("CSV file generated successfully.")
