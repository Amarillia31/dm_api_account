from setuptools import setup

REQUIRES = [
    'allure-pytest',
    'requests',
    'restclient']

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/Amarillia31/dm_api_account.git',
    license='MIT',
    author='elena',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account'
)
