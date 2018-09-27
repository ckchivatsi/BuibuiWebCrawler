import os

#create project folder for each website to be crawled
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

