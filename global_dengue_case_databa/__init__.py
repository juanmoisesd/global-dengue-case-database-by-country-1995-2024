"""Database of confirmed and reported dengue cases in 31 countries across Latin Ame
DOI:https://juanmoisesd.github.io/global-dengue-case-database-by-country-1995-2024/"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://juanmoisesd.github.io/global-dengue-case-database-by-country-1995-2024/".split(".")[-1];m=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  t=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(t["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Database of confirmed and reported dengue cases in 31 countr. Zenodo. https://juanmoisesd.github.io/global-dengue-case-database-by-country-1995-2024/"