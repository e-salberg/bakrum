from setuptools import setup, find_packages
setup(name="bakrum", packages=find_packages())


# this files set ups the project as a package so test/ can run correctlly
# use pip3 install -e .
# The -e flag tells pip to intall the package in editable or "develop" mode. So the next time you run pytest it should find your app in the standard PYTHONPATH.

# python -m pytest tests/ 
# ^ this command also works without having setup.py since
# Python adds the current directory in the PYTHONPATH for you.