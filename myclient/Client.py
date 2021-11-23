
import requests as request
import json
import pandas as pd
import sys
# from sys import argv


print ('***** Welcome *****\n ')

url = 'http://sc17s2e.pythonanywhere.com/register/'
# url2 = 'http://127.0.0.1:8000/login/'
url3 = 'http://sc17s2e.pythonanywhere.com/logout/'
url4 = 'http://sc17s2e.pythonanywhere.com/list/'
url5 = 'http://sc17s2e.pythonanywhere.com/view/'
url6 = 'http://sc17s2e.pythonanywhere.com/average/'
url7 = 'http://sc17s2e.pythonanywhere.com/rate/'

client = request.Session()

while True:

    input_string = input('Please enter your syntax (type exit to quit): ')
    input_list = input_string.split()
    # print (input_list)

    if input_list[0] == 'register':
        username = input("Create a Username: ")
        password = input("Create a Password: ")
        email = input ("Email address: ")

        data = {'username': username, 'password': password, 'email': email}
        response = client.post(url, data=data)
        s1 = client.get(url)
        print (response.text)

    elif input_list[0] == 'login':
        if len(input_list) == 2:
            url2 = input_list[1]
            username2 = input("Please enter the Username: ")
            password2 = input("Please enter Password: ")
            data2 = {'username': username2, 'password': password2}
            response2 = client.post(url2, data=data2)
            s2 = client.get(url2)
            print (response2.text)
        else:
            print('Incorrect syntax! Try 2 number of arguments: "login <url>" ')


    elif input_list[0] == 'logout':
        response3 = client.post(url3)
        print(response3.text)

    elif input_list[0] == 'list':
        response4 = client.get(url4)
        json_data = response4.json()
        df = pd.DataFrame(json_data)
        print(df)

    elif input_list[0] == 'view':
        response5 = client.get(url5)
        json_data2 = response5.json()
        df2 = pd.DataFrame(json_data2)
        print(df2)

    elif input_list[0] == 'average':
        if len(input_list) == 3:
            profesor_id_input = input_list[1]
            module_code_input = input_list[2]
            data3 = {'Prof_input': profesor_id_input, 'Module_input': module_code_input}
            response6 = client.post(url6, data=data3)
            print (response6.text)
        else:
            print('Incorrect syntax! Try 3 number of arguments: "average <professor_id> <module_code>')

    elif input_list[0] == 'rate':
        if len(input_list) == 6:
            profesor_id_input = input_list[1]
            module_code_input = input_list[2]
            year = input_list[3]
            semester = input_list[4]
            rating = input_list[5]

            data4 = {'Prof_input': profesor_id_input, 'Module_input': module_code_input, 'Year': year, 'Semester': semester, 'Rating': rating}
            response7 = client.post(url7, data=data4)
            print (response7.text)
        else:
            print('Incorrect syntax! Try 6 number of arguments: "rate professor_id module_code year semester rating"')

    elif input_list[0] == 'exit':
        print('***** Goodbye *****')
        break

    else:
        print('Invalid syntax! Please check your query and try again.\n')
