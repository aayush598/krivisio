# utils/cocomo2_evaluator.py

import requests

BASE_URL = "https://cocomo2-python-bmzz.onrender.com"

def post_json(endpoint: str, payload: dict):
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request to {endpoint} failed: {e}")
        return None

def evaluate_cocomo2(params: dict):
    result = {}

    # 1. Function Points → SLOC
    fp_payload = params.get("function_points", {})
    result["function_points"] = post_json("/size/from_function_points", fp_payload)

    # 2. Reuse → ESLOC
    reuse_payload = params.get("reuse", {})
    result["reuse"] = post_json("/size/from_reuse", reuse_payload)

    # 3. REVL Adjustment
    revl_payload = params.get("revl", {})
    result["revl"] = post_json("/size/adjust_with_revl", revl_payload)

    # 4. Effort & Schedule
    effort_payload = params.get("effort_schedule", {})
    result["effort_schedule"] = post_json("/estimate/effort_schedule", effort_payload)

    return result
