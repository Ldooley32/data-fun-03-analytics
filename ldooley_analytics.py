# yourname_analytics.py

"""
The purpose of this script is to fetch data from the web, using python collections processes the data,
and write the processed data to different file formats.
"""

# Standard library imports
import csv
import pathlib
import json
import socket
import ssl

# External library imports
import requests
import pandas as pd

# The Write functions
def write_txt_file(folder_name, filename, data):
    
    '''construct a file path using pathlib'''

    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
   
    with file_path.open('w') as file: # opens file in write mode to write date in file
        file.write(data)

    print(f"Text data saved to {file_path}") # print message to confirm the data has been saved to a file.



def write_csv_file(folder_name, filename, data):
    
    '''construct a file path using pathlib'''

    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w', newline='') as file: # open in write mode and use newline to handle line endings
        writer = csv.writer(file)
        writer.writerows(data)
   
    print(f"CSV data saved to {file_path}") # print message to confirm the data has been saved to a file.



def write_json_file(folder_name, filename, data):
    
    '''construct a file path using pathlib'''

    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w') as file:  # print message to confirm the data has been saved to a file.
        
        json.dump(data, file, indent=4) # use json.dump to keep json formating
    
    print(f"JSON data saved to {file_path}") # print message to confirm the data has been saved to a file.



def write_excel_file(folder_name, filename, data):
    
    '''construct a file path using pathlib'''

    file_path = pathlib.Path(folder_name) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('wb') as file:   #open excel in binary mode to write date to file
        file.write(data)
   
    print(f"Excel data saved to {file_path}")  # print message to confirm the data has been saved to a file.



# Fetch functions to get data from a URL
def fetch_and_write_txt_data(folder_name, filename, url):
    try:
        response = requests.get(url) #send request to the url
        response.raise_for_status()  #request for status

        ''' write response text when status = 200'''
        
        write_txt_file(folder_name, filename, response.text)
   
    except requests.exceptions.RequestException as e: # when request fails print fail message
        print(f"Failed to fetch data: {e}")


def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url) #send request to the url
        response.raise_for_status() #request for status

        '''When response is successful (status = 200) request http content as a Unicode sting, 
        to be split into line, then convert lines into fields'''

        decoded_content = response.content.decode('utf-8')
        reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(reader)
        write_csv_file(folder_name, filename, data)
    
    except requests.exceptions.RequestException as e: # when request fails print fail message
        print(f"Failed to fetch data: {e}")

def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
       
        '''When response is successful (status =200) write json file'''

        write_json_file(folder_name, filename, response.json())
    
    except requests.exceptions.RequestException as e: # when request fails print fail message
        print(f"Failed to fetch data: {e}")



def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        '''When response is successful (status = 200) write excel file'''

        write_excel_file(folder_name, filename, response.content)
    
    except requests.exceptions.RequestException as e: # when request fails print fail message
        print(f"Failed to fetch Excel data: {e}")


# Processing functions
def process_txt_file(folder_name, filename, output_filename):
    file_path = pathlib.Path(folder_name) / filename
    output_path = pathlib.Path(folder_name) / output_filename
    with file_path.open('r') as file:
        content = file.read()
    
    '''Split text into words, calculate the word count and unique 
    word count, and format result'''

    words = content.split()
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    
    result = f"Word count: {word_count}\nUnique words: {unique_word_count}\n" #Saving proccessed data in folder and file
    with output_path.open('w') as file:
        file.write(result)
    
    print(f"Processed text data saved to {output_path}") #confirming data has been saved

def process_csv_file(folder_name, filename, output_filename):
    file_path = pathlib.Path(folder_name) / filename
    output_path = pathlib.Path(folder_name) / output_filename
    with file_path.open('r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)
     
    '''count rows and columns'''

    num_rows = len(rows)
    num_columns = len(headers)
    
    result = f"Number of rows: {num_rows}\nNumber of columns: {num_columns}\n" #Saving proccessed data in folder and file

    with output_path.open('w') as file:
        file.write(result)
   
    print(f"Processed CSV data saved to {output_path}") #confirming data has been saved

def process_json_file(folder_name, filename, output_filename):
    file_path = pathlib.Path(folder_name) / filename
    output_path = pathlib.Path(folder_name) / output_filename
    with file_path.open('r') as file:
        data = json.load(file)
    
    '''set up json data to be easier readability'''


    result = json.dumps(data, indent=4)
    with output_path.open('w') as file: #Saving proccessed data in folder and file
        file.write(result)
    print(f"Processed JSON data saved to {output_path}") #confirming data has been saved

def process_excel_file(folder_name, filename, output_filename):
    file_path = pathlib.Path(folder_name) / filename
    output_path = pathlib.Path(folder_name) / output_filename
    df = pd.read_excel(file_path)
    
    '''count rows and columns'''

    num_rows, num_columns = df.shape
    
    result = f"Number of rows: {num_rows}\nNumber of columns: {num_columns}\n" #Saving proccessed data in folder and file
    with output_path.open('w') as file: 
        file.write(result)
    print(f"Processed Excel data saved to {output_path}") #confirming data has been saved


def main():
    ''' Main function demonstrating module capabilities. '''
    
    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'
    
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'
    
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'
    
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)
    
    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_xls.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

if __name__ == '__main__':
    main()
