'''
    the setup.py file is an essentaial part of packaging
    and distributing python projects. It is used by setuptools() 
    to defin the configuration of your project, such as its metadat
    dependencies and more.
'''

from setuptools import find_packages, setup # it consider all folders having __init__.py file as a package.
from typing import List


def get_requirements()->List[str]:
    '''
    This fn will return list of requiremnts
    '''
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement) 
    except FileNotFoundError:
        print("requirments.txt file is not found")

    return requirement_list

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author= "Shibith P",
    author_email= "shibithp94@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)