from utils.datafactory import worker
from utils.config import globalvariables as g
import pandas as pd

class Counties(worker):
    def __init__(self):
        pass

    def import_data(self):
        url = g.counties_source_url
        df = pd.read_csv(url,sep=',')
        return list(df['Name'])

