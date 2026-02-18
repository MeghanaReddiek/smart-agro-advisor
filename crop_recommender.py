# import pandas as pd
# import os

# MARKET_DEMAND_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'market_demand.csv')

# def load_market_demand_data():
#     import logging
#     logging.info(f"Loading market demand data from: {MARKET_DEMAND_FILE}")
#     if os.path.exists(MARKET_DEMAND_FILE):
#         try:
#             df = pd.read_csv(MARKET_DEMAND_FILE)
#             logging.info(f"Market demand data loaded successfully with {len(df)} records")
#             logging.info(f"Dataset preview:\n{df.head()}")
#             return df
#         except Exception as e:
#             logging.error(f"Error loading market demand data: {e}")
#             return None
#     else:
#         logging.error(f"Market demand file not found at path: {MARKET_DEMAND_FILE}")
#         return None

# import logging

# def recommend_crop(data):
#     district = data.get('location', '').strip().lower()
#     season = data.get('season', '').strip().lower()
#     nearest_market = data.get('nearest_market', '').strip().lower()

#     df = load_market_demand_data()
#     if df is not None:
#         logging.info(f"Market demand dataset loaded with {len(df)} records")
#         # Log unique values for debugging
#         logging.info(f"Unique Districts: {df['District'].unique()}")
#         logging.info(f"Unique Seasons: {df['Season'].unique()}")
#         logging.info(f"Unique Nearest_Markets: {df['Nearest_Market'].unique()}")

#         # Normalize dataset columns for comparison
#         df['District'] = df['District'].str.strip().str.lower()
#         df['Season'] = df['Season'].str.strip().str.lower()
#         df['Nearest_Market'] = df['Nearest_Market'].str.strip().str.lower()

#         filtered = df[
#             (df['District'] == district) &
#             (df['Season'] == season) &
#             (df['Nearest_Market'] == nearest_market)
#         ]
#         logging.info(f"Filtered records count: {len(filtered)}")
#         if not filtered.empty:
#             crop = filtered.iloc[0]['Preferred_Crop']
#             price_trend = filtered.iloc[0]['Market_Trend']
#             logging.info(f"Recommendation: crop={crop}, price_trend={price_trend}")
#             return {'crop': crop, 'price_trend': price_trend}

#     # Fallback logic if no data or no match found
#     price_trend = 'stable'
#     if district in ['dry', 'arid', 'desert']:
#         crop = 'Millet'
#     elif district in ['tropical', 'humid']:
#         crop = 'Rice'
#     else:
#         crop = 'cotton'
#     return {'crop': crop, 'price_trend': price_trend}
# def recommend_crop(data):
#     # Embedded sample dataset with 10 entries
#     market_data = [
#         {'District': 'hyd', 'Season': 'kharif', 'Nearest_Market': 'sangareddy', 'Preferred_Crop': 'Rice', 'Market_Trend': 'rising'},
#         {'District': 'hyd', 'Season': 'rabi', 'Nearest_Market': 'sangareddy', 'Preferred_Crop': 'Wheat', 'Market_Trend': 'stable'},
#         {'District': 'nalgonda', 'Season': 'kharif', 'Nearest_Market': 'miryalaguda', 'Preferred_Crop': 'Cotton', 'Market_Trend': 'rising'},
#         {'District': 'nalgonda', 'Season': 'rabi', 'Nearest_Market': 'miryalaguda', 'Preferred_Crop': 'Bengal Gram', 'Market_Trend': 'falling'},
#         {'District': 'karimnagar', 'Season': 'kharif', 'Nearest_Market': 'jammikunta', 'Preferred_Crop': 'Maize', 'Market_Trend': 'rising'},
#         {'District': 'karimnagar', 'Season': 'rabi', 'Nearest_Market': 'jammikunta', 'Preferred_Crop': 'Sunflower', 'Market_Trend': 'stable'},
#         {'District': 'adilabad', 'Season': 'kharif', 'Nearest_Market': 'mancherial', 'Preferred_Crop': 'Soybean', 'Market_Trend': 'rising'},
#         {'District': 'adilabad', 'Season': 'rabi', 'Nearest_Market': 'mancherial', 'Preferred_Crop': 'Sorghum', 'Market_Trend': 'falling'},
#         {'District': 'khammam', 'Season': 'kharif', 'Nearest_Market': 'kothagudem', 'Preferred_Crop': 'Groundnut', 'Market_Trend': 'rising'},
#         {'District': 'khammam', 'Season': 'rabi', 'Nearest_Market': 'kothagudem', 'Preferred_Crop': 'Sesame', 'Market_Trend': 'stable'},
#     ]

#     # Extract user inputs from the request data
#     district = data.get('location', '').strip().lower()
#     season = data.get('season', '').strip().lower()
#     nearest_market = data.get('nearest_market', '').strip().lower()

#     # Match the record
#     for entry in market_data:
#         if (entry['District'].lower() == district and
#             entry['Season'].lower() == season and
#             entry['Nearest_Market'].lower() == nearest_market):
#             return {
#                 'crop': entry['Preferred_Crop'],
#                 'price_trend': entry['Market_Trend']
#             }

#     # Default recommendation if no match is found
#     return {
#         'crop': 'Maize',
#         'price_trend': 'stable'
#     }
def recommend_crop(data):
    # Embedded Telangana dataset with seasons in English
    market_data = [
        {'District': 'warangal', 'Season': 'rainy', 'Nearest_Market': 'parakal', 'Preferred_Crop': 'Paddy', 'Market_Trend': 'rising'},
        {'District': 'warangal', 'Season': 'winter', 'Nearest_Market': 'parakal', 'Preferred_Crop': 'Chickpea', 'Market_Trend': 'stable'},
        {'District': 'nizamabad', 'Season': 'rainy', 'Nearest_Market': 'armoor', 'Preferred_Crop': 'Turmeric', 'Market_Trend': 'rising'},
        {'District': 'nizamabad', 'Season': 'winter', 'Nearest_Market': 'armoor', 'Preferred_Crop': 'Sorghum', 'Market_Trend': 'falling'},
        {'District': 'medak', 'Season': 'summer', 'Nearest_Market': 'siddipet', 'Preferred_Crop': 'Sunflower', 'Market_Trend': 'stable'},
        {'District': 'suryapet', 'Season': 'rainy', 'Nearest_Market': 'kodad', 'Preferred_Crop': 'Cotton', 'Market_Trend': 'rising'},
        {'District': 'suryapet', 'Season': 'winter', 'Nearest_Market': 'kodad', 'Preferred_Crop': 'Green Gram', 'Market_Trend': 'falling'},
        {'District': 'jagtial', 'Season': 'rainy', 'Nearest_Market': 'korutla', 'Preferred_Crop': 'Maize', 'Market_Trend': 'rising'},
        {'District': 'mahbubnagar', 'Season': 'winter', 'Nearest_Market': 'gadwal', 'Preferred_Crop': 'Groundnut', 'Market_Trend': 'stable'},
        {'District': 'mancherial', 'Season': 'spring', 'Nearest_Market': 'bellampalli', 'Preferred_Crop': 'Sesame', 'Market_Trend': 'stable'},
    ]

    # Extract input data
    district = data.get('location', '').strip().lower()
    season = data.get('season', '').strip().lower()
    nearest_market = data.get('nearest_market', '').strip().lower()

    # Match the data against embedded dataset
    for entry in market_data:
        if (entry['District'].lower() == district and
            entry['Season'].lower() == season and
            entry['Nearest_Market'].lower() == nearest_market):
            return {
                'crop': entry['Preferred_Crop'],
                'price_trend': entry['Market_Trend']
            }

    # Default recommendation if no match found
    return {
        'crop': 'Maize',
        'price_trend': 'stable'
    }
