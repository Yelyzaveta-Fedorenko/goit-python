from setuptools import setup, find_packages

setup(

    name="clean_folder",
    version="0.1",
    author="Yelyzaveta Fedorenko",
    entry_points = {
          'console_scripts' : ['clean-folder=clean_folder.clean:main'],
          },
    packages = find_packages(),
    description = "Clean folder script",

)