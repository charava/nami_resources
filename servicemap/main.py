import pandas as pd

# Try different encodings if utf-8 doesn't work
# encodings_to_try = ['utf-8', 'latin-1', 'ISO-8859-1']
govdata = pd.read_csv('FindTreatmentData.csv')
    
df = pd.DataFrame(govdata)

state_abbreviations = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'AS': 'American Samoa',
    'DC': 'District of Columbia',
    'FM': 'Federated States of Micronesia',
    'GU': 'Guam',
    'MH': 'Marshall Islands',
    'MP': 'Northern Mariana Islands',
    'PW': 'Palau',
    'PR': 'Puerto Rico',
    'VI': 'Virgin Islands'
}


state_political_leaning = {
    'AL': 'Conservative',
    'AK': 'Mixed/Variable',
    'AZ': 'Swing',
    'AR': 'Conservative',
    'CA': 'Liberal',
    'CO': 'Swing',
    'CT': 'Liberal',
    'DE': 'Liberal',
    'FL': 'Swing',
    'GA': 'Swing',
    'HI': 'Liberal',
    'ID': 'Conservative',
    'IL': 'Liberal',
    'IN': 'Conservative',
    'IA': 'Swing',
    'KS': 'Conservative',
    'KY': 'Conservative',
    'LA': 'Conservative',
    'ME': 'Swing',
    'MD': 'Liberal',
    'MA': 'Liberal',
    'MI': 'Swing',
    'MN': 'Swing',
    'MS': 'Conservative',
    'MO': 'Swing',
    'MT': 'Conservative',
    'NE': 'Conservative',
    'NV': 'Swing',
    'NH': 'Swing',
    'NJ': 'Liberal',
    'NM': 'Liberal',
    'NY': 'Liberal',
    'NC': 'Swing',
    'ND': 'Conservative',
    'OH': 'Swing',
    'OK': 'Conservative',
    'OR': 'Liberal',
    'PA': 'Swing',
    'RI': 'Liberal',
    'SC': 'Conservative',
    'SD': 'Conservative',
    'TN': 'Conservative',
    'TX': 'Conservative',
    'UT': 'Conservative',
    'VT': 'Liberal',
    'VA': 'Swing',
    'WA': 'Liberal',
    'WV': 'Conservative',
    'WI': 'Swing',
    'WY': 'Conservative',
    'AS': 'Non-voting Delegate',
    'DC': 'Liberal',
    'FM': 'Mixed/Variable',
    'GU': 'Non-voting Delegate',
    'MH': 'Mixed/Variable',
    'MP': 'Mixed/Variable',
    'PW': 'Mixed/Variable',
    'PR': 'Liberal',
    'VI': 'Non-voting Delegate'
}



state_counts = df['state'].value_counts()

state_counts_df = pd.DataFrame({'State Abbreviation': state_counts.index, 'Service Count': state_counts.values})

state_counts_df['State Name'] = state_counts_df['State Abbreviation'].map(state_abbreviations)
state_counts_df['Political Leaning'] = state_counts_df['State Abbreviation'].map(state_political_leaning)


print(state_counts_df)


"""
- correlation between severity of mental illness in counties and the amount of services?

- correlation between political leaning of states/counties and the amount of services?

- correlation between political leaning of states/counties and the severity of mental illness in the area? 

"""