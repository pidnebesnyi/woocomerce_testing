from setuptools import setup, find_packages

setup(
    name='ssqaapitest',
    version='1.0',
    description='Practice API Testing',
    author='Roman Koshevarov',
    author_email='koshevarov.roma@gmail.com',
    url='none',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "certifi",
        "charset-normalizer",
        "exceptiongroup",
        "idna",
        "iniconfig",
        "Jinja2",
        "MarkupSafe",
        "oauthlib",
        "packaging",
        "pluggy",
        "PyMySQL",
        "pytest",
        "pytest-html",
        "pytest-metadata",
        "requests",
        "requests-oauthlib",
        "ssqaapitest",
        "tomli",
        "urllib3",
        "WooCommerce"

    ]
)
