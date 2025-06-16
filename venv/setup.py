from setuptools import find_packages,setup
from typing import List
requirement_list:List[str]=[]

def get_requirements()->List[str]:
    "This Function will return requirements"
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines() #Read lines from requirements
            for line in lines:       #Process each line
                requirement=line.strip() #Remove white spaces
                if requirement and requirement!='-e .': # ignore empty lines and -e .
                    requirement_list.append(requirement) #appending to requirement_List
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list
    
setup(
    name="NetworkSecurityML",
    version="0.0.1",
    author="Rajkumar Bantu",
    author_email="rajbantu801@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
