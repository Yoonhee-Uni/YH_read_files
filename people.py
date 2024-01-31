import yaml
import pprint
import ruamel.yaml


def read_file():
    with open('data/people.yml', 'r', encoding ='utf-16') as yml_file:
        prime_service = yaml.safe_load(yml_file)
        return prime_service

read_yfile = read_file()    

# task1
def craigs_job():
    job = [job['job'] for job in read_yfile['people'] if job['name'] == 'Craig']
    print('Craig\'s job is : ', job[0])

# task2
def rons_interests():
    interests = [interest['interests'] for interest in read_yfile['people'] if interest['name'] == 'Ron']
    print('Ron\'s interest is :', interests[0])

# task3
def averge_age():
    age = [ find_age['age'] for find_age in read_yfile['people'] if type(find_age['age']) == int ]
    print("average age is:" , round(sum(age)/ len(age),2))

# task4
def list_dict():
    pprint.pprint([read_yfile])

# task5
def tombolas():
    find_tombolas = [find_name['name'] for find_name in read_yfile['people'] if "Tombolas" in find_name['interests']]
    print(find_tombolas)

# task6
def edit_file():
    my_info = {'name' : 'Yoonhee',
      'age': 32,
      'job': 'Unemployeed',
      'interests':
          [
              "Drawing",
              "Coding",
              "Traveling",
              "Gardening",
              "Math",
          ],
    'wants': ["I want to be wise", "graceful", "wisdom"],
    'location': 'Manchester',
    'favorite song':' Shang-a-lang-a',
    'favorite movie': 'I am legend'
    }

    yaml = ruamel.yaml.YAML()    

    # call existing data
    with open('data/people.yml', 'r', encoding='utf-16') as yaml_file:
        existing_data = yaml.load(yaml_file)

    # adding new data 
    existing_data['people'].append(my_info)

    # put into a file
    with open('data/people.yml', 'w', encoding='utf-16') as file:
        yaml.dump(existing_data, file)


# task 7 
def add_colour():
    yaml = ruamel.yaml.YAML()   

    with open('data/people.yml', 'r', encoding='utf-16') as yaml_file:
        existing_data = yaml.load(yaml_file)
            
    for data in existing_data['people']:
        data['Colour'] = 'Red'

    with open('data/people.yml', 'w', encoding='utf-16') as file:
        yaml.dump(existing_data,file)

# task 8
def find_london():
    yaml = ruamel.yaml.YAML()  

    with open('data/people.yml', 'r', encoding='utf-16') as yaml_file:
        existing_data = yaml.load(yaml_file)

    for data in existing_data['people']:
        if data['location'] == 'London':
            data['location'] = 'The City'
    
    with open('data/people.yml', 'w', encoding='utf-16') as file:
        yaml.dump(existing_data,file)
find_london()                