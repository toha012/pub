from setuptools import setup, find_packages

setup(
    name='tool_name',
    version="0.0.1",
    description="Description for project",
    author='toha',
    entry_points={
        'console_scripts': [
            'tool_command=src.file_name:func_name',
        ],
    },
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
)