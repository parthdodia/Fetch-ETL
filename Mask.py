import hashlib
import json

class Mask:
    def __init__(self, encryption_type=0, debug=False):
        # Initialize the Mask object with default values
        self.queue_fields = ["user_id", "app_version", "device_type", "ip", "locale", "device_id"]
        # Define a bridge to map input fields to output fields
        self.bridge = {
            "user_id": "user_id",
            "app_version": "app_version",
            "device_type": "device_type",
            "locale": "locale",
            "ip": "masked_ip",
            "device_id": "masked_device_id"
        }
        self.debug = debug
        self.encryption_type = encryption_type

    def encrypt(self, value: str) -> str:
        if self.encryption_type == 0:
            # Convert the string to an integer using little-endian byte order
            return str(int.from_bytes(value.encode(), 'little'))
        elif self.encryption_type == 1:
            return hashlib.sha256(value.encode()).hexdigest()
        else:
            return value

    def mask(self, responses: list or dict) -> list or dict:
        # Mask the input responses (either a list of dictionaries or a single dictionary)
        if isinstance(responses, list):
            return [self._mask_response(response) for response in responses]
        elif isinstance(responses, dict):
            return self._mask_response(responses)
        else:
            raise ValueError("Invalid input type.")

    def _mask_response(self, response: dict) -> dict:
        masked_response = {}
        for field in self.queue_fields:
            # Check if the response has a 'Body' key
            if 'Body' in response:
                response = json.loads(response['Body'])
            if field in response:
                if 'asked' in self.bridge[field]:
                    masked_response[self.bridge[field]] = self.encrypt(response[field])
                else:
                    masked_response[self.bridge[field]] = response[field]
            else:
                if self.debug:
                    print("No Key")
        return masked_response