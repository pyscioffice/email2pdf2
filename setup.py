from setuptools import setup, find_packages


setup(
    name='email2pdf',
    version='0.9.9.0',
    packages=find_packages(exclude=["*tests*"]),
    url='https://github.com/andrewferrier/email2pdf',
    license='MIT',
    author='Andrew Ferrier',
    description='email2pdf is a Python script to convert emails to PDF.',
    install_requires=[
        'beautifulsoup4>=4.6.3',
        'html5lib',
        'lxml',
        'pypdf2',
        'python-magic',
        'reportlab',
    ],
    entry_points={
        "console_scripts": [
            'email2pdf=email2pdf.__main__:main'
        ]
    }
)
