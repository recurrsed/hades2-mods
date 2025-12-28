import csv

def transformDataForChart():
    xData = []
    yData = {}

    with open('./values.csv', mode ='r') as file:
        csvFile = csv.reader(file)
    
        for line in csvFile:
            if line[0] == "Label":
                continue

            resource = line[0]
            value = float(line[1])
            timestamp = float(line[2])

            if timestamp not in xData:
                xData.append(timestamp)

            if resource not in yData:
                yData[resource] = [value]
            else:
                yData[resource].append(value)
    
    return xData, yData


transformDataForChart()