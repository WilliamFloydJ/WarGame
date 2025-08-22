import random

first_names = [
    "James", "Michael", "William", "David", "John",
    "Robert", "Thomas", "Charles", "Christopher", "Daniel",
    "Matthew", "Andrew", "Joseph", "Mark", "Paul",
    "Steven", "Richard", "Edward", "George", "Benjamin",
    "Samuel", "Stephen", "Timothy", "Jonathan", "Brian",
    "Nicholas", "Anthony", "Eric", "Adam", "Jeffrey",
    "Ryan", "Jacob", "Gary", "Kenneth", "Joshua",
    "Jason", "Frank", "Nathan", "Justin", "Scott",
    "Brandon", "Patrick", "Dennis", "Gregory", "Aaron",
    "Peter", "Philip", "Ronald", "Donald", "Douglas"
]
last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown",
    "Davis", "Clark", "Lewis", "Walker", "Hall",
    "Allen", "Young", "Hernandez", "King", "Wright",
    "Lopez", "Hill", "Scott", "Green", "Adams",
    "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell",
    "Perez", "Roberts", "Turner", "Phillips", "Campbell",
    "Parker", "Evans", "Edwards", "Collins", "Stewart",
    "Sanchez", "Morris", "Rogers", "Reed", "Cook",
    "Morgan", "Bell", "Murphy", "Bailey", "Rivera",
    "Cooper", "Richardson", "Cox", "Howard", "Ward"
]

def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)

    full = f"{first} {last}"
    return full