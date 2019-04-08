import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='fastindex',  
     version='0.0.1',
     author="Yonatan Medan",
     author_email="yonatan.medan@gmail.com",
     description="fast pandas selction and indexing",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/yonatanMedan/fastIndex",
     packages=["fastindex"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )
