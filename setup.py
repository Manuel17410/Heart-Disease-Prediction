from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Eligibility_Prediction_for_Loan",
    version="0.1",
    author="Manuel",
    packages=find_packages(),
    install_requires=requirements,
)
