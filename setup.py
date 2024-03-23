from setuptools import (
    setup,
    find_packages,
)

REQUIRES = [
    'allure-pytest',
    'requests',
    'restclient',
    'pydantic'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/Amarillia31/dm_api_account.git',
    license='MIT',
    author='elena',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account'
)
