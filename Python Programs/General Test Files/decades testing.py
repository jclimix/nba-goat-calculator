size = 40

season_history = [[] for _ in range(size)]  # Initialize an empty list for each decade

int_list = []

era_score = [0] * 4815  # Initialize as a list with five zeros

season_history [0] = ['1990-91', '1991-92', '1992-93', '1993-94', '1994-95']
season_history [1] = ['1968-69', '1969-70', '1970-71', '1971-72', '1972-73', '1973-74', '1974-75', '1975-76', '1976-77', '1977-78']
season_history [2] = ['1969-70', '1970-71', '1971-72', '1972-73', '1973-74', '1974-75', '1975-76', '1976-77', '1977-78', '1978-79', '1979-80', '1980-81', '1981-82', '1982-83', '1983-84', '1984-85', '1985-86', '1986-87', '1987-88', '1988-89']
season_history [3] = ['1990-91', '1991-92', '1992-93', '1993-94', '1994-95', '1995-96', '1996-97', '1997-98', '2000-01']

years50 = ["1949-50", "1950-51", "1951-52", "1952-53", "1953-54", "1954-55", "1955-56", "1956-57", "1957-58", "1958-59"]
years60 = ["1959-60", "1960-61", "1961-62", "1962-63", "1963-64", "1964-65", "1965-66", "1966-67", "1967-68", "1968-69"]
years70 = ["1969-70", "1970-71", "1971-72", "1972-73", "1973-74", "1974-75", "1975-76", "1976-77", "1977-78", "1978-79"]
years80 = ["1979-80", "1980-81", "1981-82", "1982-83", "1983-84", "1984-85", "1985-86", "1986-87", "1987-88", "1988-89"]
years90 = ["1989-90", "1990-91", "1991-92", "1992-93", "1993-94", "1994-95", "1995-96", "1996-97", "1997-98", "1998-99"]
years00 = ["1999-00", "2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06", "2006-07", "2007-08", "2008-09"]
years10 = ["2009-10", "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19"]
years20 = ["2019-20", "2020-21", "2021-22", "2022-23"]

factor50 = 5
factor60 = 3
factor70 = 2
factor80 = 2
factor90 = 5
factor00 = 5
factor10 = 5
factor20 = 2

for i, int_list in enumerate(season_history):  # Enumerate to get the player ID

# Look for 1950s
    found_integers = [x for x in int_list if x in years50]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor50 * 10)

# Look for 1960s
    found_integers = [x for x in int_list if x in years60]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor60 * 10)

# Look for 1970s
    found_integers = [x for x in int_list if x in years70]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor70 * 10)

# Look for 1980s
    found_integers = [x for x in int_list if x in years80]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor80 * 10)

# Look for 1990s
    found_integers = [x for x in int_list if x in years90]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor90 * 10)

# Look for 2000s
    found_integers = [x for x in int_list if x in years00]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor00 * 10)

# Look for 2010s
    found_integers = [x for x in int_list if x in years10]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor10 * 10)

# Look for 2020s
    found_integers = [x for x in int_list if x in years20]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor20 * 10)

for i in range(len(season_history)):
    print("Player with INDEX: " + str(i) + " has an ERA Score of " + str(era_score[i]))
