from sqlalchemy import String, Integer, Numeric, ForeignKey, create_engine
from schema import Base

"""
This script is run to generate the basic schema of the database, it only needs to be run once
"""


def main():
    print("Connecting to database..")
    engine = create_engine("postgresql+psycopg2://example:example@127.0.0.1:5432/db", echo=True)
    print("Creating Schema..")
    Base.metadata.create_all(engine)
    print("Done!")


if __name__ == "__main__":
    main()


"""

 provider_id, provider_name, provider_city/state/zip_code,ms_drg_definition, total_discharges, average_covered_charges, average_total_payments, average_medicare_payments
<generate>, Rndrng_Prvdr_Org_Name, Rndrng_Prvdr_City, Rndrng_Prvdr_State_Abrvtn, Rndrng_Prvdr_Zip5, DRG_Desc,Tot_Dschrgs, Avg_Submtd_Cvrd_Chrg, Avg_Tot_Pymt_Amt, Avg_Mdcr_Pymt_Amt

Rndrng_Prvdr_CCN,Rndrng_Prvdr_Org_Name           ,Rndrng_Prvdr_City,Rndrng_Prvdr_St       ,Rndrng_Prvdr_State_FIPS,Rndrng_Prvdr_Zip5,Rndrng_Prvdr_State_Abrvtn,Rndrng_Prvdr_RUCA,Rndrng_Prvdr_RUCA_Desc,                                                               DRG_Cd,DRG_Desc,                                                                                Tot_Dschrgs,Avg_Submtd_Cvrd_Chrg,Avg_Tot_Pymt_Amt,Avg_Mdcr_Pymt_Amt
010001,          Southeast Health Medical Center,Dothan,            1108 Ross Clark Circle,01                     ,36301            ,AL                       ,1                , "Metropolitan area core: primary flow within an urbanized area of 50,000 and greater",023   ,CRANIOTOMY WITH MAJOR DEVICE IMPLANT OR ACUTE COMPLEX CNS PRINCIPAL DIAGNOSIS WITH MCC O,           25,                  158541.64,        37331,  35332.96
"""