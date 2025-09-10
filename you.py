‏import requests
‏import time

‏url = "https://www.tiktok.com/@._9903"  # local server for testing
‏data = {"message": "test message"}

‏for i in range(10000):  # limited number of attempts
‏    response = requests.post(url, data=data)
‏    print(f"Attempt {i+1}: Status code: {response.status_code}")
‏    time.sleep(0.1)
