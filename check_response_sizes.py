import requests

def check_response_sizes():
    url = "https://dog.ceo/api/breeds/image/random"  
    request_count = 100  
    threshold_size =  1050000

    larger_count = 0  
    smaller_count = 0 

    for i in range(request_count):
        try:
            response = requests.get(url)
            
            if response.status_code == 200:  
                json_data = response.json()
                if 'message' in json_data:
                    image_url = json_data['message'] 
                    image_response = requests.get(image_url)
                    content_length = len(image_response.content)  
                    if content_length > threshold_size:
                        larger_count += 1
                    else:
                        smaller_count += 1

                    print(f"Request {i + 1}: {content_length} bytes, Image URL: {image_url}")
                else:
                    print(f"Request {i + 1} failed: No image found in response")
            else:
                print(f"Request {i + 1} failed: Status Code {response.status_code}")
        except Exception as e:

            print(f"Request {i + 1} failed: {e}")

    print(f"\nResponses larger than {threshold_size} bytes: {larger_count}")
    print(f"Responses smaller than {threshold_size} bytes: {smaller_count}")

if __name__ == "__main__":
    check_response_sizes()
