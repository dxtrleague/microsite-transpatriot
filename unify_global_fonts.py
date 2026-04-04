import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = ['assets/css/style.css']
all_files = html_files + css_files

for filepath in all_files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Standardize the CSS Variable definition
    new_content = re.sub(r'--font-family-body:\s*[^;]+;', "--font-family: 'Inter', sans-serif;", new_content)
    new_content = re.sub(r'--font-family:\s*[^;]+;', "--font-family: 'Inter', sans-serif;", new_content)
    new_content = re.sub(r'--font-main:\s*[^;]+;', "--font-family: 'Inter', sans-serif;", new_content)

    # 2. Standardize variable usage
    new_content = re.sub(r'font-family:\s*var\(--font-family-body\);', 'font-family: var(--font-family);', new_content)
    new_content = re.sub(r'font-family:\s*var\(--font-main\);', 'font-family: var(--font-family);', new_content)

    # 3. Standardize hardcoded font strings
    new_content = re.sub(r"font-family:\s*['\"]DM Sans['\"][^;]*;", "font-family: 'Inter', sans-serif;", new_content)
    new_content = re.sub(r"font-family:\s*['\"]Inter['\"][^;]*;", "font-family: 'Inter', sans-serif;", new_content)

    # 4. Standardize `body {` to explicitly have font-size: 16px if it doesn't already
    body_match = re.search(r'body\s*\{([^}]*)\}', new_content)
    if body_match:
        body_content = body_match.group(1)
        # remove old font-size if exists
        body_content = re.sub(r'font-size:\s*[^;]+;', '', body_content)
        # remove old font-family if exists
        body_content = re.sub(r'font-family:\s*[^;]+;', '', body_content)
        
        # Add the standardized ones
        body_content = f"\n    font-family: var(--font-family);\n    font-size: 16px;{body_content}"
        
        # reconstruct the body
        new_content = new_content[:body_match.start()] + f"body {{{body_content}}}" + new_content[body_match.end():]

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Standardized fonts in {filepath}")

print("Done standardizing global fonts!")
