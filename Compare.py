
def read_file(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
    # Create a set containing each line stripped of leading/trailing whitespaces
    return set(line.strip() for line in lines)

def compare_followers(old, new):
    # Calculate followers removed (in old but not in new) and followers added (in new but not in old)
    removed = old - new
    added = new - old
    return removed, added

def main():
    # Define file names for old and new followers
    old_followers_file = 'old_followers.txt'
    new_followers_file = 'new_followers.txt'

    # Read old and new followers from respective files
    old_followers = read_file(old_followers_file)
    new_followers = read_file(new_followers_file)

    # Compare old and new followers
    removed, added = compare_followers(old_followers, new_followers)

    # Print removed followers
    print("Removed followers:")
    for follower in removed:
        print(follower)

    # Print added followers
    print("\nAdded followers:")
    for follower in added:
        print(follower)

if __name__ == "__main__":
    main()
#!Frank Mina