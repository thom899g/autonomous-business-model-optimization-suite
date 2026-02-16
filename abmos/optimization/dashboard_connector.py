import json
from typing import Dict, Optional

class DashboardConnector:
    """Connects to the dashboard to report and receive commands."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def send_update(self, data: Dict) -> bool:
        """Send an update to the dashboard."""
        headers = {'Authorization': f'Bearer {self.api_key}', 
                  'Content-Type': 'application/json'}
        payload = json.dumps(data)
        
        try:
            response = requests.post('https://dashboard.evolsys.com/updates', 
                                   headers=headers, data=payload)
            if response.status_code == 200:
                return True
            else:
                logger.error(f"Update failed. Status code: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error occurred: {str(e)}")
            return False
            
    def receive_command(self) -> Optional[Dict]:
        """Receive a command from the dashboard."""
        headers = {'Authorization': f'Bearer {self.api_key}'}
        
        try:
            response = requests.get('https://dashboard.evolsys.com/commands', 
                                   headers=headers)
            if response.status_code == 200:
                return response.json()['command']
            else:
                logger.warning("No command received or error in response.")
                return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error occurred: {str(e)}")
            return None