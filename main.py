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
    csv = pd.read_csv(io.StringIO(table_data),header=None,dtype=str,date_parser=date_parse,parse_dates=[1])
    csv.columns = csv_header
    csv.replace(' ',np.nan,inplace=True)
    csv = csv.astype(
        dtype = {
            'Station Name':str,
            'Evapo-Transpiration':float,
            'Rain':float,
            'PanEvaporation':float,
            'MaximumTemperature':float,
            'MinimumTemperature':float,
            'MaximumRelativeHumidity':float,
            'MinimumRelativeHumidity':float,
            'Average10m WindSpeed':float,
            'SolarRadiation':float
        }
    )
    return csv
    
def date_parse(val):
    return datetime.datetime.strptime(val,'%d/%m/%Y')

def report_output(weather_table,temp_threshold):
    #create tmp for compute
    tmp = weather_table.copy()
    tmp['Year'] = out.Date.apply(lambda x: x.year)
    output = tmp[tmp['MaximumTemperature'] > temp_threshold].groupby(['Station Name','Year']).agg('count')[['index']]
    output.columns = ['count']
    return print(output.to_csv())


def generate_report(temp_threshold,state,location):
    weather_table = load_data(state=state,location=location,start_str='200901',end_str='202109')
    return report_output(weather_table=weather_table,temp_threshold=temp_threshold)

    
generate_report(35,'nsw','albury_airport')

#TODO VALIDATOR?
#TODO schema
#TODO move csv_header from out of fn
filename = 'data/tables/vic/east_sale/east_sale-201709.csv'
