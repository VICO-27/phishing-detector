from rules import SUSPICIOUS_WORDS, SUSPICIOUS_DOMAINS

def is_suspicious(url):
    reasons = []

    if len(url) > 75:
        reasons.append("URL is too long")

    if "@" in url:
        reasons.append("@ symbol used")

    if "-" in url:
        reasons.append("Hyphens detected")

    if url.startswith("http://"):
        reasons.append("No HTTPS (not secure)")

    # Check suspicious words
    for word in SUSPICIOUS_WORDS:
        if word in url.lower():
            reasons.append(f"Suspicious keyword found: '{word}'")
            break

    # Check suspicious domains
    for domain in SUSPICIOUS_DOMAINS:
        if url.lower().endswith(domain):
            reasons.append(f"Suspicious domain extension: '{domain}'")
            break

    if any(char.isdigit() for char in url):
        reasons.append("Numbers found in URL")

    if url.count(".") >= 3 and url.replace(".", "").isdigit():
        reasons.append("IP address used instead of domain")

    return reasons
