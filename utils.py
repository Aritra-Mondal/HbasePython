def printRow(data, Row):
    for key in data:
        print(f"{Row} || {str(key, 'utf-8')} || {str(data[key][0],'utf-8')} || {str(data[key][1])}")