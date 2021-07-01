import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from pprint import pprint       # to print a more organised output import pprint


  # define the scope
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

  # add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

  #authorize the clientsheet
client = gspread.authorize(creds)

  # get the instance of spreadsheet
sheet = client.open("Mysheet").sheet1

  # to get all records of data
data = sheet.get_all_records()
pprint(data)

row = sheet.row_values(1)
col = sheet.col_values(3)

  # to get the value at specific cell
cell = sheet.cell(2,2).value
pprint(row)

  # to insert a row in spreadsheet
  #insertRow = [5, "huawei", "excellent"]
  #sheet.insert_row(row,3)
  # to delete a row at 4
  #sheet.delete_row(4)

  #converting the dictionary to pandas dataframe
class data_tables():
    def data_df(self, data):
        records_df = pd.Dataframe.from_dict(data)
        records = records_df.head()
        print(records)