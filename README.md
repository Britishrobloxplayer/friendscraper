# friendscraper
Scrape roblox friends (best for erp database)
Download both scrape.py and checkiferp.py

Open scrape.py
at the bottom youll see:
Example usage
user_id = 123456789 -- replace the id of the user you want to check the friends of, and their related friends (friends of friends)
Save as .py and run in cmd (you need python 3)
Wait for up to 3 minutes, youll get a list of ids, copy and paste all of those ids into a new notepad tab. Delete the "[]" at the start and end of the list.
Open converttolink in notepad, and paste all of those ids in. Do not delete the "[]" already in the script.
It should look like:


 Example usage
user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Add any user IDs you want
urls = convert_to_roblox_urls(user_ids)


Once you put in all ids, save as .py and run the script, so python converttolink.py
it will give you a long list of links, like this:


https://roblox.com/users/10041425896

https://roblox.com/users/4334616552

https://roblox.com/users/2269478891

https://roblox.com/users/7963312115

https://roblox.com/users/3612344308

https://roblox.com/users/1803452405

https://roblox.com/users/3873636347

Paste all ids that are outputted in terminal into a new .txt file. Call it anything, like ids.txt or userids.txt 
Open checkiferp.py in notepad.
The first part is done already, it will be ids that will detect if the user is innapropriate, and keywords, they can be changed.


Where it says: inappropriate_users_file = "inappropriate_users.txt"

API_KEY = "studio api key needed to check group members and api, generate at https://create.roblox.com/dashboard/credentials?activeTab=ApiKeysTab"
ROBLOSECURITY = "roblosecurity goes here to properly check friends idk if its needed"

headers_cookie = {'Cookie': f'.ROBLOSECURITY={ROBLOSECURITY}'}

Follow the instructions.

In the .txt file where you pasted all the links of the users, make sure you saved it, and input the path in this part of the checkiferp script:

links = read_links(r'path to user id files go here example: C:\Users\user\Downloads\ids.txt')

once done, save the script as .py, and run it in cmd.
It will start scanning the list of the users in your ids.txt

You can change keywords in the checkiferp script if it detects non erp users.
