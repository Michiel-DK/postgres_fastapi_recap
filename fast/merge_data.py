import pandas as pd
import os

def get_data():
    """Function to merge dataframes into one"""
        
    merge_ls = []

    #get path
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'raw_data')

    for city in os.listdir(path):
        
        if city != 'merged.csv':
        
            #read csv + rename price
            city_df = pd.read_csv(f"{os.path.join(path, city)}", index_col=0).rename(columns={'realSum':'room_price', 'guest_satisfaction_overall':'satisfaction'})
            
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
    
    print(merged_df.head())
    
    #save merged file to correct directory
    merged_df.to_csv(os.path.join(path, 'merged.csv'))
    
if __name__ == '__main__':
    get_data()