"""
Payload Lab - Setup Script
Educational payload template framework
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / 'README.md'
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ''

setup(
    name='payload_lab',
    version='1.0.0',
    description='Educational payload template framework for security training',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Payload Lab Project',
    author_email='',
    url='https://github.com/yourusername/payload_lab',
    license='Educational Use Only',
    
    packages=find_packages(),
    include_package_data=True,
    
    python_requires='>=3.7',
    
    install_requires=[
        # No external dependencies - uses Python standard library only
    ],
    
    entry_points={
        'console_scripts': [
            'payload_lab=payload_lab.cli:main',
        ],
    },
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Topic :: Education',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    
    keywords='security, education, owasp, penetration-testing, payload, xss, sqli, command-injection, training',
    
    project_urls={
        'OWASP': 'https://owasp.org/',
        'Documentation': 'https://github.com/yourusername/payload_lab/blob/main/README.md',
    },
)
