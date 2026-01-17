import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

@st.cache_resource
def get_engine():
    db = st.secrets["postgres"]
    url = (
        f"postgresql+psycopg2://{db['user']}:{db['password']}"
        f"@{db['host']}:{db['port']}/{db['database']}"
    )
    return create_engine(url)

def run_query(query):
    engine = get_engine()
    return pd.read_sql(query, engine)
