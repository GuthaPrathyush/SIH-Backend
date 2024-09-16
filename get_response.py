import pandas as pd

# Function to load the CSV and select district data
def load_and_get_district_data(csv_file, district_name):
    try:
        # Load the CSV into a DataFrame
        data = pd.read_csv(csv_file)

        # Check if the district exists in the CSV
        district_data = data[data['name of district'] == district_name]
        
        if district_data.empty:
            return f"District '{district_name}' not found in the data."
        
        # Prepare the key-value string
        result_string = f"Data for {district_name}:\n"
        district_dict = district_data.iloc[0].to_dict()  # Get the first row as a dictionary
        
        # Loop through the dictionary and prepare the key-value pairs
        for key, value in district_dict.items():
            if key != 'name of district':  # Skip the district name in the output
                result_string += f"{key}: {value}\n"

        return result_string

    except FileNotFoundError:
        return f"File '{csv_file}' not found."
    except Exception as e:
        return str(e)

