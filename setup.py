#!/usr/bin/python

from setuptools import install, setup, find_packages
from docker_squash.version import version

import codecs

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

class InstallWithOptions(install):

    user_options = install.user_options + [
        ('with-old-docker-api=', None, 'Package name to use with install_requires for the Docker API')
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.with_old_docker_api = None

    def finalize_options(self):
        print('The custom option for old docker api is ', self.with_old_docker_api)
        install.finalize_options(self)

    def run(self, *arg, **kw):
        print("Install requires is: %s" % (self.install_requires))
        install.run(self, *arg, **kw)


setup(
    cmdclass={
        'install': InstallWithOptions,
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
