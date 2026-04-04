import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = ['assets/css/style.css']
all_files = html_files + css_files

patterns = [
    # General replacements for hardcoded pixel sizes to modernize
    (r'font-size:\s*13px;', 'font-size: 14px;'),
    (r'font-size:\s*15px;', 'font-size: 16px;'),
    (r'font-size:\s*17px;', 'font-size: 16px;'),
    
    # Specific elements
    (r'\.logo-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 20px;', m.group(0))),
    (r'\.logo-subtitle\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 14px;', m.group(0))),
    
    # Nav
    (r'\.nav-link\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 16px;', m.group(0))),
    
    # Hero Title (large)
    (r'\.hero-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 48px;', m.group(0))),
    
    # Section Title (medium large)
    (r'\.section-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 32px;', m.group(0))),
    (r'\.contact-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 32px;', m.group(0))),

    # Card / Focus titles (medium)
    (r'\.card-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 24px;', m.group(0))),
    (r'\.card\s+h3\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 24px;', m.group(0))),
    (r'\.fokus-card\s+h3\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 24px;', m.group(0))),
    (r'\.feature-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 24px;', m.group(0))),

    # Footers
    (r'\.footer-title\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 18px;', m.group(0))),
    (r'\.footer-links\s+a\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 16px;', m.group(0))),
    (r'\.footer-bottom\s*\{[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 14px;', m.group(0))),
    
    # Fix inline 14px with opacity that acts as general body text
    (r'style="([^"]*)font-size:\s*14px;\s*opacity:\s*0\.7;', r'style="\g<1>font-size: 16px; opacity: 0.7;'),
    (r'style="([^"]*)font-size:\s*14px;\s*opacity:\s*0\.8;', r'style="\g<1>font-size: 16px; opacity: 0.8;'),
    (r'style="font-size: 14px; opacity: 0.7; margin-bottom: 10px;"', 'style="font-size: 16px; opacity: 0.7; margin-bottom: 10px;"'),
    (r'style="font-size: 14px; opacity: 0.7;"', 'style="font-size: 16px; opacity: 0.7;"'),
    
    # Logo title specifically targeted inline
    (r'style="font-size: 16px; font-weight: 700; display: block; text-transform: uppercase;"', 'style="font-size: 20px; font-weight: 700; display: block; text-transform: uppercase;"'),
    (r'style="font-size: 18px; font-weight: 700; display: block; text-transform: uppercase;"', 'style="font-size: 20px; font-weight: 700; display: block; text-transform: uppercase;"'),
]

for filepath in all_files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for pattern, replacement in patterns:
        if callable(replacement):
            new_content = re.sub(pattern, replacement, new_content, flags=re.DOTALL)
        else:
            new_content = re.sub(pattern, replacement, new_content)
            
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done standardizing sizes!")
