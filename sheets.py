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
def get_records():
    data = sheet.get_all_records()
    pprint(data)

get_records()

class get_row_col():
    def __init__(self,row ,col):
        self.row = row
        self.col = col

    def get_row_col(row,col):
        row = sheet.row_values(1)
        col = sheet.col_values(3)
        cell = sheet.cell(2, 2).value
        pprint(row)
        pprint(col)
     # to get the value at particular cell
        pprint(cell)

    # to insert a row in spreadsheet
def insert_into_spreadsheet(row):

    insertRow = [5, "huawei", "excellent"]
    sheet.insert_row(row,3)
    
    
  # to delete a row at 4
  #sheet.delete_row(4)

  #converting the dictionary to pandas dataframe
class data_tables():
    def __init__(self):
        self.records_df = pd.Dataframe.from_dict(data=None)
        
    def data_df(self, data):
        records_df = pd.Dataframe.from_dict(data=data)
        records = records_df.head()
        print(records)
