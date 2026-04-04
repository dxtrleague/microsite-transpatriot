import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = ['assets/css/style.css']
all_files = html_files + css_files

patterns = [
    # Headers
    (r'<h1([^>]*)font-size:\s*\d+px;', r'<h1\1font-size: 48px;'),
    (r'<h2([^>]*)font-size:\s*\d+px;', r'<h2\1font-size: 32px;'),
    (r'<h3([^>]*)font-size:\s*\d+px;', r'<h3\1font-size: 24px;'),
    (r'<h4([^>]*)font-size:\s*\d+px;', r'<h4\1font-size: 18px;'),
    
    # Paragraphs / Text
    (r'<p([^>]*)font-size:\s*\d+px;', r'<p\1font-size: 16px;'),
    (r'<a([^>]*)btn-download([^>]*)font-size:\s*\d+px;', r'<a\1btn-download\2font-size: 16px;'),
    
    # Logo texts
    (r'class="logo-title"([^>]*)font-size:\s*\d+px;', r'class="logo-title"\1font-size: 20px;'),
    (r'class="logo-subtitle"([^>]*)font-size:\s*\d+px;', r'class="logo-subtitle"\1font-size: 14px;'),
    
    # Other common fixes for standardizing 15->16, 13->14, 12->14  ONLY globally in CSS if safe
]

for filepath in all_files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, new_content)
            
    # Also standardize general rem usages
    new_content = re.sub(r'font-size:\s*1\.1rem;', 'font-size: 20px;', new_content)
    new_content = re.sub(r'font-size:\s*1rem;', 'font-size: 16px;', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated HTML styles in {filepath}")

print("Done standardizing inline styles!")
