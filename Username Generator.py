import requests
import random

db = requests.get("https://www.muguguestbook.com/mugu.txt").text
usernames = []
blacklisted = ["mugu", "mail", "spam", "outlook", "gmail", "yandex", "bait",
               "taylor", "jason", "jackson", "albert", "robot", "oscar",
               "olivia", "johnny", "hannah", "chatty", "john", "dick",
               "andrew", "billy", "victor", "nik","nig", "antonio", "ronald",
               "george", "biden", "bill", "michael", "schmidt", "admin", "support",
               "test", "example", "reply", "service", "contact", "info", "username",
               "hacker", "mod", "wolfgang", "rebecca", "joe", "catcher", "walker",
               "dave", "user", "james", "albert", "sean", "hello", "ladmail", "smith", "trash"]

def extract_parts(input_string):
    part_after_split = input_string.split('<')[-1]
    local_part = part_after_split.split('@')[0]
    return local_part.replace('.', '_').strip()

for line in db.splitlines():
    if not any(blacklist_word in line for blacklist_word in blacklisted):
        usernames.append(extract_parts(line))

random.shuffle(usernames)

print(usernames)
