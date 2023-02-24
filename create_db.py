import pandas as pd
import os

def create_merged_csv():
    """function that merges csv"""
    
    merge_ls = []

    path = 'raw_data/'

    for city in os.listdir(path):
        
        #read csv + rename price
        city_df = pd.read_csv(f"{path + city}", index_col=0).rename(columns={'realSum':'room_price', 'guest_satisfaction_overall':'satisfaction'})
        
        #get city name from path
        city_name = city.split('_')[0]
        
        #add city column
        city_df['city'] = city_name
        
        #creat smaller df
        city_df_small = city_df[['city', 'room_price', 'host_is_superhost', 'bedrooms', 'satisfaction']]
        
        #append to ls
        merge_ls.append(city_df_small)

    #concatenate all df
    merged_df = pd.concat(merge_ls)

    #reset index to generate 'index column'
    merged_df.reset_index(inplace=True,drop=True)
    
    merged_df.to_csv('raw_data/merged.csv')
    
if '__main__' == __name__:
    print('created merged csv under raw_data')
    create_merged_csv()