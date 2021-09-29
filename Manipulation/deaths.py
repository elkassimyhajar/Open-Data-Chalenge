from csv import reader, writer

def getSet():
    new_column_header = "Continent"
    with open('../Datasets/air-pollution-deaths-by-age.csv', 'r') as read_obj, \
            open('../Datasets/output_deaths.csv', 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append to the header
            if csv_reader.line_num == 1:
                row[3] = 'Deaths - Age: 5-14 years'
                row[4] = 'Deaths - Age: under 5 years'
                row[5] = 'Deaths - Age: 70+ years'
                row[6] = 'Deaths - Age: 50-69 years'
                row[7] = 'Deaths - Age: 15-49 years'
                row.append('Total')
                row.append(new_column_header)
            else:
                #Calculate the total

                # Append the continent using the country name
                # Asia
                if row[0] in {'Afghanistan', 'Armenia', 'Azerbaijan',
                'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'Central Asia',
                'China', 'East Asia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel',
                'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon',
                'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea',
                'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia',
                'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand',
                'Timor', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
                'Yemen'}:
                    row.append("Asia")
                #Europe
                elif row[0] in {'Albania', 'Andorra', 'Austria',
                'Belarus', 'Belgium', 'Bermuda', 'Bosnia and Herzegovina', 'Bulgaria', 'Central Europe',
                'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Eastern Europe', 'England', 'Estonia'
                'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland',
                'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova',
                'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Scotland',
                'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom',
                'Wales', 'Finland'}:
                    row.append("Europe")
                #Africa
                elif row[0] in {'Algeria', 'Angola', 'Benin', 'Botswana',
                'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic',
                'Central Sub-Saharan Africa', 'Chad', 'Comoros', 'Congo', 'Cote d\'Ivoire', 'Democratic Republic of Congo',
                'Djibouti', 'Eastern Sub-Saharan Africa', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia',
                'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Jamaica', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
                'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger',
                'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'Sudan', 'Tanzania', 'Togo', 'Tunisia',
                'Uganda', 'Zambia', 'Zimbabwe'}:
                    row.append("Africa")
                #Americas
                elif row[0] in {'Andean Latin America', 'Antigua and Barbuda', 'Argentina'
                , 'Bahamas', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Caribbean',
                'Central Latin America', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica',
                'Dominican Republic', 'Ecuador', 'El Salvador', 'Greenland', 'Grenada',
                'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Mexico', 'Nicaragua', 'North America', 'Panama',
                'Paraguay', 'Peru', 'Puerto Rico', 'Saint Lucia', 'Suriname', 'Trinidad and Tobago', 'United States',
                'United States Virgin Islands', 'Uruguay', 'Venezuela'}:
                    row.append("Americas")
                #Oceania
                elif row[0] in {'American Samoa', 'Australasia', 'Australia', 'Fiji', 'Guam',
                'Kiribati', 'Marshall Islands', 'Micronesia', 'New Zealand', 'Samoa', 'Solomon Islands',
                'Tonga', 'Vanuatu'}:
                    row.append("Oceania")
                else:
                    continue
            # Add the updated row / list to the output file
            csv_writer.writerow(row)

getSet()

def getCountries():
    #Get countries from dataset
    with open('../Datasets/output_deaths.csv', 'r') as read_obj, \
        open('../Datasets/countries.csv', 'w', newline='') as write_obj:

        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)

        Category = []
        for row in csv_reader:
            if csv_reader.line_num != 1 and row[0] not in Category:
                Category.append(row[0])
                csv_writer.writerow([row[0]])    
getCountries()