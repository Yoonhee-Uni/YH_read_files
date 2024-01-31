from csv import writer
import csv

pizza_list = []
task_three=[]
with open('data/pizza.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        pizza_list.append(row)

#task2
def capri_pizza():
    for pizza in pizza_list:
        if pizza['Pizza'] == "Capri":
            descriptions = pizza['Description'].split()
            
            for description in descriptions:
                print(description)
# task3
def cost(e):
    return float(e['Cost'][1:])
pizza_list.sort(key=cost)

for pizza in pizza_list:
    if float(pizza["Cost"][1:]) < 10.50:
        print(pizza["Pizza"], pizza["Cost"])

#task4
def new_pizza():
    new_pizza_menu=[]
    new_pizza = ['gochujang-pizza','£9.56', 'gochujang-paste, Mozzarella cheese, chilli, hot chili', '7300kcal']

    with open('data/pizza.csv', 'a', newline='') as csvfile:
        writer_obj = writer(csvfile)
        writer_obj.writerow(new_pizza)     
        
# task5
def new_pizza_price():
    datas =[]
    new_menu = []

    with open('data/pizza.csv', 'r') as csvfile:
        spreadsheet = csv.DictReader(csvfile)
        for row in spreadsheet:
            datas.append(row)
        for data in datas:
            data['Cost'] = '£'+str(round(float(data['Cost'][1:])*1.1,2))
            print(data)
# extension tasks
# task1

def vege_option():
    updated_vege = []
    for pizza in pizza_list:
        for ingredient  in pizza['Description'].split(', '):
            if ingredient not in ['ham', 'anchovies', 'pepperoni', 'salami', 'tomato and ham'] :
                pizza['option'] = 'Vegetarian'
            else:
                pizza['option'] = 'Non_Vegetarian'
        updated_vege.append(pizza)
        
    for menu in updated_vege:
        print (menu)
vege_option()


# split description and check if list are in the dict










