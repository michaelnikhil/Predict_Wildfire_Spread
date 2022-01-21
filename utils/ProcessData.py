
def convert_decimal_latitude_longitude(df):
    # Converting Lat/Long DMS to Decimal
    pattern = r'(?P<d>[\d\.]+).*?(?P<m>[\d\.]+).*?(?P<s>[\d\.]+)'

    spatial_directions = ['latitude', 'longitude']

    for direction in spatial_directions:
        dms = df[direction].str.extract(pattern).astype(float)
        df[direction] = dms['d'] + dms['m'].div(60) + dms['s'].div(3600)
        if direction == 'longitude':
            df[direction] *= -1
