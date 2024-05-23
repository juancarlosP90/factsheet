# import PyPDF2
# #rb lectura binaria
# pdf = open("ArrowsideQ1_2024.pdf","rb")

# reader = PyPDF2.PdfReader(pdf)

# #extraer una pagina en especifico
# #page = reader._get_page(2)
# #print(page.extract_text())

# #Imprimir todas las paginas del PDF
# for no_page in range(len(reader.pages)):
#     print("pagina", no_page+1)
#     info_page = reader._get_page(no_page)
#     extract_info = info_page.extract_text()
#     print(extract_info)
#     print("***********************")

import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "ada.xlsx"
df = pd.read_excel(excel_file_path)
#print(df.head())

valores = df[["date","Dynamic Allocation Gross","Dynamic Allocation Net","S&P 500 Total Return"]]
print(valores)

ax = valores.plot.bar(x="date", y="Dynamic Allocation Net", rot = 0)

plt.show()