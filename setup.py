from setuptools import find_packages, setup

setup(
    name='Vital AI',  # Fixed string formatting and ensured comma
    version='0.0.0',  # Added missing comma
    author='Zubair Jamil',
    author_email='zubairjamilwork@gmail.com',
    packages=find_packages(),
    install_requires=[]  # Empty list is fine for now
)
