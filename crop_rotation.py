def suggest_rotation(current_crop):
    rotation_map = {
        'Rice': 'Legumes',
        'Wheat': 'Maize',
        'Tomato': 'Onion',
        'Groundnut': 'Cotton'
    }
    return rotation_map.get(current_crop, 'Try pulses or green manure crop')
