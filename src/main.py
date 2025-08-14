from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/providers/{zip_code}")
def query_providers():
    """
    Endpoint for querying providers from within a specific zipcode
    :return: json list
    """

    return {"Hello": "World"}

