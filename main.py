def is_suspicious(url):
    # 1. URL too long
    if len(url) > 75:
        return "Suspicious (too long)"
    
    # 2. @ symbol is used
    if "@" in url:
        return "Suspicious (@ symbol used)"
    
    # 3. Hyphens (common in fake domains)
    if "-" in url:
        return "Suspicious (hyphens detected)"
    
    # 4. HTTP instead of HTTPS
    if url.startswith("http://"):
        return "Suspicious (no HTTPS)"
    
    # 5. If none triggered, looks safe
    return "Looks Safe (basic checks)"

# --- MAIN PROGRAM ---
url = input("Enter URL to check: ")
result = is_suspicious(url)
print(result)
