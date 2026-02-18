def recommend_crop_by_geotag(latitude, longitude, terrain):
    """
    Recommend crop based on geo tagging inputs: latitude, longitude, and terrain.
    Uses a sample dataset to find the closest match and recommend a crop.
    """
    terrain = terrain.strip().lower()

    # Sample dataset of latitude, longitude, terrain, and associated crop
    sample_data = [
        {'latitude': 17.3850, 'longitude': 78.4867, 'terrain': 'plain', 'crop': 'Wheat'},
        {'latitude': 18.1124, 'longitude': 79.0193, 'terrain': 'hilly', 'crop': 'Tea'},
        {'latitude': 16.5062, 'longitude': 80.6480, 'terrain': 'coastal', 'crop': 'Rice'},
        {'latitude': 17.6868, 'longitude': 83.2185, 'terrain': 'plain', 'crop': 'Maize'},
        {'latitude': 15.8281, 'longitude': 78.0373, 'terrain': 'hilly', 'crop': 'Coffee'},
    ]

    # Find the closest match based on terrain and approximate latitude/longitude
    def distance(lat1, lon1, lat2, lon2):
        return abs(lat1 - lat2) + abs(lon1 - lon2)

    closest_entry = None
    min_distance = float('inf')
    for entry in sample_data:
        if entry['terrain'] == terrain:
            dist = distance(latitude, longitude, entry['latitude'], entry['longitude'])
            if dist < min_distance:
                min_distance = dist
                closest_entry = entry

    if closest_entry:
        recommended_crop = closest_entry['crop']
    else:
        recommended_crop = 'Maize'  # Default crop if no match found

    return {
        'recommended_crop': recommended_crop,
        'latitude': latitude,
        'longitude': longitude,
        'terrain': terrain
    }   


# import math

# def recommend_crop_by_geotag(latitude, longitude, terrain):
#     """
#     Recommend crop based on geo tagging inputs: latitude, longitude, and terrain.
#     Uses a sample dataset to find the closest match and recommend a crop.
#     """
#     terrain = terrain.strip().lower()

#     # Sample dataset of latitude, longitude, terrain, and associated crop
#     # This dataset can be expanded and made more robust for a real application
#     sample_data = [
    #     {'latitude': 17.3850, 'longitude': 78.4867, 'terrain': 'plain', 'crop': 'Wheat'},
    #     {'latitude': 18.1124, 'longitude': 79.0193, 'terrain': 'hilly', 'crop': 'Tea'},
    #     {'latitude': 16.5062, 'longitude': 80.6480, 'terrain': 'coastal', 'crop': 'Rice'},
    #     {'latitude': 17.6868, 'longitude': 83.2185, 'terrain': 'plain', 'crop': 'Maize'},
    #     {'latitude': 15.8281, 'longitude': 78.0373, 'terrain': 'hilly', 'crop': 'Coffee'},
    #     # Adding more diverse data points for better recommendations
    #     {'latitude': 17.0000, 'longitude': 81.0000, 'terrain': 'plain', 'crop': 'Sugarcane'},
    #     {'latitude': 13.0827, 'longitude': 80.2707, 'terrain': 'coastal', 'crop': 'Coconut'}, # Chennai
    #     {'latitude': 28.7041, 'longitude': 77.1025, 'terrain': 'plain', 'crop': 'Mustard'}, # Delhi
    #     {'latitude': 27.1751, 'longitude': 78.0421, 'terrain': 'plain', 'crop': 'Potatoes'}, # Agra
    #     {'latitude': 11.0168, 'longitude': 76.9558, 'terrain': 'hilly', 'crop': 'Spices'}, # Coimbatore nearby hilly
    # ]

    # Find the closest match based on terrain and approximate latitude/longitude
    # Using Euclidean distance as a simple proximity measure
#     def euclidean_distance(lat1, lon1, lat2, lon2):
#         return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

#     closest_entry = None
#     min_distance = float('inf')

#     # Filter by terrain first, then find the closest geographical match
#     potential_matches = [entry for entry in sample_data if entry['terrain'] == terrain]

#     if not potential_matches:
#         # If no entries match the terrain, try to find the closest geographically
#         # regardless of terrain, or fall back to a default.
#         # For simplicity, we'll just assign a default if no terrain matches
#         # or find closest geographical match if no terrain match.
#         # This part could be improved with more sophisticated logic.
#         for entry in sample_data: # Search all data if terrain not found
#             dist = euclidean_distance(latitude, longitude, entry['latitude'], entry['longitude'])
#             if dist < min_distance:
#                 min_distance = dist
#                 closest_entry = entry
#         if closest_entry:
#             # If a geo match is found without terrain match, note it.
#             # You might want to adjust the default or add a "best effort" message.
#             recommended_crop = closest_entry['crop']
#             # print(f"DEBUG: No exact terrain match found, best geo match: {recommended_crop}")
#         else:
#             recommended_crop = 'Maize' # Fallback if dataset is empty or no match
#     else:
#         # Find the closest geographical match within the specified terrain
#         for entry in potential_matches:
#             dist = euclidean_distance(latitude, longitude, entry['latitude'], entry['longitude'])
#             if dist < min_distance:
#                 min_distance = dist
#                 closest_entry = entry
        
#         if closest_entry:
#             recommended_crop = closest_entry['crop']
#         else:
#             # This case should ideally not be hit if potential_matches is not empty
#             recommended_crop = 'Maize' # Fallback

#     return {
#         'recommended_crop': recommended_crop,
#         'latitude': latitude,
#         'longitude': longitude,
#         'terrain': terrain
#     }

# # --- Example Usage ---
# if __name__ == "__main__":
#     print("--- Testing recommend_crop_by_geotag function ---")

#     # Test Case 1: Plain terrain, near existing data (Hyderabad, Telangana)
#     lat1, lon1, terr1 = 17.4000, 78.4900, "plain"
#     result1 = recommend_crop_by_geotag(lat1, lon1, terr1)
#     print(f"\nInput: Lat={lat1}, Lon={lon1}, Terrain='{terr1}'")
#     print(f"Recommended Crop: {result1['recommended_crop']}")
#     print(f"Full Result: {result1}")
#     # Expected: Likely Wheat or Maize, depending on proximity logic

    # Test Case 2: Hilly terrain, near existing data (Warangal, Telangana)
    # lat2, lon2, terr2 = 18.0000, 79.5000, "hilly"
    # result2 = recommend_crop_by_geotag(lat2, lon2, terr2)
    # print(f"\nInput: Lat={lat2}, Lon={lon2}, Terrain='{terr2}'")
    # print(f"Recommended Crop: {result2['recommended_crop']}")
    # print(f"Full Result: {result2}")
    # Expected: Likely Tea or Coffee

    # Test Case 3: Coastal terrain, near existing data (Visakhapatnam, Andhra Pradesh)
    # lat3, lon3, terr3 = 17.7000, 83.3000, "coastal"
    # result3 = recommend_crop_by_geotag(lat3, lon3, terr3)
    # print(f"\nInput: Lat={lat3}, Lon={lon3}, Terrain='{terr3}'")
    # print(f"Recommended Crop: {result3['recommended_crop']}")
    # print(f"Full Result: {result3}")
    # Expected: Likely Rice or Coconut

    # Test Case 4: A new location, slightly different terrain phrasing
    # lat4, lon4, terr4 = 17.5, 78.8, "PlaiN " # Testing case-insensitivity and stripping
    # result4 = recommend_crop_by_geotag(lat4, lon4, terr4)
    # print(f"\nInput: Lat={lat4}, Lon={lon4}, Terrain='{terr4}'")
    # print(f"Recommended Crop: {result4['recommended_crop']}")
    # print(f"Full Result: {result4}")

    # Test Case 5: A location far from existing sample data for a specific terrain
    # (Example: Northern India, but looking for a "hilly" crop in a less-represented hilly region)
    # lat5, lon5, terr5 = 30.0, 77.0, "hilly"
    # result5 = recommend_crop_by_geotag(lat5, lon5, terr5)
    # print(f"\nInput: Lat={lat5}, Lon={lon5}, Terrain='{terr5}'")
    # print(f"Recommended Crop: {result5['recommended_crop']}")
    # print(f"Full Result: {result5}")
    # Expected: Will try to find the closest 'hilly' region, might be Coffee/Tea

    # Test Case 6: Terrain not explicitly in the dataset (should fall back to default logic)
    # lat6, lon6, terr6 = 20.0, 75.0, "desert"
    # result6 = recommend_crop_by_geotag(lat6, lon6, terr6)
    # print(f"\nInput: Lat={lat6}, Lon={lon6}, Terrain='{terr6}'")
    # print(f"Recommended Crop: {result6['recommended_crop']}")
    # print(f"Full Result: {result6}")
    # Expected: Will fall back to Maize or the geographically closest in the whole dataset

import math

def recommend_crop_by_geotag(latitude, longitude, terrain):
    """
    Recommend a crop based on geotagging: latitude, longitude, and terrain.
    Uses a predefined sample dataset for matching.
    """
    terrain = terrain.strip().lower()

    # Sample dataset (latitude, longitude, terrain, recommended crop)
    sample_data = [
        {'latitude': 17.3850, 'longitude': 78.4867, 'terrain': 'plain', 'crop': 'Wheat'},
        {'latitude': 18.1124, 'longitude': 79.0193, 'terrain': 'hilly', 'crop': 'Tea'},
        {'latitude': 16.5062, 'longitude': 80.6480, 'terrain': 'coastal', 'crop': 'Rice'},
        {'latitude': 17.6868, 'longitude': 83.2185, 'terrain': 'plain', 'crop': 'Maize'},
        {'latitude': 15.8281, 'longitude': 78.0373, 'terrain': 'hilly', 'crop': 'Coffee'},
        {'latitude': 17.0000, 'longitude': 81.0000, 'terrain': 'plain', 'crop': 'Sugarcane'},
        {'latitude': 13.0827, 'longitude': 80.2707, 'terrain': 'coastal', 'crop': 'Coconut'},
        {'latitude': 28.7041, 'longitude': 77.1025, 'terrain': 'plain', 'crop': 'Mustard'},
        {'latitude': 27.1751, 'longitude': 78.0421, 'terrain': 'plain', 'crop': 'Potatoes'},
        {'latitude': 11.0168, 'longitude': 76.9558, 'terrain': 'hilly', 'crop': 'Spices'},
    ]

    def euclidean_distance(lat1, lon1, lat2, lon2):
        return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

    potential_matches = [entry for entry in sample_data if entry['terrain'] == terrain]
    fallback_matches = sample_data  # in case terrain doesn't match

    closest_entry = None
    min_distance = float('inf')

    # Use appropriate dataset depending on whether terrain matched
    search_space = potential_matches if potential_matches else fallback_matches

    for entry in search_space:
        dist = euclidean_distance(latitude, longitude, entry['latitude'], entry['longitude'])
        if dist < min_distance:
            min_distance = dist
            closest_entry = entry

    recommended_crop = closest_entry['crop'] if closest_entry else 'Maize'

    return {
        'recommended_crop': recommended_crop,
        'latitude': latitude,
        'longitude': longitude,
        'terrain': terrain,
        'note': 'Based on best match in terrain' if potential_matches else 'Fallback to best geographic match'
    }

# --- Example Test Cases ---
if __name__ == "__main__":
    test_cases = [
        (17.4000, 78.4900, "plain"),
        (18.0000, 79.5000, "hilly"),
        (17.7000, 83.3000, "coastal"),
        (17.5, 78.8, "PlaiN "),  # case-insensitive and strip test
        (30.0, 77.0, "hilly"),  # far location
        (20.0, 75.0, "desert")  # terrain not in dataset
    ]

    print("--- Geo-Tagging Crop Recommendation ---")
    for lat, lon, terr in test_cases:
        result = recommend_crop_by_geotag(lat, lon, terr)
        print(f"\nInput => Latitude: {lat}, Longitude: {lon}, Terrain: '{terr}'")
        print(f"Recommended Crop: {result['recommended_crop']}")
        print(f"Result Detail: {result}")
