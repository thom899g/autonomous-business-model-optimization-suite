import requests
from typing import Optional, Dict

class MarketDataFetcher:
    """Fetches market data from various sources for analysis."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def fetch_data(self, symbols: List[str], start_date: datetime, end_date: datetime) -> Dict:
        """Fetch historical market data for given symbols within a date range."""
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = {
            'symbols': ','.join(symbols),
            'start': start_date.isoformat(),
            'end': end_date.isoformat()
        }
        
        try:
            response = requests.get('https://api.marketdata.com/v1/historical', headers=headers, params=params)
            if response.status_code == 200:
                return response.json()['data']
            else:
                logger.error(f"Failed to fetch data. Status code: {response.status_code}")
                raise DataFetchError("Data fetching failed.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error occurred: {str(e)}")
            raise DataFetchError(str(e))
        
    class DataFetchError(Exception):
        """Custom exception for data fetching errors."""
        pass