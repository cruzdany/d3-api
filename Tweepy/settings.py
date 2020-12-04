#Settings for preparing the DB.

#Tracking the words

TRACK_WORDS = ['Coronavirus','Covid19','covid','covid19','coronavirus','Covid-19','covid-19','Covid']
#Stored in the table
TABLE_NAME = "Coronavirus"
#With the next columns
TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
            polarity INT, subjectivity INT, user_created_at VARCHAR(255), user_location VARCHAR(255), \
            user_description VARCHAR(255), user_followers_count INT, longitude DOUBLE, latitude DOUBLE, \
            retweet_count INT, favorite_count INT"
