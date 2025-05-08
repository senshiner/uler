
# Hari 20 - API dan HTTP Requests

import requests
import json
from datetime import datetime

# HTTP Request dengan modul requests
# Perlu install modul requests: pip install requests

# GET Request
print("GET Request:")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"Status code: {response.status_code}")
    print(f"Content type: {response.headers['Content-Type']}")
    
    # Parsing response JSON
    data = response.json()
    print("\nResponse data:")
    print(f"User ID: {data['userId']}")
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# GET Request dengan parameters
print("\nGET Request dengan parameters:")
try:
    params = {
        "userId": 1,
        "completed": False
    }
    response = requests.get("https://jsonplaceholder.typicode.com/todos", params=params)
    print(f"Status code: {response.status_code}")
    print(f"URL: {response.url}")
    
    # Parsing response JSON
    data = response.json()
    print(f"\nDitemukan {len(data)} todo items")
    for i, item in enumerate(data[:3], 1):  # Ambil 3 item pertama
        print(f"Item {i}:")
        print(f"  User ID: {item['userId']}")
        print(f"  ID: {item['id']}")
        print(f"  Title: {item['title']}")
        print(f"  Completed: {item['completed']}")
    
    if len(data) > 3:
        print(f"...dan {len(data) - 3} item lainnya")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# POST Request
print("\nPOST Request:")
try:
    new_post = {
        "title": "Test Post",
        "body": "This is a test post created by Python",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    print(f"Status code: {response.status_code}")
    
    # Parsing response JSON
    data = response.json()
    print("\nCreated post:")
    print(f"User ID: {data['userId']}")
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# PUT Request (Update)
print("\nPUT Request:")
try:
    updated_post = {
        "id": 1,
        "title": "Updated Post",
        "body": "This post has been updated using Python",
        "userId": 1
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
    print(f"Status code: {response.status_code}")
    
    # Parsing response JSON
    data = response.json()
    print("\nUpdated post:")
    print(f"User ID: {data['userId']}")
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# PATCH Request (Partial Update)
print("\nPATCH Request:")
try:
    patch_data = {
        "title": "Patched Post"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=patch_data)
    print(f"Status code: {response.status_code}")
    
    # Parsing response JSON
    data = response.json()
    print("\nPatched post:")
    print(f"User ID: {data['userId']}")
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# DELETE Request
print("\nDELETE Request:")
try:
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Request dengan headers
print("\nRequest dengan headers:")
try:
    headers = {
        "User-Agent": "Python Requests",
        "Accept": "application/json"
    }
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)
    print(f"Status code: {response.status_code}")
    print(f"Headers sent: {headers}")
    print(f"Response headers: {dict(response.headers)}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Request dengan timeout
print("\nRequest dengan timeout:")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    print(f"Status code: {response.status_code}")
    print(f"Request completed within timeout")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Menggunakan session
print("\nMenggunakan session:")
try:
    with requests.Session() as session:
        # Session akan menyimpan cookies, headers, dll.
        session.headers.update({"User-Agent": "Python Session"})
        
        # Request pertama
        response1 = session.get("https://jsonplaceholder.typicode.com/todos/1")
        print(f"First request status: {response1.status_code}")
        
        # Request kedua (menggunakan session yang sama)
        response2 = session.get("https://jsonplaceholder.typicode.com/todos/2")
        print(f"Second request status: {response2.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Error handling
print("\nError handling:")
try:
    # URL tidak valid
    response = requests.get("https://nonexistent-url.xyz")
    response.raise_for_status()  # Raise exception untuk kode status 4XX/5XX
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Timeout Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Contoh Real-world: Open Weather Map API (simulasi)
print("\nContoh Real-world API (simulasi):")
# Dalam implementasi nyata, Anda perlu mendaftar dan mendapatkan API key
# api_key = "your_api_key_here"
# city = "Jakarta"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Simulasi response
weather_data = '''
{
    "coord": {"lon": 106.8451, "lat": -6.2146},
    "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}],
    "base": "stations",
    "main": {
        "temp": 32.5,
        "feels_like": 35.8,
        "temp_min": 29.2,
        "temp_max": 33.0,
        "pressure": 1010,
        "humidity": 65
    },
    "visibility": 6000,
    "wind": {"speed": 3.6, "deg": 160},
    "clouds": {"all": 90},
    "dt": 1630000000,
    "sys": {
        "type": 1,
        "id": 9383,
        "country": "ID",
        "sunrise": 1629931200,
        "sunset": 1629974400
    },
    "timezone": 25200,
    "id": 1642911,
    "name": "Jakarta",
    "cod": 200
}
'''

weather = json.loads(weather_data)
print(f"Cuaca di {weather['name']}, {weather['sys']['country']}:")
print(f"Kondisi: {weather['weather'][0]['main']} ({weather['weather'][0]['description']})")
print(f"Suhu: {weather['main']['temp']}°C")
print(f"Terasa seperti: {weather['main']['feels_like']}°C")
print(f"Kelembaban: {weather['main']['humidity']}%")
print(f"Kecepatan angin: {weather['wind']['speed']} m/s")

# Konversi timestamp Unix ke waktu lokal
sunrise = datetime.fromtimestamp(weather['sys']['sunrise'])
sunset = datetime.fromtimestamp(weather['sys']['sunset'])
print(f"Matahari terbit: {sunrise.strftime('%H:%M:%S')}")
print(f"Matahari terbenam: {sunset.strftime('%H:%M:%S')}")
