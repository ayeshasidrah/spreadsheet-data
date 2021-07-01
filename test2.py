import re
import unittest
import pytest
import requests
import itertools
from collections import namedtuple

from gspread.exceptions import APIError
import gspread
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from google.oauth2.credentials import Credentials as UserCredentials

from gspread import utils

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

  # add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)

  # get the instance of spreadsheet
sheet = client.open("Mysheet").sheet1


class testUpdate:
 # to create a new spreadsheet
    def test_create(self):
        title = 'Test Spreadsheet'
        new_spreadsheet = self.client.create(title)
        self.assertTrue(isinstance(new_spreadsheet, gspread.models.Spreadsheet))

  #finding a cell

def find_cell():
    cell1 = cell = sheet.find("redmi")
    if cell1 not in sheet:
        print("cell not found")
    else:
        print("Found something at R%sC%s" % (cell.row, cell.col))


class utilsTest(unittest.TestCase):
    def test_a1_to_row_col(self):
        self.assertEqual(utils.a1_to_rowcol('ABC'),(2,1))

    # to extract id from url
    def test_extract_id_from_url(self):
        url_id_list = [

            (
                'https://docs.google.com/spreadsheets/d/'
                '1qpyC0X3A0MwQoFDE8p-Bll4hps/edit#gid=0',
                '1qpyC0X3A0MwQoFDE8p-Bll4hps',
            ),
            (
                'https://docs.google.com/spreadsheets/d/'
                '1qpyC0X3A0MwQoFDE8p-Bll4hps/edit',
                '1qpyC0X3A0MwQoFDE8p-Bll4hps',
            ),
            (
                'https://docs.google.com/spreadsheets/d/'
                '1qpyC0X3A0MwQoFDE8p-Bll4hps',
                '1qpyC0X3A0MwQoFDE8p-Bll4hps',
            ),

            (
                'https://docs.google.com/spreadsheet/'
                'ccc?key=1qpyC0X3A0MwQoFDE8p-Bll4hps&usp=drive_web#gid=0',
                '1qpyC0X3A0MwQoFDE8p-Bll4hps',
            ),
        ]

        for url, id in url_id_list:
            self.assertEqual(id, utils.extract_id_from_url(url))


    def  extract_id(self):
        self.assertRaises(gspread.NoValidUrlKeyFound, utils.extract_id_from_url("https://docs.google.com/spreadsheets/d/1Ds0HnehHrghBuL9CD_Zlp1w-im3GkpfWXGT2rRVxsfI/edit#gid=0"))

    def test_addr_converter(self):
        for row in range(0,4):
            for col in range(0,3):
                addr = utils.rowcol_to_a1(row,col)
                (r,c) = utils.a1_to_rowcol(addr)
                self.assertEqual((row,col),(r,c))

