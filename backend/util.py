# utility functions / Pranay

def generate_recommendations(name, restaurants):
    # print(restaurants[0])
    selected_restaurant = None
    name_found = False
    recommended_restaurants = []
    for r in restaurants:
        if r['name'] == name:
            selected_restaurant = r
            name_found = True
            break
    if name_found == False:
        recommended_restaurants.append('Invalid Input')
        return recommended_restaurants
    else:
        pass
    for i in restaurants:
        if selected_restaurant['name'] == i['name']:
            continue
        else:
            if len(recommended_restaurants) > 4:
                return recommended_restaurants
            set1 = set(i['categories'])
            set2 = set(selected_restaurant['categories'])
            common_elements = set1.intersection(set2)
        if len(common_elements) > 0:
            recommended_restaurants.append(i)
        else:
            pass
    return recommended_restaurants
