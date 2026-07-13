import logging 
import time
import os
import pandas as pd

from fredapi import Fred

fred = Fred(api_key="73762aac2424ef546f1add23dfb399d3")
df=pd.read_csv("transactions.csv")



def ingest_paysim():
    df=pd.read_csv("transactions.csv")
    
    try:
       

        df = df.rename(columns={
            "nameOrig": "name_orig",
            "oldbalanceOrg": "old_balance_org",
            "newbalanceOrig": "new_balance_orig",
            "nameDest": "name_dest",
            "oldbalanceDest": "old_balance_dest",
            "newbalanceDest": "new_balance_dest",
            "isFraud": "is_fraud",
            "isFlaggedFraud": "is_flagged_fraud"
        })

        print(df.dtypes)

        logging(f"Rows: {len(df)}")

        df.to_parquet("transactions.parquet", index=False)

      

    except Exception as e:
        print(e)



def ingest_fred():
  df=pd.read_csv("transactions.csv")
  try:
    os.makedirs("data/raw/macro", exist_ok=True)
    series_ids= ["CPIAUCSL", "UNRATE", "DEXUSEU"]
    for i in series_ids:
      data=fred.get_series(i)   
      df=data.reset_index()
      df.columns=["date","value"]
      df.to_csv(f"data/raw/macro/{i}.csv")
      print(f"{i}.csv saved")
  except Exception as e:
    logging(e)


def ingest_complaints():
  os.makedirs("data/processed", exist_ok=True)
  url="https://files.consumerfinance.gov/ccdb/complaints.csv.zip"
  #file="complaints.csv.zip"
  df=pd.read_csv(url)
  print(df.head())
  df=df[df["product"].isin(["Credit card","Cheking or savings account"])]
  df.to_parquet("data/processed/complaints.parquet",index=False)
  print("complaints.parquet saved")

def run_sequential():
  start=time.perf_counter()
  ingest_paysim()
  ingest_fred()
  #ingest_complaints()
  end=end = time.perf_counter()
  print(end-start)
  
#ingest_fred()
#ingest_paysim()
ingest_complaints()
#run_sequential()

    
  

   




   

