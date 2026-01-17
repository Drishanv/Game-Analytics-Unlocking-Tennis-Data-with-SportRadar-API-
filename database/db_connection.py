import psycopg2
import pandas as pd
import streamlit as st


def get_connection():
    try:
        conn = psycopg2.connect(
            host=st.secrets["postgres"]["host"],
            user=st.secrets["postgres"]["user"],
            password=st.secrets["postgres"]["password"],
            dbname=st.secrets["postgres"]["database"],
            port=st.secrets["postgres"]["port"],
            sslmode="require"
        )
        return conn
    except Exception as e:
        st.error("❌ Database connection failed")
        st.error(str(e))
        st.stop()


def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
