import requests
import json
import pprint
# Create your dictionary class 
class My_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

def someSearch(query):


    url = "https://deezerdevs-deezer.p.rapidapi.com/search"

    querystring = {"q":query}

    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "292b7df762msh8d462e70b1e0dbap14fbf1jsn6e68782d54cf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.text
    searchdict = json.loads(json_data)["data"]
    search_results = My_dictionary()
    i = 0
    for result in searchdict:
        
        my_dict = {}
        my_dict['id'] = result["id"]
        my_dict['title'] = result["title"]
        my_dict['duration'] = result["duration"]
        my_dict['url'] = result["preview"]
        my_dict['artist_id'] = result["artist"]["id"]
        my_dict['artist_name'] = result["artist"]["name"]
        my_dict['album_id'] = result["album"]["id"]
        my_dict['album_title'] = result["album"]["title"]
        my_dict['cover'] = result["album"]["cover"]
        
        search_results.add( f'result{i}', json.dumps(my_dict))
        
        i += 1        

    return search_results

if __name__ == "__main__":
    r = someSearch('set fire to the rain')
    pprint.pprint(r)