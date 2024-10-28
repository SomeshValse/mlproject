from typing import List
from setuptools import find_packages, setup
from typing import List

#HYPE_E = []
def get_req(file_path:str)->List[str]:
    '''
    this function will return the lists of requirements
    '''
    req_list= []

    with open(file_path) as file_obj:

        req_list=file_obj.readlines()

        req_list=[req.replace("/n","") for req in req_list]

        if "-e ." in req_list:
            req_list.remove("-e .")
    
    return req_list



setup(
    name='mlproject',
    version='0.0.1',
    author='Sam',
    author_email='someshvalse@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')

)