import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = ['assets/css/style.css']
all_files = html_files + css_files

print("Files to process:", all_files)

def replace_font_sizes(content):
    # Standardize all standalone basic text sizes
    # Replace anything from 11px to 17px to 16px if it's generally text
    content = re.sub(r'font-size:\s*(11|12|13)px;', 'font-size: 14px;', content)
    content = re.sub(r'font-size:\s*(15|17)px;', 'font-size: 16px;', content)
    
    # Standardize classes specifically since they differ per file
    
    # 1. Hero Titles (H1 equivalent) -> 48px
    content = re.sub(r'(\.hero-title|\.hero\s+h1)[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 48px;', m.group(0)), content, flags=re.DOTALL)
    
    # 2. Section Titles (H2 equivalent) -> 32px
    content = re.sub(r'(\.section-title|\.contact-title|\.content\s+h2)[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 32px;', m.group(0)), content, flags=re.DOTALL)
    
    # 3. Component Titles (Cards, Focus, Stats, Logos) -> 24px
    content = re.sub(r'(\.card-title|\.fokus-card\s+h3|\.feature-title|\.stat-value)[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 24px;', m.group(0)), content, flags=re.DOTALL)
    
    # Fix Logo specifically
    content = re.sub(r'\.logo-title[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 20px;', m.group(0)), content, flags=re.DOTALL)
    content = re.sub(r'\.logo-subtitle[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 14px;', m.group(0)), content, flags=re.DOTALL)
    
    # Footer and smaller headers -> 18px
    content = re.sub(r'\.footer-title[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 18px;', m.group(0)), content, flags=re.DOTALL)
    
    # Form elements -> 16px/14px
    content = re.sub(r'\.form-label[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 14px;', m.group(0)), content, flags=re.DOTALL)
    content = re.sub(r'\.input-style[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 16px;', m.group(0)), content, flags=re.DOTALL)
    
    # Navbar -> 16px
    content = re.sub(r'\.nav-link[^}]*?font-size:\s*\d+px;', lambda m: re.sub(r'font-size:\s*\d+px;', 'font-size: 16px;', m.group(0)), content, flags=re.DOTALL)

    return content

for filepath in all_files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    new_content = replace_font_sizes(original_content)
    
    # Also standardize direct inline sizes if we missed them initially
    new_content = re.sub(r'<h1([^>]*)font-size:\s*\d+px;', r'<h1\1font-size: 48px;', new_content)
    new_content = re.sub(r'<h2([^>]*)font-size:\s*\d+px;', r'<h2\1font-size: 32px;', new_content)
    new_content = re.sub(r'<h3([^>]*)font-size:\s*\d+px;', r'<h3\1font-size: 24px;', new_content)
    new_content = re.sub(r'<h4([^>]*)font-size:\s*\d+px;', r'<h4\1font-size: 18px;', new_content)
    
    # Brute force fix any remaining weird headings/fonts in styles
    # We will search for all `.xxx { ... font-size: Xpx; }` and normalize
    # For instance if profil has `.section-title { font-size: 36px; }` and media query `.section-title { font-size: 28px; }`
    
    # Mobile queries standard
    # Let's just fix the most egregious ones
    new_content = re.sub(r'font-size:\s*56px|font-size:\s*42px|font-size:\s*36px', 'font-size: 48px', new_content)
    new_content = re.sub(r'font-size:\s*28px|font-size:\s*22px', 'font-size: 32px', new_content)
    new_content = re.sub(r'font-size:\s*20px', 'font-size: 24px', new_content)
    # Be careful not to replace Logo title to 24px, wait Logo title is 20px!
    new_content = re.sub(r'class="logo-title"([^>]*)font-size:\s*24px', r'class="logo-title"\1font-size: 20px', new_content)

    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

print("Done complete pass.")
