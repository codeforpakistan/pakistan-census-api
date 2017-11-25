from flask import Flask
from flask import request
from flask_restful import Api
from flask_restful import Resource
from json import dumps
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Provinces(Resource):
    def get(self):
        uri = "mongodb://pakistancensus:CwTZjX2WgUICeQbc7zUPBCiP9JlDe7AfD9Qe6u9XYeW4jLKdMOXuF5qzrNYATiMKkCylsigwnNY4lAlN9e9eBA==@pakistancensus.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
        client = MongoClient(uri)

        db = client['pakistancensus']

        eqn_df = pd.DataFrame(list(db.provinces.find()))
        print eqn_df

        return eqn_df.to_json(orient='records')




api.add_resource(Provinces, '/provinces') # Route_1


if __name__ == '__main__':
     app.run(port=5002,debug=True)