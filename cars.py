import json
import csv

# task1
def read_file():
    with open("data/cars.json", "r", encoding = 'utf-8') as json_file:
        jsonDatas = json.load(json_file)
    data = jsonDatas["Cars"]
    
    return data

jsonfiles = read_file()

# task2
def car_makes():
    brand =[]
    for jsonfile in jsonfiles:
        if jsonfile['make'] not in brand:
            brand.append(jsonfile['make'])
    print("All the brands : ", brand)        

# task3
def car_age(e):
    return e['year']
    
sorted = jsonfiles.sort(key=car_age)
age = []
for jsonfile in jsonfiles:
    if 2024-jsonfile['year'] < 20:
        age.append(jsonfile['model'])
# print('age', age)

# task4
def new_cars():

    new_car = {
        'vin': 'WAGAWAGA123456789', 'make': 'Tesla', 'model': 'Tetemozzi', 'year': 2010, 'colour': 'white'
        }
    with open("data/cars.json", 'r+', encoding="utf-8") as jsonfile:
        file_data = json.load(jsonfile)
        file_data["Cars"].append(new_car)
        jsonfile.seek(0)
        json.dump(file_data,jsonfile, indent =4)

# task5

def update_year():
    updated_jsonfiles = []
    for jsonfile in jsonfiles:    
        if jsonfile['model'] == 'Tempo':
            jsonfile['year'] = 1985
            updated_jsonfiles.append(jsonfile)
        else : updated_jsonfiles.append(jsonfile)    

    print("updated", updated_jsonfiles)
    return updated_jsonfiles

# extension tasks
# task1
def update_fuel_type():
    updated_fuel_type =[]
    for jsonfile in jsonfiles:
        if jsonfile['make'] in ['Ford', 'Mercury', 'Toyota', 'Dodge']:
            jsonfile['fuel'] = 'petrol'
        else:
            jsonfile['fuel'] = 'electric'
        updated_fuel_type.append(jsonfile)
    print("updated", updated_fuel_type)
    return updated_fuel_type

# task2
def json_to_csv():
    with open('data/cars.json') as json_file:
        data = json.load(json_file)
    cars_data = data['Cars']

    data_file = open('cars_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    count= 0

    for car in cars_data:
        if count == 0 :
            header = car.keys()
            csv_writer.writerow(header)
            count +=1

        csv_writer.writerow(car.values())
    data_file.close()

