
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

def check
    out[out['MaximumTemperature'] == '35.1']

# load data
#input: daterange in months
def load_data(state,location,start_str='200901',end_str='202109'):
    #TODO validate input
    datetime.datetime.strptime(start_str,'%Y%M') 
    datetime.datetime.strptime(end_str,'%Y%M') 
    date_range = pd.date_range(start=start_str+'01',end=end_str+'01',freq='MS')
    csv_list = []
    for date in date_range:
        date_str = str(date.year) + str(date.month).zfill(2) 
        filename = "data/tables/{}/{}/{}-{}.csv".format(state,location,location,date_str)
        csv = load_csv(filename)
        csv_list.append(csv)
    return_table = pd.concat(csv_list)
    return_table.reset_index(inplace=True)
    return return_table

##
start_str='200901'
end_str='202109'
state='nsw'
location='albury_airport'
datetime.datetime.strptime(start_str,'%Y%M') 
datetime.datetime.strptime(end_str,'%Y%M') 
date_range = pd.date_range(start=start_str+'01',end=end_str+'01',freq='MS')

csv_list = []
for date in date_range:
    date_str = str(date.year) + str(date.month).zfill(2) 
    filename = "data/tables/{}/{}-{}.csv".format(state,location,date_str)
    print(filename)
    csv = load_csv(filename)
    csv_list.append(csv.copy())
    print(len(csv_list))

return_table = pd.concat(csv_list)
return_table.reset_index(inplace=True)
##


    #iterate over dates,
        #construct filenames with locaiton and state
        #call load_csv
        #join
    #return


filename = 'data/tables/vic/east_sale/east_sale-201709.csv'

#TODO move csv_header from out of fn

def load_csv(filename):
    csv_header = ['Station Name','Date','Evapo-Transpiration','Rain','PanEvaporation','MaximumTemperature','MinimumTemperature','MaximumRelativeHumidity','MinimumRelativeHumidity','Average10m WindSpeed','SolarRadiation']
    with open(filename,'r') as f:
        filedata = f.read()
        try:
            table_data = '\n'.join(filedata.split('\n')[13:-1]) 
        except:
            print('error')
            return 1
    #create pandas csv
    csv = pd.read_csv(io.StringIO(table_data),header=None,dtype=str)
    csv.columns = csv_header
    csv.replace(' ',np.nan,inplace=True)
    return csv
    
#TODO VALIDATOR?
#TODO schema

# find max temps over a threshold
# input: threshold
