import requests

def test_tool1_suggest():
    url = "http://127.0.0.1:8000/api/tool1/suggest"  # Change this if hosted elsewhere
    payload = {
        "project_idea": "Build a course management system with live class features",
        "max_repos": 3
    }

    try:
        response = requests.post(url, json=payload)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            print("Suggested Features:", data.get("suggested_features"))
            print("Suggested Tech Stack:", data.get("suggested_tech_stack"))
            print("Total Repos Processed:", data.get("total_repos_processed"))

            # Optional assertions
            assert isinstance(data.get("suggested_features"), str)
            assert isinstance(data.get("suggested_tech_stack"), str)
            assert isinstance(data.get("total_repos_processed"), int)

            print("✅ Test Passed")
        else:
            print("❌ Test Failed: Non-200 response")
            print("Response:", response.text)

    except Exception as e:
        print("❌ Test Failed with Exception:", str(e))

if __name__ == "__main__":
    test_tool1_suggest()
