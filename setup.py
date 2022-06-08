import os
from pathlib import Path
from setuptools import setup, find_packages
 

README=Path("README.md").read_text(encoding="utf-8")
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'django_sotp',
    version = '1.0.2',
    packages = find_packages(),
    include_package_data = True,
    license = 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    description = 'Generate a secured base32 one time password to authenticate your user! 🔐',
    long_description = README,
    long_description_content_type='text/markdown',
    keywords=[
        'sotp', 
        'otp', 
        'totps', 
        'one time password',
        'passwords' 
    ],
    url = 'https://github.com/israelabraham/django-sopt',
    author = 'Abram 🐼',
    author_email = 'israelvictory87@gmail.com',
    classifiers =[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires=">=3.6",
    install_requires=[
        "django>=2.2",
        "django-apscheduler",
    ],
)
