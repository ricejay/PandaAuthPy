

# ──────────────────────────────────── #
#          PandaAuthPy Module          #
#                                      #
# by: RiceJay                          #
# ──────────────────────────────────── #



import requests
import hashlib
import json

class PandaAuthPy:
    def __init__(self):
        pass
    
    def get_ip(self):
        try:
            response = requests.get("https://api.ipify.org")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print("ERROR IN HTTP GET REQUEST: ", e)
            return "BAD_REQUEST"
    
    def encode_ip(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()
    
    def get_key(self, service: str) -> str:
        hashed_ip = self.encode_ip(self.get_ip())
        return f"https://pandadevelopment.net/getkey?service={service}&hwid={hashed_ip}"
    
    def validate_key(self, key: str, service: str) -> bool:
        try:
            url = f"https://pandadevelopment.net/v2_validation?key={key}&service={service}&hwid={self.encode_ip(self.get_ip())}"
            response = requests.get(url)
            response.raise_for_status()
            
            info = response.json()
            return info.get("V2_Authentication") == "success"
        except requests.RequestException as e:
            print("ERROR IN HTTP GET:", e)
        except json.JSONDecodeError as e:
            print("ERROR UNMARSHALING JSON:", e)
        return False
        
    def validate_premium_key(self, key: str, service: str) -> bool:
        try:
            url = f"https://pandadevelopment.net/v2_validation?key={key}&service={service}&hwid={self.encode_ip(self.get_ip())}"
            response = requests.get(url)
            response.raise_for_status()
            
            info = response.json()
            key_info = info.get("Key_Information")
            if isinstance(key_info, dict):
                return key_info.get("Premium_Mode", False)
            else:
                print("ERROR: 'Key_Information' is not a dictionary")
        except requests.RequestException as e:
            print("ERROR IN HTTP GET:", e)
        except json.JSONDecodeError as e:
            print("ERROR UNMARSHALING JSON:", e)
        return False