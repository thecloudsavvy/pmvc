# ### script from chapqpt
# import sys
# print("Python executable:", sys.executable)
# print("Python version:", sys.version)

# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
# print(installed_packages_list)



import mysql.connector as MySQL
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
# print(type(host))
dbconn = MySQL.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    db = os.getenv("DB_NAME")
)
cursor = dbconn.cursor()
if(cursor):
    print("connected")
free = pd.read_excel("Fins.xlsx", index_col=0)
farmishes = pd.DataFrame(free).head().all()
# print(farmishes)
for farmish in range(len(farmishes)):
    famich = farmish + 1
    print(farmishes.iloc[0])
print(free)