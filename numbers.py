
import requests
import json

def fetch_numbers_from_urls(urls):
    numbers = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            numbers.extend(response.json()["numbers"])
    return numbers

def main():
    api_endpoints = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd",
        "http://20.244.56.144/numbers/rand"
    ]
    
    all_numbers = fetch_numbers_from_urls(api_endpoints)
    sorted_numbers = sorted(set(all_numbers))
    
    result = {"numbers": sorted_numbers}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
