import requests

def match_talent_profiles(tech_stack: str, avg_team_size: float, manager_score_threshold: float) -> list:
    """Send data to the external talent-matching API and return the response"""
    url = "https://talent-matching.onrender.com/generate-team"
    payload = {
        "tech_stack": tech_stack,
        "avg_team_size": avg_team_size,
        "manager_score_threshold": manager_score_threshold
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Talent matching request failed: {str(e)}")
