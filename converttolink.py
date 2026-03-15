def convert_to_roblox_urls(user_ids):
    # Define the base URL
    base_url = "https://roblox.com/users/"
    
    # Generate the Roblox profile URLs
    roblox_urls = [f"{base_url}{user_id}" for user_id in user_ids]
    
    return roblox_urls

# Example usage
user_ids = [ ]  # Add any user IDs you want
urls = convert_to_roblox_urls(user_ids)

# Print the result
for url in urls:
    print(url)
