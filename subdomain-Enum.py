import requests
import json
import csv
import os
from datetime import datetime

print("\nSubdomain Enumeration Script\n")

def get_sub_domains(domain, json_filename, csv_filename):
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
    querystring = {"children_only":"true"}
    headers = {
        'accept': "application/json",
        'apikey': "APIKEY"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

    # Save the JSON response to a file
    with open(json_filename, mode='w') as file:
        json.dump(data, file, indent=4)

    subdomains = data.get("subdomains", [])
    subdomain_list = [[subdomain] for subdomain in subdomains]

    # Save subdomains to a CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subdomain"])
        writer.writerows(subdomain_list)

    return subdomains

domain = input("\nEnter Domain name: ")
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
json_filename = f"{domain}_data.json"
csv_filename = f"{domain}_subdomains.csv"
subdomains = get_sub_domains(domain, json_filename, csv_filename)

print(f"\n{len(subdomains)} subdomains found and saved in '{csv_filename}' and JSON response saved in '{json_filename}' file.")
