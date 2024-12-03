import singer 
import pandas as pd
import math

def clean_float_for_json(value):
    if isinstance(value, float):
        if math.isinf(value) or math.isnan(value):
            return None
    elif isinstance(value, dict):
        return {k: clean_float_for_json(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [clean_float_for_json(v) for v in value]
    return value

def fetchData():
    """
    Fetches data from the SpaceX API
    """
    
    LOGGER = singer.get_logger()
    
    schema = {
    'type': 'object',
    'properties': {
        'id': {'type': ['string']},
        'name': {'type': ['string']},
        'date_utc': {'type': ['string'], 'format': 'date-time'},
        'flight_number': {'type': ['string']},
        'success': {'type': ['boolean']},
        'details': {'type': ['string', 'null']},
        'rocket': {'type': ['string']}
    },
    'required': ['id', 'name', 'date_utc']
}

    url = "https://api.spacexdata.com/v5/launches"

    df = pd.read_json(url)

    records = df.to_dict(orient='records')

    # Clean each record 
    cleaned_records = [clean_float_for_json(record) for record in records]

    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', cleaned_records)


if __name__ == '__main__':
    fetchData()