def get_connection():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"],
            port=st.secrets["mysql"]["port"],
            ssl_disabled=True,        # 👈 IMPORTANT FIX
            connection_timeout=10     # 👈 prevents hanging
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
