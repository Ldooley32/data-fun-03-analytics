# datafun-03-analytics


 create Repository named datafun-03-analitics

Option 1

Use GitHub 
1. under repository click new
2. Add repo name
3. Make public 
4. Create README.md file 
5. Add .gitignore file using phython template

Option 2
create repo locally
1. open a terminal to the document folder
        '''cd documents'''
2. make a folder with repo name
        '''mkdir data-fun-03-analytics'''
4. open VS Code and open new repo folder.
3. Add a README.md file to document progress.
4. Add a .gitignore file and include files that don't need to be committed.

When using option 1 use VScode to clone repository to work locally.


Create / activate. Virtual Environment'


1. creating virtual environment
        '''phython 3 -m venu . venu'''
2. activate venv 
        '''source .venu/bin /activate '''
3. intall requests library package.
        '''python 3-m pip install requests'''
4  to create a requirements.txt
        '''Python 3-m pip freeze > requirements, txt.""
        
Add docstring to script 
        '''Create a module that collects data from the web and process into file/folder and process data to genterate output'''
Add librarys in the following order
import standard librarys
import External librarys
import local modules.


# Data Acquisition
Function 1 Use the requests library to fetch data from specified web APIs or online data sources. This will include JSON, CSV, and plain text data. After a successful fetch, call the appropriate write function to save the data to a file.


Function 2 Write Data
Write functions to save content to different file types (e.g., text, CSV, JSON).


# Process Data and Generate Output
Write functions to read, process, and write results using appropriate Python collections (lists, sets, dictionaries, etc.). Demonstrate understanding of each collection data type's characteristics and usage.

Process the fetched data using appropriate Python collections and generate insightful analytics. The results of the processing should be formatted and written into text files.

Process Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working with text files. Analyze text data to generate statistics like word count, frequency of words, etc., and format these findings into a readable text file.

Process Function 2. Process CSV Data: Process CSV files with tuples to demonstrate proficiency in working with tabular data. Extract and analyze data from CSV files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Process Function 3. Process Excel Data: Extract and analyze data from Excel files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Process Function 4. Process JSON Data: Process JSON data with dictionaries to demonstrate proficiency in working with labeled data. Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format.

# Implement Exception Handling
We know that reading and writing files - especially fetching items from the web is unreliable. Even with perfect code, there are many things that can go wrong. Use try/except/finally and implement exception handling to catch known possible errors and handle them gracefully in at least one of your functions.
Couldnt really figure this part out.

# Implement a main() function 
 test the folder creation functions and demonstrate the use of imported modules.

Python main() function code example:

def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: {yourname_attr.my_name_string}")

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
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

    # Find some data you care about. What format is it? How will you ingest the data?
    # What do you want to extract and write? What export format will you use?
    # Process at least TWO unique data sets and describe your work clearly.
    # Use the README.md and your code to showcase your ability to work with data.
Copies of the data files have been added to this repo. Click on a data file to view it. To save the data, click "Raw" in the upper right - this will show just the raw file content in your browser. In Chrome, right-click and select "Save as ..." to get a local copy to compare. This won't work for Excel files - save the .xls file directly from GitHub.

# Conditional Script Execution (At the end of the file)
Ensure the main function only executes when the script is run directly, not when imported as a module by using standard boilerplate code.

if __name__ == '__main__':
    main()
Module Design
The code should be clear, well-organized, and demonstrate good practices. Include comments and docstrings for clarity.

Evaluation Criteria
Functionality: The project should be functional and meet all requirements.
Documentation: The project should be well-written and well-documented.
Presentation: The project should be presented in a clear and organized manner.
Professionalism: The project should be submitted on-time and reflect an original, creative effort.
See rubric for additional information.
