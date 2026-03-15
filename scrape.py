import requests
import time

def get_friends(user_id):
    """Get the list of direct friends of a user."""
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
    response = requests.get(url)

    if response.status_code == 200:
        friends = response.json()['data']
        friend_ids = [friend['id'] for friend in friends]
        return friend_ids
    elif response.status_code == 429:
        print("Rate limit reached, sleeping for 10 seconds...")
        # Wait for 10 seconds (or adjust this value based on the rate-limit)
        time.sleep(10)
        return get_friends(user_id)  # Retry the request
    else:
        print(f"Error: {response.status_code}")
        return []

def get_friends_of_friends(user_id):
    """Get the friends of friends of a user."""
    # First, get the user's direct friends
    direct_friends = get_friends(user_id)
    if not direct_friends:
        return []

    friends_of_friends = set()  # Use a set to avoid duplicates
    for friend_id in direct_friends:
        # Get each friend's direct friends
        friend_ids = get_friends(friend_id)
        for fid in friend_ids:
            if fid != user_id:  # Avoid including the original user
                friends_of_friends.add(fid)
        
        # Add a small delay between each friend's requests
        time.sleep(2)  # Adjust the time delay if needed

    return list(friends_of_friends)

# Example usage
user_id = 123456789  # Replace with any user ID
friends_of_friends = get_friends_of_friends(user_id)
print(friends_of_friends)
