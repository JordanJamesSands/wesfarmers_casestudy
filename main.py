import io, datetime, pandas as pd, numpy as np

#TODO VALIDATOR?
#TODO schema
#TODO move csv_header from out of fn

#Reads all available csv files for the relevant Weather Station
#input:
#   state: State of weather station
#   location: Weather Station_Name
#   start_str: start date(str) <YYYYMM>
#   end_str: end date(str) <YYYYMM>
#output: Pandas dataframe containing all available data in csv tables
def load_data(state,location,start_str='200901',end_str='202109'):
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


#Reads a single csv file
#input:
    #filename: path to file for which data is to be parsed
#output: Pandas datarame containing data from <filename>
def load_csv(filename):
    csv_header = ['Station_Name','Date','Evapo-Transpiration','Rain','PanEvaporation','MaximumTemperature','MinimumTemperature','MaximumRelativeHumidity','MinimumRelativeHumidity','Average10m WindSpeed','SolarRadiation']
    try:
        with open(filename,'r') as f:
            filedata = f.read()
            try:
                table_data = '\n'.join(filedata.split('\n')[13:-1]) 
            except:
                raise ValueError('CSV file not readable: {}'.format(filename))
    except:
        print('File does not exist: {}'.format(filename))
        return pd.DataFrame(columns = csv_header)
    #create pandas csv
    csv = pd.read_csv(io.StringIO(table_data),header=None,dtype=str,date_parser=date_parse,parse_dates=[1])
    csv.columns = csv_header
    csv.replace(' ',np.nan,inplace=True)
    csv = csv.astype(
        dtype = {
            'Station_Name':str,
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
    
#parse function
#input:
    #value contained in the date column of the csv file
#output: Parsed datetime type value
def date_parse(val):
    return datetime.datetime.strptime(val,'%d/%m/%Y')

#Does basic aggregation to compute number of days above a temperature threshold
#Input:
    #weather_table: Pandas dataframe containing all table data relevant to a weather station
    # temp_threshold: Temperature threshold for which number of days with MaxTemperature above is to be calculated
#output: pandas dataframe containing the summarised temperature data
def report_output(weather_table,temp_threshold):
    #create tmp for compute
    tmp = weather_table.copy()
    tmp['Year'] = tmp.Date.apply(lambda x: x.year)
    output = tmp[tmp['MaximumTemperature'] > temp_threshold].groupby(['Station_Name','Year']).agg('count')[['index']]
    output.columns = ['count']
    print(output.to_csv())
    return output

#Generate a MaxTemperature report given a weather station
#input: 
    #temp_threshold: Temperature threshold for which number of days with MaxTemperature above is to be calculated
    #state: State of weather station
    #location: Weather Station_Name  
#output: pandas dataframe containing the summarised temperature data
def generate_report(temp_threshold,state,location):
    weather_table = load_data(state=state,location=location,start_str='200901',end_str='202109')
    return report_output(weather_table=weather_table,temp_threshold=temp_threshold)

def generate_summary_report():
    #latlons
    #-------
    #bunnings notting hill: 
        #-37.9003340275206, 145.12698915589579
        #nearest station: MOORABBIN AIRPORT, VIC
    # officeworks geelong: 
        #-38.14841478301936, 144.36390415590225
        #nearest station: BREAKWATER (GEELONG RACECOURSE), VIC
    # Kmart Belmont: 
        #-31.96532953131573, 115.93558156924325
        #nearest station: PERTH AIRPORT, WA
    locations = [
        ('vic','moorabbin_airport'),
        ('vic','breakwater_(geelong_racecourse)'),
        ('wa','perth_airport')
    ]
    report_list = []
    for loc in locations:
        report = generate_report(35,*loc)
        report_list.append(report)
    print('Final Output')
    pandas_report = pd.concat(report_list)
    report_csv = pandas_report.to_csv()
    print(report_csv)
    timenow = datetime.datetime.now()
    timenow_str = datetime.datetime.strftime(timenow,'%Y%m%d-%H%M%S')
    with open('output/Temperature_Report-{}.csv'.format(timenow_str),'w',newline='') as f:
        f.write(report_csv)
    return pandas_report.reset_index()





