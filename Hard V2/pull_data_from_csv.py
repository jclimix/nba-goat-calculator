import pandas as pd

def read_csv_as_dataframe(csv_file_path):
    """
    Reads a CSV file and returns it as a pandas DataFrame.
    
    Args:
    csv_file_path (str): The file path to the CSV file.
    
    Returns:
    pandas.DataFrame: DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(csv_file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    csv_file_path = "nba-dataset-test.csv"  # Change this to your CSV file path
    dataframe = read_csv_as_dataframe(csv_file_path)
    if dataframe is not None:
        # Accessing a single column using square brackets []
        player_names = dataframe['PLAYER_NAME']
        print("Printing different cells in the column 'PLAYER_NAME':")
        print("First player name:", player_names[0])
        print("Second player name:", player_names[1])
        # Accessing a single column using dot notation
        r_ppg = dataframe.R_PPG
        print("\nPrinting different cells in the column 'R_PPG':")
        print("First player R_PPG:", r_ppg[0])
        print("Second player R_PPG:", r_ppg[1])
