# Dextools Data Scraper

This repository contains a Python script for scraping data from the Dextools API and saving it to a CSV file. The script fetches information about cryptocurrency pairs from the Dextools API and extracts specific data fields from the response. The extracted data is then parsed and saved to a CSV file named "Data.csv".

## Prerequisites

To run this script, you need to have the following installed:

- Python 3
- pandas library
- requests library

You can install the required libraries using the following command:

```
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository to your local machine or download the script directly.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the following command to execute the script:

```
python dextools_scraper.py
```

4. The script will start fetching data from the Dextools API and display the progress on the console. Once the script has finished, a CSV file named "Data.csv" will be created in the same directory.

## How it Works

1. The script uses the `requests` library to send HTTP requests to the Dextools API. It also utilizes the `pandas` library to manipulate and save the data to a CSV file.

2. The script defines a function called `parse_json` that takes the API response data as input and extracts specific fields from it. The extracted fields are stored in a dictionary.

3. Another function called `get_data` is defined to fetch data from the Dextools API. It takes a page number as input and sends a GET request to the API with the appropriate parameters. The response is checked for errors, and if successful, the data is parsed using the `parse_json` function.

4. In the main section of the script, a session object is created with the necessary headers for the API requests. The `main_data` list is initialized to store the parsed data.

5. A loop is started to iterate over the pages of data from the API. The `get_data` function is called for each page, and if successful, the parsed data is added to the `main_data` list.

6. After fetching all the data, the `main_data` list is converted to a pandas DataFrame and saved to a CSV file named "Data.csv". The file is appended if it already exists, or a new file is created with headers if it doesn't exist.

## Note

- Make sure to handle any exceptions or errors that may occur during the execution of the script.

- Adjust the `maxFdv` parameter in the `get_data` function if you want to modify the maximum FDV value for the API query.

- Uncomment and modify the lines in the `parse_json` function to include additional data fields if needed.

- Customize the CSV file name and save location according to your preference.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are always welcome!
