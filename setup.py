# setup.py for packaging and distributing the Python project
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='mlproject',
    version="0.0.1",
    author="AkshatM",
    author_email="Akshatmaurya1501@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    description="A brief description of your project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AkshatM13/mlproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)