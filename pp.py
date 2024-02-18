# Importing necessary modules
from instagram_private_api import Client
import time
import random

# Function to retrieve followers of a specified user
def get_followers(username, max_count):
    # Placeholder credentials
    username = ''
    password = ''

    # Initializing Instagram API client
    api = Client(username, password)
    api.login()

    # Getting information about the target user
    user_info = api.username_info(username)
    user_id = user_info['user']['pk']

    followers = []  # List to store followers

    next_max_id = None
    while len(followers) < max_count:
        # Fetching followers in batches
        follower_response = api.user_following(user_id, rank_token=api.generate_uuid(), max_id=next_max_id)
        users = follower_response.get('users', [])
        followers.extend(users)

        # Checking if there are more followers to fetch
        if not follower_response.get('next_max_id'):
            break

        next_max_id = follower_response.get('next_max_id')

        # Adding a random delay between requests to avoid rate limiting
        time.sleep(random.uniform(1, 3))

    # Extracting usernames from the follower objects and returning them
    return [follower['username'] for follower in followers[:max_count]]

# Setting parameters
target_username = ""  # Target user's username
exact_followers_count = 1324  # Exact number of followers to retrieve

# Constructing filename for storing followers
followers_file = f"{target_username}_{exact_followers_count}_followers.txt"

# Number of attempts to retrieve followers
attempts = 3
current_followers = []
for i in range(attempts):
    current_followers.extend(get_followers(target_username, exact_followers_count))

    # Checking if enough followers have been retrieved
    if len(current_followers) >= exact_followers_count:
        break

# Truncating the list to the exact number specified
current_followers = current_followers[:exact_followers_count]

# Writing followers' usernames to a file
with open(followers_file, "w") as f:
    for follower in current_followers:
        f.write(follower + "\n")

# Printing confirmation message
print(f"Successfully saved {exact_followers_count} followers of {target_username} in the file {followers_file}.")
