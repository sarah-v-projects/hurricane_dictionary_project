# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:


def updated_damages_function(damages):
    updated_damages_list = []
    for i in damages:
        if i != "Damages not recorded":
            if i[-1] == "M":
                number = float(i[:-1])
                number = number * 1000000
                updated_damages_list.append(number)
            elif i[-1] == "B":
                number = float(i[:-1])
                number = number * 100000000
                updated_damages_list.append(number)
        elif i == "Damages not recorded":
            updated_damages_list.append(i)
    return updated_damages_list

updated_damages = updated_damages_function(damages)


# write your construct hurricane dictionary function here:

zipped_hurricane_lists = list(zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))

def hurricane_dictionary_creation(zipped_hurricane_lists):
    hurricane_dictionary_create = {}
    for name, month, year, maxwind, areaaff, damage, deaths in zipped_hurricane_lists:
        hurricane_dictionary_create[name] = {"Name": name, 
                                      "Month": month, 
                                      "Year": year, 
                                      "Max Sustained Wind": maxwind, 
                                      "Areas Affected": areaaff, 
                                      "Damage": damage, 
                                      "Deaths": deaths}
    return hurricane_dictionary_create

hurricane_dictionary = hurricane_dictionary_creation(zipped_hurricane_lists)


# write your construct hurricane by year dictionary function here:


def hurricane_by_year_creation(hurricane_dictionary):
    hurricane_by_year_create = {}
    for name, record in hurricane_dictionary.items():
        current_year = (record["Year"])
        if current_year not in hurricane_by_year_create.keys():
            hurricane_by_year_create[current_year] = [record]
        else:
            hurricane_by_year_create[current_year].append(record)
    return hurricane_by_year_create

hurricane_by_year = hurricane_by_year_creation(hurricane_dictionary)

# write your count affected areas function here:


def count_hurricane_areas(areas_affected):
    area_affected_dictionary = {}
    for area_list in areas_affected:
        for area in area_list:
            if area not in area_affected_dictionary.keys():
                area_affected_dictionary[area] = 1
            else:
                area_affected_dictionary[area] += 1
    return area_affected_dictionary

top_areas_affected = count_hurricane_areas(areas_affected)


# write your find most affected area function here:

def most_affected_area(top_areas_affected):
    max_area_affected = ''
    max_area_count = 0
    for area in top_areas_affected:
        area_cycle = top_areas_affected[area]
        if area_cycle > max_area_count:
            max_area_count = top_areas_affected[area]
            max_area_affected = area

    return max_area_affected, max_area_count

area_affected_most, num_times_affected = most_affected_area(top_areas_affected)

# write your greatest number of deaths function here:
def num_deaths(hurricane_dictionary):
    max_death_count = 0
    name_max_death_count = ''
    for name, record in hurricane_dictionary.items():
        current_death_count = (record["Deaths"])
        if current_death_count > max_death_count:
            name_max_death_count = name
            max_death_count = current_death_count

    return name_max_death_count, max_death_count

name_highest_mortality, highest_mortality = num_deaths(hurricane_dictionary)

# write your catgeorize by mortality function here:

def hurricane_fatality(hurricane_dictionary):
    hurricanes_by_mortality = {0: [],
                               1: [],
                               2: [], 
                               3: [], 
                               4: [], 
                               5: []}
    hurricane_mortality_rating = { 0: 0,
                                   1: 100,
                                   2: 500,
                                   3: 1000,
                                   4: 10000}
    for name, record in hurricane_dictionary.items():
        temp_variable = (record["Deaths"])
        if temp_variable == hurricane_mortality_rating[0]:
            hurricanes_by_mortality[0].append(record)
        elif temp_variable > hurricane_mortality_rating[0] and temp_variable <= hurricane_mortality_rating[1]:
            hurricanes_by_mortality[1].append(record)
        elif temp_variable > hurricane_mortality_rating[1] and temp_variable <= hurricane_mortality_rating[2]:
            hurricanes_by_mortality[2].append(record)
        elif temp_variable > hurricane_mortality_rating[2] and temp_variable <= hurricane_mortality_rating[3]:
            hurricanes_by_mortality[3].append(record)
        elif temp_variable > hurricane_mortality_rating[3] and temp_variable <= hurricane_mortality_rating[4]:
            hurricanes_by_mortality[4].append(record)
        elif temp_variable > hurricane_mortality_rating[4]:
            hurricanes_by_mortality[5].append(record)
    return hurricanes_by_mortality

hurricanes_sorted_by_mortality_rating = hurricane_fatality(hurricane_dictionary)

# write your greatest damage function here:

def greatest_damage(hurricane_dictionary):
    max_damage = 0
    name_max_damage = ''
    for name, record in hurricane_dictionary.items():
        temp_variable = record["Damage"]
        if temp_variable == "Damages not recorded":
            throw_away = temp_variable
        elif temp_variable > max_damage:
            max_damage = temp_variable
            name_max_damage = name
    return name_max_damage, max_damage

name_greatest_damage, greatest_damage = greatest_damage(hurricane_dictionary)


# write your catgeorize by damage function here:
hurricane_by_damage_dict = {"Damages Not Recorded": [], 
                            0: [], 
                            1: [], 
                            2: [], 
                            3: [], 
                            4: [], 
                            5: []}
hurricane_damage_ratings = {0: 0,
                            1: 100000000,
                            2: 1000000000,
                            3: 10000000000,
                            4: 50000000000}
def hurricanes_by_damage(hurricane_dictionary):
    for name, record in hurricane_dictionary.items():
        temp_variable = record["Damage"]
        if temp_variable == "Damages not recorded":
            hurricane_by_damage_dict["Damages Not Recorded"].append(record)
        elif temp_variable == hurricane_damage_ratings[0]:
            hurricane_by_damage_dict[0].append(record)
        elif temp_variable > hurricane_damage_ratings[0] and temp_variable <= hurricane_damage_ratings[1]:
            hurricane_by_damage_dict[1].append(record)
        elif temp_variable > hurricane_damage_ratings[1] and temp_variable <= hurricane_damage_ratings[2]:
            hurricane_by_damage_dict[2].append(record)
        elif temp_variable > hurricane_damage_ratings[2] and temp_variable <= hurricane_damage_ratings[3]:
            hurricane_by_damage_dict[3].append(record)
        elif temp_variable > hurricane_damage_ratings[3] and temp_variable <= hurricane_damage_ratings[4]:
            hurricane_by_damage_dict[4].append(record)
        elif temp_variable > hurricane_damage_ratings[4]:
            hurricane_by_damage_dict[5].append(record)
    return hurricane_by_damage_dict

hurricanes_sorted_by_damage_rating = hurricanes_by_damage(hurricane_dictionary)

print("This first list sorts the given hurricanes by year: {}".format(str(hurricane_by_year)))
print("This second list sorts the regions affected by hurricanes from region most affected to region least affected: {}".format(str(top_areas_affected)))
print("This third list sorts the regions affected by hurricanes into fatality categories based on the number of fatalities: {}".format(str(hurricanes_sorted_by_mortality_rating)))
print("This fourth list sorts the regions affected by hurricanes into damage categories based on the dollar amount in damage suffered: {}".format(str(hurricanes_sorted_by_damage_rating)))
print("The most affected area in our data is {} with {} recorded hurricanes.".format(area_affected_most, num_times_affected))
print("The most lethal hurricane in our data was {} with {} lives lost.".format(name_highest_mortality, highest_mortality))
print("The most damaging hurricane in our data was {} with an estimated ${} in damages.".format(name_greatest_damage, greatest_damage))