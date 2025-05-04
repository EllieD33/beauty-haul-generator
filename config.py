from dotenv import load_dotenv
import os

load_dotenv()

HOST = "localhost"
USER = "root"
PASSWORD = os.getenv("PASSWORD") # Replace this with your own DB password: PASSWORD = <yourpasswordhere>