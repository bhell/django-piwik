from os.path import join, dirname
from setuptools import setup, find_packages

HERE = dirname(__file__)


def get_version():
    fh = open(join(HERE, "piwik", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()


setup(
    name="piwik",
    version=get_version(),
    description="Application to add Piwik analytics to a Django site",
    long_description=(open(join(HERE, "README.rst")).read() + "\n\n" +
                      open(join(HERE, "LICENSE.txt")).read()),
    author="Benjamin Hell",
    author_email="b@bhell.net",
    url="https://github.com/bhell/django-piwik/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: Log Analysis",
    ],
    zip_safe=True,
    tests_require=["Django>=1.2"],
    test_suite="tests"
)
