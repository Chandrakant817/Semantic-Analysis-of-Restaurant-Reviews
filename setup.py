from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "MLPipeline"
VERSION = "0.0.1"
DESCRIPTION = "This is Machine Learning Project"
AUTHOR = "Chandrakant Thakur"
AUTHOR_EMAIL = "chandrakantthakur817@gmail.com"

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requries = []
     )