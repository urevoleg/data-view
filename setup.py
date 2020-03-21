from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='data-view',  
     version='0.2.0',
     download='https://github.com/urevoleg/data-view',
     download_url='https://github.com/urevoleg/data-view/archive/0.2.0.tar.gz',
     author="Urev Oleg",
     author_email="urevolegg@gmail.com",
     description="Automated view of dataset",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.6",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=['pandas', 'numpy', 'matplotlib', 'ipython', 'seaborn'],
 )
