import requests

def register_domain(domain, email, password):
    # Set API endpoint and parameters
    api_endpoint = "https://api.freenom.com/v2/domain/register.json"
    params = {
        "domain": domain,
        "email": email,
        "password": password,
        "tlds": ["tk", "ml", "ga", "cf", "gq"]  # Freenom's free TLDs
    }

    # Make API request
    response = requests.post(api_endpoint, params=params)

    # Check if domain was registered successfully
    if response.status_code == 200:
        print(f"{domain} registered successfully!")
    else:
        print(f"Failed to register {domain}: {response.text}")

def main():
    domain = input("Enter a domain name: ")
    email = input("Enter your email address: ")
    password = input("Enter a password for your Email account: ")

    register_domain(domain, email, password)

if __name__ == "__main__":
    main()