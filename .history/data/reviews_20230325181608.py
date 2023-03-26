import pandas as pd
import matplotlib.pyplot as plt


import json

# Load the restaurant and business JSON files
with open('../../data/yelp_academic_dataset_review.json', 'r') as f:
    #restaurants = json.load(f)
    reviews = [json.loads(line) for line in f]
    






restaurant = pd.read_csv("yelp_academic_dataset_restaurants.csv")
restaurant_set = set(restaurant['business_id'])

#reviews = pd.read_json("/Users/jameslarson/Desktop/yelp_academic_dataset_review.json",lines=True)

reviews = reviews[:10]

print("reviews done")

print(reviews)

# reviews = reviews[reviews['business_id'].isin(restaurant['business_id'])]
reviews = [review for review in reviews if review['business_id'] in restaurant['business_id'].values]


# store the dataset reviews into a csv file
import csv

# open a file for writing
review_data = open('yelp_academic_dataset_review.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(review_data)

# write the reviews into the file
count = 0
for review in reviews:
    if count == 0:
        header = review.keys()
        csvwriter.writerow(['business_id','stars','useful','funny','cool','text'])
        count += 1

    csvwriter.writerow([review['business_id'], review['stars'], review['useful'], review['funny'], review['cool'], review['text'].replace('\n', ' ')])
    # # write without the line text
    # csvwriter.writerow([ review['business_id'], review['stars'], review['useful'], review['funny'], review['cool']])
    # # write the line text without \n
    # csvwriter.writerow([review['text'].replace('\n', ' ')])



review_data.close()