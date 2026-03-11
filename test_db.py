print("===== FILE STARTED RUNNING =====")

from db_mysql import fetch_one

print("===== IMPORT SUCCESSFUL =====")

print("Testing MySQL connection...")

result = fetch_one("SELECT DATABASE();")

print("===== FETCH COMPLETED =====")
print("Connected to database:", result)