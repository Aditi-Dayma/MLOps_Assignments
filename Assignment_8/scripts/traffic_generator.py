import time
import requests

URL = "http://localhost:8000/predict"

def generate_traffic(num_requests=50):
    print(f"Generating {num_requests} inference requests to populate Prometheus metrics...")
    for i in range(num_requests):
        try:
            res = requests.post(URL)
            if res.status_code == 200:
                print(f"[{i+1}/{num_requests}] Response: {res.json()}")
        except Exception as e:
            print(f"Error connecting to service: {e}")
        time.sleep(0.1)
    print("Traffic generation complete.")

if __name__ == "__main__":
    generate_traffic()
