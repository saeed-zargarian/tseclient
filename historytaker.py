import  pytse_client as t
import openpyxl as x
voroodi = input('سهم موردنظر:\n')
symbol = t.Ticker(voroodi)
History = symbol.history
file1 = './history/{} - تاریخچه.xlsx'
file2 = file1.format(voroodi)
Clients = symbol.client_types
file3 = './history/{} - حقیقی و حقوقی.xlsx'
file4 = file3.format(voroodi)
History.to_excel('{}'.format(file2))
Clients.to_excel('{}'.format(file4))
