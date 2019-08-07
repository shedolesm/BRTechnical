import json
from collections import Counter
import operator
import re


def get_me_logo(fcompanyName):
    upper_company_name = re.sub(r"[^A-Za-z]", "", fcompanyName.upper())
    char_counts = dict(Counter(upper_company_name))
    sorted_char_counts_alphabetically = dict(sorted(char_counts.items(), key=operator.itemgetter(0)))
    most_frequent_sorted_alphabetically = sorted(sorted_char_counts_alphabetically.items(), key=operator.itemgetter(1), reverse=True)
    if len(most_frequent_sorted_alphabetically) >= 3:
        logo = most_frequent_sorted_alphabetically[0][0] + "," + most_frequent_sorted_alphabetically[1][0] + "," + most_frequent_sorted_alphabetically[2][0]
    elif len(most_frequent_sorted_alphabetically) == 2:
        logo = most_frequent_sorted_alphabetically[0][0] + "," + most_frequent_sorted_alphabetically[1][0]
    else:
        logo = most_frequent_sorted_alphabetically[0][0]
    return logo.rstrip(" ")


with open("CompaniesList.json", "r", encoding="utf8") as write_file:
    data = json.load(write_file)


for company in data:
    if 'Company Name' in company.keys():
        company["logoCharacters"] = get_me_logo(company['Company Name'])

with open("UpdatedCompaniesList.json", "w") as write_file:
    json.dump(data, write_file)
