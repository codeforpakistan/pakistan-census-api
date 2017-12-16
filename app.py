from flask import Flask
from flask import request
from flask_restful import Api
from flask_restful import Resource
from json import dumps
from pymongo import MongoClient
import pandas as pd
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class Provinces(Resource):
  def get(self):
    provinces_df = pd.read_excel("DISTRICT_WISE_CENSUS_RESULTS_CENSUS_2017.xlsx","Province_Wise")
    print provinces_df

    return provinces_df.to_dict(orient='records')


class Cities(Resource):
  def get(self):
    cities_df = pd.read_excel("DISTRICT_WISE_CENSUS_RESULTS_CENSUS_2017.xlsx","City_Wise")

    return cities_df.to_dict(orient='records')

class Districts(Resource):
  def get(self):
    district_df = pd.read_excel('DISTRICT_WISE_CENSUS_RESULTS_CENSUS_2017.xlsx', 'Districts')

    return district_df.to_dict(orient='records')



api.add_resource(Provinces, '/provinces') # Route_1
api.add_resource(Cities, '/cities') # Route_2
api.add_resource(Districts, '/districts') # Route_2



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5002))
  app.run(host='0.0.0.0',port=5002,debug=True)