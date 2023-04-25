# utility functions / Pranay & James

# data description:

#       restuarants is a list of dictionaries

# keys of restuarants are:
    # restuarant = {
    #     "business_id": "string",
    #     "name": "string",
    #     "address": "string",
    #     "city": "string",
    #     "state": "string",
    #     "postal_code": "string",
    #     "latitude": "string",
    #     "longitude": "string",
    #     "stars": "string",
    #     "review_count": "string",
    #     "is_open": "string",
    #     "attributes": "string",
    #     "categories": "string",
    #     "hours": "string"
# }


# this function takes in a list of restaurant names and the complete set of restaurants 
# and returns a list of recommended restaurants
# 
# note that the input restaurant names are not necessarily in the list of all restaurants, so check for that
# 
# the input restuarants are a list of dictionaries, the definition inside is commented out above

# def generate_recommendations(restaurant_names, restaurants):

#     # PLEASE WRITE YOUR CODE HERE

#     # the dummy version always tells you ["McDonald's", 'Cafe Baladi', 'Chick-fil-A']
#     return restaurants[0:3]


#JOANNAS GENERATE_RECOMMENDATIONS
def generate_recommendations(restaurant_names, restaurants):

    # PLEASE WRITE YOUR CODE HERE
    recommended_restaurants = []
    for restaurant_name in restaurant_names:
        for restaurant in restaurants:
            if restaurant_name.lower() in restaurant["name"].lower():
                recommended_restaurants.append({
                    "name": restaurant["name"],
                    "latitude": float(restaurant["latitude"]),
                    "longitude": float(restaurant["longitude"])
                })
                break
    return recommended_restaurants






# this is previously written code keeping for reference, by pranay.

# def generate_recommendations(name, restaurants):
#     # print(restaurants[0])
#     selected_restaurant = None
#     name_found = False
#     recommended_restaurants = []
#     for r in restaurants:
#         if r['name'] == name:
#             selected_restaurant = r
#             name_found = True
#             break
#     if name_found == False:
#         recommended_restaurants.append('Invalid Input')
#         return recommended_restaurants
#     else:
#         pass
#     for i in restaurants:
#         if selected_restaurant['name'] == i['name']:
#             continue
#         else:
#             if len(recommended_restaurants) > 4:
#                 return recommended_restaurants
#             set1 = set(i['categories'])
#             set2 = set(selected_restaurant['categories'])
#             common_elements = set1.intersection(set2)
#         if len(common_elements) > 0:
#             recommended_restaurants.append(i)
#         else:
#             pass
#     return recommended_restaurants