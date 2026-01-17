import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import pandas as pd


@st.cache_resource
def get_engine():
    db = st.secrets["postgres"]

    DATABASE_URL = (
        f"postgresql+psycopg2://{db['user']}:{db['password']}"
        f"@{db['host']}:{db['port']}/{db['database']}"
        "?sslmode=require"
    )

    engine = create_engine(
        DATABASE_URL,
        poolclass=NullPool,   # IMPORTANT for Supabase + Streamlit
    )

    return engine


@st.cache_data(ttl=600)
def run_query(query: str):
    engine = get_engine()
    with engine.connect() as connection:
        return pd.read_sql(query, connection)
