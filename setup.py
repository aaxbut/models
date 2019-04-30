from setuptools import setup

setup(
    name='models',
    version='0.1',
    description='Models test package',
    url='http://github.com/',
    author='Flying Circus',
    author_email='aaxbut@gmail.com',
    license='MIT',
    packages=['models',],
    install_requires=[
          'gino==0.8.*',
          'pytz==2019.1',
          'sqlalchemy==1.3.*',
    ],
    zip_safe=False
)