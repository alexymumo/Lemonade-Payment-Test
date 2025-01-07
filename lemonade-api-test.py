import requests

BASE_URL = "https://fakestoreapi.com/auth/login"

API_TEST_CASES = [
    {"username":"mor_2314","password":"83r5^_","expected_code":200,"description":"positive login test"},
    {"username":"1234","password":"1234","expected_code":401,"description":"negative login test"}
]

def test_login_api(test_case,url):
    for case in test_case:
        print(f"Running test case: {case['description']}")
        res = requests.post(url,json={"username":case["username"],"password":case["password"]})
        status_code = res.status_code

        try:
            response_json = res.json()
        except requests.exceptions.JSONDecodeError:
            response_json = {"error":"Non JSON response","body":res.text}

        if status_code == case["expected_code"]:
            print(f"Test Passed: Status Code {status_code}")
            if status_code == 200 and "token" in response_json:
                print(f"Token: {response_json['token']}")
            elif status_code != 200:
                print("Invalid username and password")
        else:
            print(f"Test Failed: Expected {case['expected_code']}, but status code is{status_code}")
            print(f"Response: {response_json}")
        print("-" * 50)
if __name__ == "__main__":
    test_login_api(API_TEST_CASES,BASE_URL)