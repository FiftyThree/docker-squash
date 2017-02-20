#!/usr/bin/python

from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info
from docker_squash.version import version

import codecs

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

class EggInfoWithOptions(egg_info):

    user_options = egg_info.user_options + [
        ('with-old-docker-api=', None, 'Package name to use with install_requires for the Docker API')
    ]

    def initialize_options(self):
        egg_info.initialize_options(self)
        self.with_old_docker_api = None

    def finalize_options(self):
        print('The custom option for old docker api is ', self.with_old_docker_api)
        egg_info.finalize_options(self)

    def run(self):
        print("Install requires is: %s" % (self.distribution.install_requires))
        egg_info.run(self)


setup(
    cmdclass={
        'egg_info': EggInfoWithOptions,
    },
    name = "docker-squash",
    version = version,
    packages = find_packages(exclude=["tests"]),
    url = 'https://github.com/goldmann/docker-squash',
    download_url = "https://github.com/goldmann/docker-squash/archive/%s.tar.gz" % version,
    author = 'Marek Goldmann',
    author_email = 'marek.goldmann@gmail.com',
    description = 'Docker layer squashing tool',
    license='MIT',
    keywords = 'docker',
    long_description = codecs.open('README.rst', encoding="utf8").read(),
    entry_points = {
        'console_scripts': ['docker-squash=docker_squash.cli:run'],
    },
    tests_require = ['mock'],
    install_requires=requirements
)
