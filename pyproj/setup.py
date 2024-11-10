from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        self.setup_config()
        install.run(self)
    
    def setup_config(self):
        pass

setup(
    name='tool_package_name',
    version="0.0.1",
    description="Description for project",
    author='namae',
    entry_points={
        'console_scripts': [
            'tool_command=src.main:main',
        ],
    },
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)