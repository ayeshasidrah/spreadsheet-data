# spreadsheet-data
Creating a Spreadsheet
sh = client.create('A new spreadsheet')

Sharing a Spreadsheet
sh.share('auto@example.com', perm_type='user', role='writer')

to insert a row in spreadsheet
insertRow = [5, "huawei", "excellent"]
sheet.insert_row(row,3)
  
to delete a row at 4
sheet.delete_row(4)
