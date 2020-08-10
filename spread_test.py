import gspread
gc = gspread.service_account('./service_account.json')
sh = gc.open("Apartment Hunt")
values = sh.sheet1.get_all_values()
#sh.sheet1.append_row([1,2,3,4,5,6,7,8])

print(values)
