import xlwings as xw
import time
import os

# Path to your OneDrive Excel file
one_drive_path = os.path.expanduser('C:/Users/chadh/OneDrive/Desktop/x.xlsx')

# Open the Excel file
wb = xw.Book(one_drive_path)

# Refresh all data connections
wb.api.RefreshAll()

# Wait for 60 minutes (3600 seconds)
time.sleep(3600)

# Save and close the workbook
wb.save()
wb.close()
