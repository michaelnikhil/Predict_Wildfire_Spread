from utils.counties import Counties
from utils.config import globalvariables as g


counties = Counties.import_data(g.counties_source_url)
https://www.drought.gov/states/oregon/county/clatsop#
print(counties)