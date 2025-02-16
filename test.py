import requests

# URL to fetch
url = "https://famme.no/"

# Basic headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

try:
    # Fetch HTML content
    response = requests.get(url, headers=headers)

    # Check for request success
    if response.status_code == 200:
        print("HTML content retrieved successfully!")
        html_content = response.text

        # Save the content to a file for easier viewing
        with open('famme_page.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("Content saved to famme_page.html")

    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"An error occurred: {e}")