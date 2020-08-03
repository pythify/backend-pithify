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
def songSearch(searchdict):
    search_results = My_dictionary()
    i = 0
    for result in searchdict["data"]:
                
        my_dict = {}
        my_dict['id'] = result["id"]
        my_dict['title'] = result["title"]
        my_dict['duration'] = result["duration"]
        my_dict['url'] = result["preview"]
        my_dict['artist_id'] = result["artist"]["id"]
        my_dict['artist_name'] = result["artist"]["name"]
        my_dict['album_id'] = result["album"]["id"]
        my_dict['album_title'] = result["album"]["title"]
        my_dict['album_tracklist'] = result["album"]["tracklist"]
        my_dict['cover'] = result["album"]["cover"]
        
                
        search_results.add( f'result{i}', json.dumps(my_dict))
                
        i += 1 
    if searchdict['next']:
        search_results['next'] = searchdict['next']


    return search_results
    
def albumSearch(searchdict):
    search_results = My_dictionary()
    i = 0
    my_list = []
    for result in searchdict['data']:
                
        if not result["album"]["title"] in my_list:
            my_list.append(result["album"]["title"])
            my_dict = {}
            my_dict['artist_name'] = result["artist"]["name"]
            my_dict['album_title'] = result["album"]["title"]

            tracklist_response = requests.request("GET", result["album"]["tracklist"])
            json_tracklist = tracklist_response.text
            my_dict['tracklist'] = json.loads(json_tracklist)['data']

            my_dict['tracklist_url'] = result["album"]["tracklist"]
            my_dict['cover'] = result["album"]["cover"]
            search_results.add( f'result{i}', json.dumps(my_dict))
            i += 1 

    return search_results

def someSearch(query,param):


    url = "https://deezerdevs-deezer.p.rapidapi.com/search"

    querystring = {"q":query}

    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "292b7df762msh8d462e70b1e0dbap14fbf1jsn6e68782d54cf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.text
    searchdict = json.loads(json_data)
    if not searchdict:
        param= 'error'
    else:
        # pprint.pprint(searchdict, sort_dicts=False)
        if param == 'songs':
            return songSearch(searchdict)
        if param == 'artist':
            return artistSearch(searchdict)
        if param == 'genre':
            return songSearch(searchdict)
        if param == 'album':
            return albumSearch(searchdict)
        
    
    

if __name__ == "__main__":
    r = someSearch('eminen', 'songs')
    next_response = requests.request("GET", r['next'])
    json_next = next_response.text
    searchdict1 = json.loads(json_next)
    b = songSearch(searchdict1)
    #print(r)
    pprint.pprint(b, sort_dicts=False)