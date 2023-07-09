import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]:%(message)s' )

#stored in src folder , this will have all the folders
project_name = "textSummarizer"

list_of_files = [
         #help in CI/CD deployment ie whenever we commit , it will automatically got update
         #in cloud , yaml file
        " .github/workflow/.gitkeep",
        f"src/{project_name}/__init__.py",
        #__init__.py is constructor file - help in file import in local pacage
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/logging//__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "app.py",
        "main.py",
        "Dockerfile",
        "requirement.txt",
        "setup.py"   
        "research/trials.ipynb"   

]

for filepath in list_of_files:
    filepath = Path(filepath)#operating sys will give the path
    #seperating folder and file from path
    filedir, filename = os.path.split(filepath)

    if filedir!="" :
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    
    else:
        logging.info(f"{filepath} already exists ")

