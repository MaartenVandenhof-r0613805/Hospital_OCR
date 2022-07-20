import pandas as pd
from random import randrange, choice, randint
from datetime import timedelta, datetime
import names
from faker import Faker

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def random_d_name():
    fake = Faker(['nl_NL', 'fr_FR'])
    name = fake.name().split(" ")
    return " ".join(name[1:]) + ", " + name[0]

d1 = datetime.strptime('1/1/1930 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')


def generate_data():
    fake = Faker(['nl_NL', 'fr_FR'])
    p_name = fake.name()
    p_date = random_date(d1, d2)

    row_1 = " ".join([p_name, str(p_date)])

    fake = Faker('nl_BE')
    address = fake.address()

    sex = choice(["M", "F"])
    birhtday = random_date(d1, d2)

    row_2 = " ".join([sex, str(birhtday)])
    
    rand_text_1 = fake.text()[:25]
    rand_text_2 = fake.text()[:25]

    d1_name = random_d_name()
    d2_name = random_d_name()

    row_3 = " ".join([str(randint(1, 9999)), d1_name, str(randint(1, 999))])
    row_4 = " ".join([str(randint(1, 9999)), d2_name, str(randint(1, 9)), "print", str(p_date)])

    return "\n".join([row_1, address, row_2, rand_text_1, rand_text_2, row_3, row_4])

text = []
for i in range(0, 20):
    text.append(generate_data())

# data = pd.DataFrame(text)
# data.to_csv("F:\Projects\Hospital_OCR\generated_data.csv")

print("\n\n".join(text))