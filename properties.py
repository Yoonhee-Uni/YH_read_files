from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import xmltodict


def read_file():
    with open('data/properties.xml', 'r') as f:
        data = f.read()
        Bs_data = BeautifulSoup(data, "xml")
        return Bs_data

read_data = read_file()

def get_cost():
    # extract plot_size 
    b_plot_size = read_data.find_all('plot_size')
    list_of_size = [size.get_text().strip() for size in b_plot_size]

    # extract biggest plot_size 
    max_size = max([float(sq[0:-5]) for sq in list_of_size])
    biggest = f"{int(max_size)} sq.ft"

    # extract plot_size -  cost
    b_cost = read_data.find('plot_size', string=biggest)
    if b_cost:
        b_cost = b_cost.find_next('cost').get_text()
        print(f"Biggest plot: {biggest}")
        print(f"Cost: {b_cost}")
    else:
        print(f"Could not find any information about {biggest}")

def get_description():
    #  extract description
    b_bungalow = read_data.find('bungalow').find('home3').find('description')
    print(f"Description of Bungalow home3 : {b_bungalow.get_text().strip()}")

def number_of_rooms():
    b_flat = read_data.find('flat').find('flat1').find('bathrooms')
    print( "Number of bathroom : ", b_flat.get_text().strip())

def read_xml_with_xmltodict():
    with open('data/properties.xml', 'r') as xml_file:
        xml_content = xml_file.read()
        return xml_content
    
xml_string = read_xml_with_xmltodict()    

# The function takes an XML string as its input argument. 
def list_of_bungalow(xml_file):
#It first creates an empty dictionary. Next, it obtains an element tree from the string using the fromstring() method. 
    root=ET.fromstring(xml_file)
    result = {}
# Now, we will check if the current node has 0 children. For this, we will check the length of the child attribute of the current node.
    for child in root:
        if len(child) == 0 :
            result[child.tag] =child.text
        else:
            result[child.tag] = list_of_bungalow(ET.tostring(child))
            return result

python_dict =  list_of_bungalow(xml_string)
print("The python dictionary is:")
print(python_dict)    



# list_of_bungalow(read_data)    


