import os
from dotenv import load_dotenv

load_dotenv()

print("MONGO_URI =", os.getenv("MONGO_URI"))
print("DATABASE_NAME =", os.getenv("DATABASE_NAME"))
print("COLLECTION_NAME =", os.getenv("COLLECTION_NAME"))