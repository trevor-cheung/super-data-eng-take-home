import pandas as pd
from io import StringIO

def transform_data(data_str: str) -> pd.DataFrame:
    """
    Transforms the input data string into a cleaned DataFrame.
    The function performs the following operations:
    1. Cleans the FlightCodes column by filling in missing values with the previous value increased by 10.
    2. Splits the To_From column into two separate columns: To and From.
    3. Cleans the Airline Code column by removing any non-letter characters and leading/trailing spaces.

    Args:
        data_str (str): The input data string in CSV format.
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    mock_csv_file = StringIO(data_str) # Turn the string into a file-like object
    df = pd.read_csv(mock_csv_file, sep=';')

    # Clean the FlightCodes column
    # Fill in missing values with previous value but increased by 10
    df['FlightCodes'] = df['FlightCodes'].interpolate()
    # Change from float to int
    df['FlightCodes'] = df['FlightCodes'].astype(int)

    # Transform the To_From column
    df['To_From'] = df['To_From'].str.upper()
    df[['To', 'From']] = df['To_From'].str.split('_', expand=True)
    df.drop(columns=['To_From'], inplace=True)

    # Clean the Airline Code column
    df['Airline Code'] = df['Airline Code'].str.replace(r'[^a-zA-Z\s]', '', regex=True) # Replace anything that is not a letter or space with ''
    df['Airline Code'] = df['Airline Code'].str.strip()
    return df

if __name__ == "__main__":
    data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'
    table = transform_data(data)
    print(table)
