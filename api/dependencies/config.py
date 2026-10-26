
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = os.getenv("MYSQL_PASSWORD")
