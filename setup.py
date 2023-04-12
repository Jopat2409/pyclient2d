import os.path

from setuptools import setup, find_packages
import codecs

c_dir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(c_dir, "README.md"), encoding='utf-8') as ld:
    long_description = "\n" + ld.read()

VERNUM = '0.0.1'
DESC = 'Encapsulating game server and client into one package'

setup(
    name='pyclient',
    version=VERNUM,
    author="Jopat2409",
    author_email="joantpat@gmail.com",
    description=DESC,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pygame', 'socket'],
    keywords=['python', 'game', 'client', 'server', 'engine'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)