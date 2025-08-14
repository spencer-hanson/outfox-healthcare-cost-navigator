import csv
import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, Integer, Computed
from schema import Provider, Procedure
from sqlalchemy.orm import Session

USERNAME = "example"
PASSWORD = "example"


def get_column_indexes(column_header_list, example_header_list):
    """
    Given a list of columns, get the index into the example_header_list of where that column is
    Example:
    get_column_indexes(["a", "b", "c"], ["ab", "a", "d", "b", "c"]) would return [1, 3, 4] because "a" is index 1, etc..

    :param column_header_list: list of columns to look for
    :param example_header_list: list to search for indexes in
    :return: list of indexes
    """
    indexes = []
    for col in column_header_list:
        found = False
        for idx, example_col in enumerate(example_header_list):
            if example_col == col:
                found = True
                indexes.append(idx)
        if not found:
            raise Exception(f"Column '{col}' not found in example given! Given '{example_header_list}'")
    return indexes


def parse_data(entries, column_headers, indexes):
    """
    Parse the data from a list of the entries from the CSV file
    :param entries: rows from the csv file
    :param column_headers: column headers of the data we're interested in
    :param indexes: indexes into the entry row for the headers we're interested in
    :return: list of providers and list of procedures dictionaries following the schema

    """
    column_header_to_idx = {column_headers[i]: indexes[i] for i in range(len(indexes))}
    provider_id_idx = column_header_to_idx["provider_id"]
    providers = {}
    procedures = []

    for entry in entries:
        procedure = {}
        provider_id = entry[provider_id_idx]

        # Check if we have catalogued the provider id already
        if provider_id not in providers:
            providers[provider_id] = {}
            for column_name, column_index in column_header_to_idx.items():  # Get the information for the provider
                if column_name.startswith("provider"):
                    providers[provider_id][column_name] = entry[column_index]

        # Populate our procedures
        for column_name, column_index in column_header_to_idx.items():
            if not column_name.startswith("provider"):
                procedure[column_name] = entry[column_index]

        procedures.append(procedure)
    return providers, procedures


def populate_database(providers, procedures):
    """
    given a list of dictionaries of providers and procedures, insert them into the database
    see schema for the formatting of the dictionaries

    :param providers: provider info dict, such as name, city, etc
    :param procedures: procedure info dict, such as average_covered_charges, etc..
    :return: None
    """
    engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@127.0.0.1:5432/db", echo=True)
    with Session(engine) as session:
        entries = []
        # Parse out providers - TODO Check for duplicate / existing!

    pass


def main():
    assert len(sys.argv) > 1, "Must pass in filename as arg!"

    filename = sys.argv[1]
    print(f"Parsing file '{filename}' into POSTGRES DB")

    column_mapping = {
        "Rndrng_Prvdr_CCN": "provider_id",
        "Rndrng_Prvdr_Org_Name": "provider_name",
        "Rndrng_Prvdr_City": "provider_city",
        "Rndrng_Prvdr_State_Abrvtn": "provider_state",
        "Rndrng_Prvdr_Zip5": "provider_zipcode",
        "DRG_Desc": "ms_drg_definition",
        "Tot_Dschrgs": "total_discharges",
        "Avg_Submtd_Cvrd_Chrg": "average_covered_charges",
        "Avg_Tot_Pymt_Amt": "average_total_payments",
        "Avg_Mdcr_Pymt_Amt": "average_medicare_payments"
    }
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        lines = list(reader)
        headers = lines[0]
        indexes = get_column_indexes(list(column_mapping.keys()), headers)
        providers, procedures = parse_data(lines[1:], list(column_mapping.values()), indexes)
        populate_database(providers, procedures)

        tw = 2
    # engine = create_engine("postgresql+psycopg2://example:example@localhost:5432/db", echo=True)
    # metadata = MetaData()
    # vv = metadata.tables.keys()
    # tw = 2
    # pass


if __name__ == "__main__":
    main()
