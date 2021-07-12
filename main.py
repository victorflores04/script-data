import csv
import sys
import re
list_state_us = ['United States', 'Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
list_state_us_short = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']

# csv file name
filename = input('¿Agregar ruta del archivo inicial?')
filenamedic= input('¿Agregar ruta final del archivo inicial?')
# filename = 'us_customers.csv'
# csv data
custom_list = []
with open(filename, 'r') as File:
    # creating a csv reader object
    us_customer_reader = csv.DictReader(File, dialect='excel')
    custom_list = list(us_customer_reader)
    print('<------Init---filter------>')
    with open(filenamedic, 'w', newline='') as csvFile:
        fieldnames = ['First Name', 'Last Name', 'State', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        try:
            for index in range(len(list(custom_list))):
                custom_list[index]['Phone'] = re.sub("\-|\ |\)|\(|\`|\+", "", custom_list[index]['Phone'])
                if custom_list[index]['State'] in list_state_us or custom_list[index]['State'] in list_state_us_short:
                    if len(custom_list[index]['Phone']) == 10:
                        custom_list[index]['Phone'] = '1' + custom_list[index]['Phone']
                writer.writerow(
                        {'First Name': custom_list[index]['First Name'], 'Last Name': custom_list[index]['Last Name'],
                         'State': custom_list[index]['State'], 'Phone': custom_list[index]['Phone'], 'Email': custom_list[index]['Email'], 'Address': custom_list[index]['Address']})
            print('Finish---filter')
        except csv.Error as e:
            sys.exit('file {}, newline {}: {}'.format(filename, us_customer_reader.line_num, e))