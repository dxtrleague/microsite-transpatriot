import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

global_style = """
    <!-- STANDARDIZASI FONT GLOBAL -->
    <style id="global-typography">
        body, p, a, span, div, input, button, select, textarea {
            font-family: 'Inter', sans-serif !important;
        }
        body { font-size: 16px !important; }
        
        /* Typography Scale */
        .logo-title { font-size: 20px !important; }
        .logo-subtitle { font-size: 14px !important; }
        .nav-link { font-size: 16px !important; }
        
        .hero-title, .hero h1 { font-size: 48px !important; }
        .section-title, .contact-title { font-size: 32px !important; }
        .card-title, .fokus-card h3, .feature-title, .stat-value, .doc-title, .profil-list strong { font-size: 20px !important; }
        
        .hero-desc, .section-desc, p { font-size: 16px !important; }
        .footer-title, h4 { font-size: 18px !important; }
        .footer-bottom, .footer-links a, .hero-badge { font-size: 14px !important; }
        
        /* Mobile Scaling */
        @media (max-width: 768px) {
            .hero-title, .hero h1 { font-size: 32px !important; }
            .section-title, .contact-title { font-size: 24px !important; }
        }
    </style>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove previous injected style if it exists so we don't multiply it
    if "<!-- STANDARDIZASI FONT GLOBAL -->" in content:
        import re
        content = re.sub(r'<!-- STANDARDIZASI FONT GLOBAL -->.*?</style>', '', content, flags=re.DOTALL)
        
    # Inject before </head>
    if "</head>" in content:
        new_content = content.replace("</head>", f"{global_style}</head>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Applied global typography to {filepath}")
