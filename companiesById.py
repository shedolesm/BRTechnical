import json
from collections import Counter
import operator
import re


def find_me_company(fdata, fcompanyId):
    for company in fdata:
        if company["CompanyId"] == fcompanyId.upper():
            return company


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

companyId = input("Enter Company Id: ")
company = find_me_company(data, companyId)

companyName = company['Company Name']
logo = get_me_logo(companyName)

company["logoCharacters"] = logo
print(company)

