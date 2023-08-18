#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a list of years and durations
years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]


# In[3]:


movie_dict = {"years": years,"durations": durations}


# In[4]:


# Print and inspect the dictionary
print(movie_dict)


# In[5]:


pip install pandas


# In[6]:


import pandas as pd

# Create a dictionary with years and durations
years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90
movie_dict = {
    "years": years,
    "durations": durations
}

# Create a DataFrame using the movie_dict
durations_df = pd.DataFrame(movie_dict)

# Print the entire DataFrame
print(durations_df)


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary with years and durations
years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie_dict = {
    "years": years,
    "durations": durations
}

# Create a DataFrame using the movie_dict
durations_df = pd.DataFrame(movie_dict)

# Create a line plot
plt.plot(durations_df['years'], durations_df['durations'], marker='o')

# Add title and labels
plt.title("Netflix Movie Durations 2011-2020")
plt.xlabel("Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()


# In[9]:


import pandas as pd

# Read the CSV file into a DataFrame
file_path = "datasets/netflix_data.csv"  # Update the path as needed
netflix_df = pd.read_csv(file_path)

# Print the first five rows of the DataFrame
print(netflix_df.head())


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


# Read the CSV file into a DataFrame
file_path = "datasets/netflix_data.csv"  # Update the path as needed
netflix_df = pd.read_csv(C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv)

# Print the first five rows of the DataFrame
print(netflix_df.head())


# In[13]:


import pandas as pd

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Print the first five rows of the DataFrame
print(netflix_df.head())


# In[14]:


import pandas as pd

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Print the first five rows of netflix_movies_col_subset
print(netflix_movies_col_subset.head())


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], alpha=0.5)  # Alpha for transparency

# Add title and labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()


# In[17]:


import pandas as pd

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Subset short movies with duration less than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))


# In[18]:


import pandas as pd

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Initialize an empty list called colors
colors = []

# Use a for loop to assign colors based on genre
for genre in netflix_movies_col_subset['genre']:
    if genre == "Children":
        colors.append("red")
    elif genre == "Documentaries":
        colors.append("blue")
    elif genre == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Print the first 10 values of the colors list
print(colors[:10])


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Initialize an empty list called colors and assign colors based on genre
colors = []
for genre in netflix_movies_col_subset['genre']:
    if genre == "Children":
        colors.append("red")
    elif genre == "Documentaries":
        colors.append("blue")
    elif genre == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Create a scatter plot with colored points
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(
    netflix_movies_col_subset['release_year'],
    netflix_movies_col_subset['duration'],
    c=colors,  # Use colors list for color mapping
    alpha=0.5
)

# Add title and labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()


# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Provide the file path as a string (enclosed in quotes)
file_path = r'C:\Users\Mary-Clara.Onyekwere\Desktop\datasets\netflix_data.csv'

# Read the CSV file into a DataFrame
netflix_df = pd.read_csv(file_path)

# Subset rows where the type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns: release_year and duration
columns_to_keep = ['release_year', 'duration']
netflix_duration_subset = netflix_df_movies_only[columns_to_keep]

# Group data by release year and calculate the mean duration
mean_durations = netflix_duration_subset.groupby('release_year')['duration'].mean()

# Perform linear regression
x = mean_durations.index
y = mean_durations.values
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Determine the trend based on the slope of the regression line
if slope < 0:
    trend = "Movies are getting shorter."
elif slope > 0:
    trend = "Movies are getting longer."
else:
    trend = "There is no significant trend in movie durations."

# Print the trend result
print(trend)


# In[ ]:




