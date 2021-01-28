#!flask/bin/python
import requests
from flask import Flask, jsonify
from flask import request, redirect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

new_url = "http://nnrf-nfm:8080"

@app.route('/nnrf-disc/v1/nf-instances', methods=['GET'])
def nnrf_disc():
    target_nf_type = request.args.get('target-nf-type', type=str)
    requester_nf_type = request.args.get('requester-nf-type', type=str)
    limit = request.args.get('limit', default=50, type=int)
    return jsonify(requests.get(new_url +"/nnrf-nfm/v1/nf-instances?nfType=" + target_nf_type).json())

if __name__ == '__main__':
    app.run(debug=True)
