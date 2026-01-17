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
    return create_engine(
        url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=0
    )

@st.cache_data(ttl=600)
def run_query(query):
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)
