import pandas as pd
import io
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

df = pd.read_csv('sample_data.csv')

df['city'] = ''
df['state'] = ''
df['country'] = ''
def city_state_country(index):
    coord = f"{df.iloc[index]['lat']}, {df.iloc[index]['lon']}"
    location = geolocator.reverse(coord, exactly_one=True)
    print(location)
    if location != None:
        print("if")
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        df.at[index, 'city'] = city
        df.at[index, 'state'] = state
        df.at[index, 'country'] = country
        # print(city, state, country)
#         df.iloc[index]['city'] = city
#         df.iloc[index]['state'] = state
#         df.iloc[index]['country'] = country
    else:
        print("else")
        df.at[index, 'city'] ="drop"
#         df.iloc[index]['city'] = "drop"
    
for index, row in df.iterrows():
    # if(index==10):
    #     break
    city_state_country(index)

df = df.drop(df[df['city']=="drop"].index)

print("df: ",df)  
# df = df.apply(city_state_country, axis=1)