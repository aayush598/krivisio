import requests

def match_talent_profiles(json_input: dict) -> dict:
    """Send a JSON input as-is to the external talent-matching API and return the response"""
    url = "https://talent-matching.onrender.com/generate-team"
    
    try:
        response = requests.post(url, json=json_input, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Talent matching request failed: {str(e)}")
