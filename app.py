"""
Author      : Suraj Nanavare
Created At  : 26 June 2019
Description : This is sample flask application with sample API 
              to get current date and time.
Dependancies: Data file "data/sample_data.json" which contain book details.
"""

from flask import Flask, request, jsonify
import json
import os


app = Flask(__name__)
app.config["DEBUG"] = True

data_source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/sample_data.json")

def read_json_data(data_source):
    fp = open(data_source,'r')
    data = json.loads(fp.read())
    print(data)
    return data

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({ "status": "404","data" : "Page Not Found!" })

@app.route('/api/v1/resources/companies/all', methods=['GET'])
def get_company_details():
    company_details = read_json_data(data_source)
    result = {
        "status" : "200",
        "data" : company_details
    }
    return jsonify(result)

@app.route('/api/v1/resources/companies', methods=['GET'])
def api_id():
    """
        Check if an ID was provided as part of the URL.
        If ID is provided, assign it to a variable.
        If no ID is provided, display an error in the browser.
    """
    print(request.args)
    #comp_id = request.args

    #a = werkzeug.datastructures.ImmutableMultiDict((('a', 1), ('b', 2)))
    #for id in comp_id:

    if 'CompanyId' in request.args:
        id = str(request.args['CompanyId'])
    else:
        return jsonify({ "status": "200","data" : "Please specify Company ID!" })

    match_found = []

    company_details = read_json_data(data_source)
    for company_name in company_details['companies']:
        if company_name['CompanyId'] == id:
            match_found.append(company_name)

    if not match_found:
        result = {
            "status" : "200",
            "data" : "No Company found!"
        }
    else:
        result = { 
            "status" : "200",
            "data" : match_found
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
