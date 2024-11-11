
import requests
import json
from datetime import datetime, timedelta
import pandas as pd 
import time 
import os 



class AQI_EXT:

	def __init__(self,country):
		self.country = country
		self.locations = self.get_locations_id()


	def get_loc_by_lat_long(self,lat,lon):	
		url = "https://api.openaq.org/v1/locations"
		headers = {
		    "X-API-Key": "60adf035dbcd3fab3e446d403311bac20657cd4e9d1f5334fa247937e2b383b6"  
		}
		params = {
		    "limit": 10000,
		    'radius':25000,
		    'coordinates':"{},{}".format(lat,lon)
		    
		    
		   
	       
	       

	        

		}
		response = requests.get(url, headers=headers, params=params)
		# Check if the request was successful
		if response.status_code == 200:
		    data = response.json()
		    result = data['results']
		    df = pd.DataFrame(result)
		    df.to_csv('coord_loc_{}_{}.csv'.format(lat,lon))
		    return df
		    
		
		


	def get_mexico_country(self):
		url = "https://api.openaq.org/v1/countries"
		headers = {
		    "X-API-Key": "60adf035dbcd3fab3e446d403311bac20657cd4e9d1f5334fa247937e2b383b6"  
		}
		params = {
		    
		    "limit": 200,
		    'offset':0,
		    'sort':'asc'
		}
		response = requests.get(url, headers=headers, params=params)
		if response.status_code == 200:
		    data = response.json()
		    result = data['results']
		    for i in result:
		    	if i['name'].lower()=='mexico':
		    		return i
	



	def get_locations_id(self):
		url = "https://api.openaq.org/v2/locations"
		headers = {
		    "X-API-Key": "60adf035dbcd3fab3e446d403311bac20657cd4e9d1f5334fa247937e2b383b6"  
		}
		params = {
		    "limit": 10000,
		    'country':self.country,
		    "date_from": datetime(2020,11,5),
	        "date_to": datetime(2024,11,7),     
		}
		response = requests.get(url, headers=headers, params=params)
		# Check if the request was successful
		if response.status_code == 200:
		    data = response.json()
		    result = data['results']
		    df = pd.DataFrame(result)
		    return df['id'].drop_duplicates().tolist()





	def get_measure_by_loc(self,measure,start,end,loc):
    	
		url = "https://api.openaq.org/v2/measurements"
		headers = {
		    "X-API-Key": "60adf035dbcd3fab3e446d403311bac20657cd4e9d1f5334fa247937e2b383b6"  
		}
		params = {
		    "limit": 10000,
		    
		    "date_from": start,
	        "date_to": end,
	        'parameter':"{}".format(measure),
	        'location_id':loc

	        

		}
		response = requests.get(url, headers=headers, params=params)
		# Check if the request was successful
		if response.status_code == 200:
		    data = response.json()
		    result = data['results']
		    df = pd.DataFrame(result)

		    if df.shape[0]==0:
		    	cols = ['locationId', 'location', 'parameter', 'value', 'date', 'unit','coordinates', 'country', 'city', 'isMobile', 'isAnalysis', 'entity','sensorType']
		    	for i in cols:
		    		df[i] = [0,]
		    return df



    




 

    
###location ids which are in a 25 km radius from the mexico city lat lon. Each coordinate was used to further apply a 25 km radius of search again. Leading to an approx 50km radius
##from mexico city lat lon 
lat_lon = [{'latitude': 19.325099999999996, 'longitude': -99.2041},
{'latitude': 19.473691944444, 'longitude': -99.046175833333},
{'latitude': 19.326388888889, 'longitude': -99.17611111111101},
{'latitude': 19.384444444444, 'longitude': -99.11777777777799},
{'latitude': 19.325277777778, 'longitude': -99.204166666667},
{'latitude': 19.404, 'longitude': -99.202722222222},
{'latitude': 19.304444444443998, 'longitude': -99.10388888888899},
{'latitude': 19.533055555556, 'longitude': -99.030555555556},
{'latitude': 19.5259, 'longitude': -99.0824},
{'latitude': 19.5329, 'longitude': -99.0303},
{'latitude': 19.3653, 'longitude': -99.2917},
{'latitude': 19.4604, 'longitude': -98.9028},
{'latitude': 19.482499999999998, 'longitude': -99.24361111111101},
{'latitude': 19.4246, 'longitude': -99.1195},
{'latitude': 19.3502, 'longitude': -99.1571},
{'latitude': 19.365555555556, 'longitude': -99.291944444444},
{'latitude': 19.5787, 'longitude': -99.0396},
{'latitude': 19.360833333333, 'longitude': -99.07388888888899},
{'latitude': 19.272222222222, 'longitude': -99.207777777778},
{'latitude': 19.393888888889, 'longitude': -99.02833333333298},
{'latitude': 19.3844, 'longitude': -99.1176},
{'latitude': 19.3575, 'longitude': -99.263055555556},
{'latitude': 19.411666666667, 'longitude': -99.152222222222},
{'latitude': 19.535, 'longitude': -99.11777777777802},
{'latitude': 19.526111111110996, 'longitude': -99.0825},
{'latitude': 19.345609999999997, 'longitude': -99.009380833333},
{'latitude': 19.577222222222, 'longitude': -99.254166666667},
{'latitude': 19.578888888889, 'longitude': -99.039722222222},
{'latitude': 19.334, 'longitude': -99.182},
{'latitude': 19.577, 'longitude': -99.2542},
{'latitude': 19.529, 'longitude': -99.2045},
{'latitude': 19.529166666667, 'longitude': -99.204722222222},
{'latitude': 19.3044, 'longitude': -99.0738},
{'latitude': 19.602777777778, 'longitude': -99.177222222222},
{'latitude': 19.4824, 'longitude': -99.2435},
{'latitude': 19.3919, 'longitude': -99.0281},
{'latitude': 19.424722222222, 'longitude': -99.119722222222},
{'latitude': 19.371666666667, 'longitude': -99.159166666667},
{'latitude': 19.3573, 'longitude': -99.26279999999998},
{'latitude': 19.3607, 'longitude': -99.0738},
{'latitude': 19.430045776952728, 'longitude': -99.18183463386997},
{'latitude': 19.5347, 'longitude': -99.1177},
{'latitude': 19.468611111111, 'longitude': -99.17},
{'latitude': 19.2464, 'longitude': -99.01},
{'latitude': 19.4684, 'longitude': -99.1697},
{'latitude': 19.246666666667, 'longitude': -99.01083333333301},
{'latitude': 19.6025, 'longitude': -99.1771},
{'latitude': 19.482777777778, 'longitude': -99.094722222222},
{'latitude': 19.4525, 'longitude': -99.086}]



    
	  
mexico_data = AQI_EXT('MX')
print(mexico_data.locations)
print(mexico_data.get_loc_by_lat_long(19.432608,-99.133209)) ##mexico city

for i in lat_lon[0:1]:
	lat = round(i['latitude'],6)
	lon = round(i['longitude'],6)
	df_merge = mexico_data.get_loc_by_lat_long(lat, lon)


for i in lat_lon[1:]:
	lat = round(i['latitude'],6)
	lon = round(i['longitude'],6)
	df_ext = mexico_data.get_loc_by_lat_long(lat, lon)
	df_merge = pd.concat([df_merge,df_ext],axis=0)



df_merge.to_csv('lat_lon_combo.csv') #####use this to decipher which location_ids cater to which pollutants, only those location_ids are in this df which are within 
# a 50km radius from the lat long of mexico city






err = []



###these are the location ids which have recorded at some point of time the pollutants on the LHS

err_pm25 = [576,7998,10534,10658,10735,9759,1791,1986,10804,480393,8000,10794,1134,10802,1285351,1659,10762,926,2054,10748,10860,348,1604,1640325,10722,1739,10632,2006,10699,1367,2020] ####locs with pm25 
err_pm10 = [576,235230,10658,10735,1991,10558,1791,10804,480393,1090,10794,1134,1659,10762,2056,10748,10860,348,1604,1640325,10722,677,1739,10759,10632,10699,1367,2020,1237,1505,759,222284,10706,918,1809,10661,795,3151153]
err_so2 = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,223434,10804,480393,8000,1090,10794,1134,10840,10802,1659,10762,926,2056,2054,10748,348,1604,1271,10722,677,1739,10759,2006,10699,1367,2020,1830,1578,494940,1237,10648,1505,759,222284,10706,918,1809,222494,10661,795,3151153]
err_o3 = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,223434,10804,480393,8000,1090,10794,1134,10840,10802,1659,10762,926,2056,2054,10748,10860,348,1604,1271,10722,677,1739,10759,10632,2006,10699,1367,2020,1830,1578,494940,1237,10648,235228,1505,759,222284,10706,918,1809,222494,10661,795,3151153]
err_co = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,10804,480393,8000,1090,10794,1134,10840,10802,1659,10762,926,2056,2054,10748,10860,348,1604,1271,10722,677,1739,10759,2006,10699,1367,2020,1830,1578,494940,1237,10648,1505,759,222284,10706,918,1809,222494,10661,3151153]
err_no = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,223434,10804,480393,8000,1090,10794,1134,10802,1659,10762,926,2056,2054,10748,10860,348,1604,10722,677,1739,10759,10632,2006,10699,1367,2020,1830,1578,494940,1237,10648,1505,759,222284,10706,918,1809,222494,10661,795,3151153]
err_nox = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,223434,10804,480393,8000,1090,10794,1134,10802,1659,10762,926,2056,2054,10748,10860,348,1604,10722,677,1739,10759,10632,2006,10699,1367,2020,1830,1578,494940,1237,10648,1505,759,222284,10706,918,1809,222494,10661,795,3151153]
err_no2 = [576,7998,10534,235230,10658,10735,9759,1991,10558,1791,1986,223434,10804,480393,8000,1090,10794,1134,10802,1659,10762,926,2056,2054,10748,10860,348,1604,10722,677,1739,10759,10632,2006,10699,1367,2020,1830,1578,494940,1237,10648,1505,759,222284,10706,918,1809,222494,10661,795,3151153]



def get_data(measure,locations):
	for k in locations:
		try:
			df_merge = mexico_data.get_measure_by_loc(measure,datetime(2019,11,30),datetime(2019,12,31),k)
			for i in [2020,2021,2022,2023,2024]:
				for j in [1,2,3,4,5,6,7,8,9,10,11,12]:
					start_dt = datetime(i,j,1) - timedelta(days=1)
					if j+1==13:
						end_j=1
						end_i = i+1
					else:
						end_j=j+1
						end_i = i
					end_dt = datetime(end_i,end_j,1) -  timedelta(days=1)
					df_ext = mexico_data.get_measure_by_loc(measure,start_dt,end_dt,k)
					time.sleep(3)
					df_merge = pd.concat([df_merge,df_ext],axis=0)
					print(k,df_merge.shape,start_dt,end_dt)
			df_merge.to_csv('{}_{}.csv'.format(measure,k))
			if np.sum(df_merge['locationId'])==0:
				err.append(k)
			time.sleep(10)
		except:
			err.append(k)
	print(err)


print(get_data(measure='pm25',locations=err_pm25))
print(get_data(measure='pm10',locations=err_pm10))
print(get_data(measure='so2',locations=err_so2))
print(get_data(measure='o3',locations=err_o3))
print(get_data(measure='co',locations=err_co))
print(get_data(measure='no',locations=err_no))
print(get_data(measure='nox',locations=err_nox))
print(get_data(measure='no2',locations=err_no2))





def make_single_frame():
	files = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'aqi_files'))
	print(files)

	for i in files[0:1]:
		file = os.path.dirname(os.path.abspath(__file__))
		file = os.path.join(file,'aqi_files')
		file = os.path.join(file,i)
		df_merge = pd.read_csv(file, encoding='utf-8')

	for i in files[1:]:
		file = os.path.dirname(os.path.abspath(__file__))
		file = os.path.join(file,'aqi_files')
		file = os.path.join(file,i)
		df_val = pd.read_csv(file, encoding='utf-8')
		df_merge = pd.concat([df_merge,df_val],axis=0)
		print(df_merge.shape)

	print(df_merge.shape)
	df_merge = df_merge[(df_merge['locationId']!=0)]
	


	df_merge = df_merge.sort_values(by=['locationId','parameter','date'])
	print(df_merge.shape)
	print(df_merge.head(100))
	df_merge.to_csv('mexico_stations_pollutants.csv')
		
		


print(make_single_frame())








	    		
