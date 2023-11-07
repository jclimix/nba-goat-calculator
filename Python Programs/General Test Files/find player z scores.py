import pandas as pd
import numpy as np

# Create and render the table (you need to pass data to a template)
data = []  # Your data here

player_count = 3

player_name = player_count * [0]
r_ppg = player_count * [0]
r_apg = player_count * [0]
r_rpg = player_count * [0]
r_spg = player_count * [0]
r_bpg = player_count * [0]
r_3fg = player_count * [0] 
r_fg = player_count * [0]
r_efg = player_count * [0]
r_ts = player_count * [0]

p_ppg = player_count * [0]
p_apg = player_count * [0]
p_rpg = player_count * [0]
p_spg = player_count * [0]
p_bpg = player_count * [0]
p_3fg = player_count * [0]
p_fg = player_count * [0]
p_efg = player_count * [0]
p_ts = player_count * [0]

#assign values
player_name[0] = "Alaa Abdelnaby"
player_name[1] = "Zaid Abdul-Aziz"
player_name[2] = "Kareem Abdul-Jabbar"
r_ppg[0] = 6.0
r_ppg[1] = 8.7
r_ppg[2] = 24.6
r_apg[0] = 0.3
r_apg[1] = 1.1
r_apg[2] = 3.6
r_rpg[0] = 3.4
r_rpg[1] = 7.9
r_rpg[2] = 11.2
r_spg[0] = 0.3
r_spg[1] = 0.6
r_spg[2] = 0.9
r_bpg[0] = 0.3
r_bpg[1] = 0.9
r_bpg[2] = 2.6
r_3fg[0] = 0.000
r_3fg[1] = 0.000
r_3fg[2] = 0.056
r_fg[0] = 0.507
r_fg[1] = 0.422
r_fg[2] = 0.559
r_efg[0] = 0.507
r_efg[1] = 0.422
r_efg[2] = 0.559
r_ts[0] = 0.535
r_ts[1] = 0.473
r_ts[2] = 0.592

p_ppg[0] = 2.2
p_ppg[1] = 5.1
p_ppg[2] = 24.3
p_apg[0] = 0.2
p_apg[1] = 0.5
p_apg[2] = 3.2
p_rpg[0] = 1.2
p_rpg[1] = 3.6
p_rpg[2] = 10.5
p_spg[0] = 0.0
p_spg[1] = 0.1
p_spg[2] = 1.0
p_bpg[0] = 0.1
p_bpg[1] = 0.7
p_bpg[2] = 2.4
p_3fg[0] = 0.000
p_3fg[1] = 0.000
p_3fg[2] = 0.000
p_fg[0] = 0.450
p_fg[1] = 0.529
p_fg[2] = 0.533
p_efg[0] = 0.450
p_efg[1] = 0.529
p_efg[2] = 0.533
p_ts[0] = 0.455
p_ts[1] = 0.565
p_ts[2] = 0.571

season_history = player_count * [0]

season_history [0] = ['1990-91', '1991-92', '1992-93', '1993-94', '1994-95']
season_history [1] = ['1968-69', '1969-70', '1970-71', '1971-72', '1972-73', '1973-74', '1974-75', '1975-76', '1976-77', '1977-78']
season_history [2] = ['1969-70', '1970-71', '1971-72', '1972-73', '1973-74', '1974-75', '1975-76', '1976-77', '1977-78', '1978-79', '1979-80', '1980-81', '1981-82', '1982-83', '1983-84', '1984-85', '1985-86', '1986-87', '1987-88', '1988-89']

# Replace 'your_excel_file.xlsx' with the path to your Excel workbook

df = pd.read_excel(r'C:\Users\jezei\OneDrive\Documents\Data Projects\NBA GOAT\StatmuseBookAVG.xlsx')

# Convert the DataFrame into a NumPy array
array_data = df.to_numpy()

i = 0 # where i = the size of the season_history array (player_count)

#iterate through all players in seasons_history array starting from 0
while i < len(season_history):

    #temp placeholders for excel workbook AVGs
    era_r_ppg = 0
    era_r_apg = 0
    era_r_rpg = 0
    era_r_spg = 0
    era_r_bpg = 0
    era_r_3fg = 0
    era_r_fg = 0
    era_r_efg = 0
    era_r_ts = 0

    era_p_ppg = 0
    era_p_apg = 0
    era_p_rpg = 0
    era_p_spg = 0
    era_p_bpg = 0
    era_p_3fg = 0
    era_p_fg = 0
    era_p_efg = 0
    era_p_ts = 0

    final_era_r_ppg = 0
    final_era_r_apg = 0
    final_era_r_rpg = 0
    final_era_r_spg = 0
    final_era_r_bpg = 0
    final_era_r_3fg = 0
    final_era_r_fg = 0
    final_era_r_efg = 0
    final_era_r_ts = 0

    final_era_p_ppg = 0
    final_era_p_apg = 0
    final_era_p_rpg = 0
    final_era_p_spg = 0
    final_era_p_bpg = 0
    final_era_p_3fg = 0
    final_era_p_fg = 0
    final_era_p_efg = 0
    final_era_p_ts = 0

    r_all_ppg = 0
    r_mean_ppg = 0
    sq_diff = player_count * [0]


    #iterate through all seasons of a single player
    a = 0 # where a = length of the current player's career in years (# of years played)

    while a < len(season_history[i]):
        
        year = str(season_history[i][a])

        print(f"year: {year}")

        for points in r_ppg[i]:
             
             r_all_ppg += points

        r_mean_ppg = r_all_ppg / #count

        # to iterate through excel workbook and retrieve era stats

        b = 0 # where b = number of rows in excel workbook

        while b < len(array_data):
                
                #print(f"array_data (excel): {array_data[b,2]}")

                if str(year) == str(array_data[b,2]):

                    print("year match")

                    era_r_ppg += array_data[b,3]
                    era_r_apg += array_data[b,4]
                    era_r_rpg += array_data[b,5]
                    era_r_spg += array_data[b,6]
                    era_r_bpg += array_data[b,7]
                    era_r_fg += array_data[b,8]
                    era_r_3fg += array_data[b,9]
                    era_r_efg += array_data[b,10]
                    era_r_ts += array_data[b,11]

                    era_p_ppg += array_data[b,12]
                    era_p_apg += array_data[b,13]
                    era_p_rpg += array_data[b,14]
                    era_p_spg += array_data[b,15]
                    era_p_bpg += array_data[b,16]
                    era_p_fg += array_data[b,17]
                    era_p_3fg += array_data[b,18]
                    era_p_efg += array_data[b,19]
                    era_p_ts += array_data[b,20]

                b += 1

        a = a + 1

    #calculations

    for year in season_history:
         if year == 