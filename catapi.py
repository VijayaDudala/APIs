import requests

# API Key (Replace with your actual Cat API key)
api_key = "live_EhS55sup84PYnN0tuaMZw01fyntS0Imr6eXEqi5TYl3EuZqlQSYPqUmeet8sZ0oO"

# API URL for searching "Siamese" breed in The Cat API
url = "https://api.thecatapi.com/v1/breeds/search?q=Siamese"

# Making the API request with the API key in headers
get_response = requests.get(url, headers={'x-api-key': api_key})

# Checking if the request was successful
if get_response.status_code == 200:
    cat_info = get_response.json()

    for cat in cat_info:
        print(f"Breed: {cat['name']}")
        print(f"Temperament: {cat['temperament']}")
        print(f"Life Span: {cat['life_span']} years")
        print(f"Origin: {cat['origin']}")

        # Fetching the image if available
        if 'reference_image_id' in cat:
            image_url = f"https://cdn2.thecatapi.com/images/{cat['reference_image_id']}.jpg"
            print(f"Image URL: {image_url}")
        else:
            print("No image available.")
        
        print('---')
else:
    print(f"Failed to fetch the cat data: {get_response.status_code}")
