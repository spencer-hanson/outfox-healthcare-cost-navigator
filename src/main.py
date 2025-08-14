from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from schema import Provider, Procedure

app = FastAPI()

USERNAME = "example"  # TODO Put in config file?
PASSWORD = "example"


@app.get("/providers/{zip_code}")
def query_providers(zip_code: str):
    """
    Endpoint for querying providers from within a specific zipcode
    :return: json list
    """
    engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@postgres:5432/db", echo=True)
    with Session(engine) as session:
        statement = select(Provider).where(Provider.provider_zipcode == zip_code)
        results = []
        for result in session.scalars(statement):
            results.append(result.to_json())

    return results


@app.get("/ask")
def ask(query: str):
    # TODO submit API call to OpenAI with the query string
    context = f"""Answer the following question if it pertains to medical bills, hospital quality or hospital location
    \"{str}\"
    """
    return "OpenAI TODO!"
