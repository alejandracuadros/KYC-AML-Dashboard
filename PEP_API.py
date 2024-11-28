#this API will help us find the proper PEP and POI people
# Our focus are matches with scores above 0.8, because they are more relevant
# Topics tells us why these people are flagged, POI means Person of Interest and role.pep is if they are or not polically exposed

import requests


# The OpenSanctions service API endpoint configuration
API_KEY = "32da23945efbcbf8d1c4ac2976ba00cc"
URL = "https://api.opensanctions.org/match/peps"
HEADERS = {"Authorization": f"ApiKey {API_KEY}"}

def search_pep(name):
    if not name:
        print("Error: Name is required!")
        return

#sending query to OpenSanctions API
    query = {"queries": {"q1":
                           {"schema": "Person",
                            "properties": {
                                "name": [name]
                            }
                            }
                       }
           }
    try:
        response = requests.post(URL, json=query, headers=HEADERS)
        response.raise_for_status()

        # receive parse responses
        results = response.json().get("responses", {}).get("q1", {})
        if not results.get("results"):
            print("No matches found.")
            return

# display results
        print(f"Found matches for '{name}':")
        for match in results.get("results", []):
            print(f"Name: {match.get('properties', {}).get('name', ['Unknown'])[0]}")
            print(f"Score: {match['score']}")
            print(f"Topics: {', '.join(match.get('properties', {}).get('topics', []))}")
            print("  ---")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenSanctions API: {e}")


#asking for user input
if __name__ == "__main__":
    name_to_search = input("Enter a name to search for: ")
    search_pep(name_to_search)










