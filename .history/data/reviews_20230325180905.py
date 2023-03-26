import pandas as pd
import matplotlib.pyplot as plt


import json

# Load the restaurant and business JSON files
with open('/Users/jameslarson/Desktop/yelp_academic_dataset_review.json', 'r') as f:
    #restaurants = json.load(f)
    reviews = [json.loads(line) for line in f]
    






restaurant = pd.read_csv("yelp_academic_dataset_restaurants.csv")
restaurant_set = set(restaurant['business_id'])

#reviews = pd.read_json("/Users/jameslarson/Desktop/yelp_academic_dataset_review.json",lines=True)

reviews = reviews[:10000]

print("reviews done")

# reviews = reviews[reviews['business_id'].isin(restaurant['business_id'])]
reviews = [review for review in reviews if review['business_id'] in restaurant['business_id'].values]


reviews.to_csv('reviews.csv', index = False)
