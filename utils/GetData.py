from utils.ImportRawDataFactory import importer
from utils.Configuration import globalvariables as _
import pandas as pd

class Counties(importer):
    def import_data(self):
        url = _.counties_source_url
        df = pd.read_csv(url,sep=',')
        return list(df['Name'])

class Wildfire(importer):
    def import_data(self,db_connection):
        return pd.read_sql('select * from wildfire_data', con=db_connection)

class Noaa(importer):
    def import_data(self,db_connection):
        return pd.read_sql('select * from noaa_data', con=db_connection)