import xlrd
import json

wb = xlrd.open_workbook("CourseData.xlsx")
ws = wb.sheet_by_index(0)
header = [] # The row where we stock the name of the column
for col in range(ws.ncols):
    header.append( ws.cell_value(0,col) )

# tronsform the workbook to a list of dictionnary
data =[]
for row in range(1, ws.nrows):
    elm = {}

    for col in range(ws.ncols):
        if(header[col] == "SDGs"):
            if(ws.cell_value(row,col) != 0 and "," in str(ws.cell_value(row,col))):
                sdgs_set = set(int(x) for x in [i.strip() for i in ws.cell_value(row,col).split(",") if i.strip()])
                elm[header[col]]= sorted(list(sdgs_set))
            else:
                elm[header[col]]= [ws.cell_value(row,col)]
        else:
            elm[header[col]]=ws.cell_value(row,col)
    data.append(elm)


#saving to file
with open('src/assets/courses.json', 'w') as file:
    file.write(json.dumps(data))
