
# find nearest location
#input: address or latlon




"""delete this
def load_csv(filename):
    #filename = 'data/tables/vic/east_sale/east_sale-201709.csv'
    #location = 'east_sale'
    #loc_cap = location.upper().replace('_',' ')
    with f as open(filename,'r'):
        filedata = print(f.read)
        try:
            #data = re.search('('+loc_cap+'.[\w\W]*)Totals',filedata).group(1)
            table_data = '\n'.join(filedata.split('\n')[13:-1]) 
        except:
            print('error')
            return 1
        #create pandas csv
        csv = pd.read_csv(io.StringIO(table_data))
"""

# load data
#input: daterange in months
def load_data(start_str='200901',end_str='202109',state,location):
    
csv_header = ['Station Name','Date','Evapo-Transpiration','Rain','PanEvaporation','MaximumTemperature','MinimumTemperature','MaximumRelativeHumidity','MinimumRelativeHumidity','Average10m WindSpeed','SolarRadiation']

def load_csv(filename):
    filename = 'data/tables/vic/east_sale/east_sale-201709.csv'
    with open(filename,'r') as f:
        filedata = f.read()
        try:
            table_data = '\n'.join(filedata.split('\n')[13:-1]) 
        except:
            print('error')
            return 1
    #create pandas csv
    csv = pd.read_csv(io.StringIO(table_data),header=None)
    return csv
    
#TODO VALIDATOR?
#TODO schema

# find max temps over a threshold
# input: threshold
