from setuptools import setup, find_packages

setup(
    name='todo_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'todo=todo.cli:main',
        ],
    },
)
