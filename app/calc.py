import pandas as pd

from player import Player


class Calculator:
    def __init__(self) -> None:
        pass

    def read_csv_as_dataframe(self, csv_file_path) -> pd.DataFrame:
        try:
            df = pd.read_csv(csv_file_path)
            return df
        except FileNotFoundError:
            print(f"Error: File '{csv_file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the CSV file '{
                  csv_file_path}': {e}")
            return None

    def create_players_from_dataframe(self, dataframe):
        players = []
        for _, row in dataframe.iterrows():
            player_data = row.to_dict()
            player = Player(player_data)
            players.append(player)
        return players
