# Step 8: Use django-security and django-secure libraries to enhance the security of the website and protect it from common web vulnerabilities.

# Install the django-security and django-secure libraries
os.system("pip install django-security django-secure")

# Add the middleware classes to the MIDDLEWARE list in settings.py
with open("cyberattack/settings.py", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace("'django.middleware.security.SecurityMiddleware',", "'django.middleware.security.SecurityMiddleware',\n    'security.middleware.DoNotTrackMiddleware',\n    'security.middleware.ContentNoSniff',\n    'security.middleware.XssProtectMiddleware',\n    'security.middleware.ContentSecurityPolicyMiddleware',\n    'djangosecure.middleware.SecurityMiddleware',"))

# Add the security and djangosecure apps to the INSTALLED_APPS list in settings.py
with open("cyberattack/settings.py", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace("'django.contrib.staticfiles',", "'django.contrib.staticfiles',\n    'security',\n    'djangosecure',"))

# Configure some security settings in settings.py
with open("cyberattack/settings.py", "a") as f:
    # Enable HTTPS for the website
    f.write("\nSECURE_SSL_REDIRECT = True\n")
    
    # Set a secure cookie for the session
    f.write("\nSESSION_COOKIE_SECURE = True\n")

    # Set a secure cookie for the CSRF token
    f.write("\nCSRF_COOKIE_SECURE = True\n")

    # Set a strict transport security header for the website
    f.write("\nSECURE_HSTS_SECONDS = 31536000\n")
    f.write("\nSECURE_HSTS_INCLUDE_SUBDOMAINS = True\n")
    
    # Set a content security policy header for the website
    f.write("\nCSP_DEFAULT_SRC = ('self',)\n")
