
from detector import is_suspicious

print("Enter URLs to check, separated by commas:")
urls_input = input()
urls = [u.strip() for u in urls_input.split(",") if u.strip()]

for url in urls:
    print(f"\nChecking: {url}")
    reasons = is_suspicious(url)
    if reasons:
        print("⚠️ POSSIBLE PHISHING DETECTED")
        for r in reasons:
            print(" -", r)
        print("\nProbabliy Fishing attept:  Do not click on the link and report it if necessary.")
        print("\nPlease be cautious and verify the URL before proceeding.")
        print("\n")

    else:
        print("✅ URL LOOKS SAFE (basic checks)")
        print("\n")