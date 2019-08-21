from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='data-view',  
     version='0.0.6',
     author="Urev Oleg",
     author_email="urevolegg@gmail.com",
     description="A first view of datasets",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=['pandas', 'numpy', 'matplotlib', 'ipython'],
 )