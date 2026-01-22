import os
import psycopg2
from dotenv import load_dotenv
from urllib.parse import quote_plus


load_dotenv()



POSTGRES_HOST="aws-1-ap-south-1.pooler.supabase.com"
POSTGRES_PORT=5432
POSTGRES_USER="postgres.htkawrtndrknuwqyrlnf"
POSTGRES_PASSWORD="RiyuMithu!2017"
POSTGRES_DB="postgres"
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
print(DATABASE_URL)
#DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL="postgresql://postgres.htkawrtndrknuwqyrlnf:[RiyuMithu!2017]@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"


if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

try:
    print(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print("✅ Connected. Time:", cur.fetchone()[0])
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Failed to connect:", e)