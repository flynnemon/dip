from setuptools import setup

setup(
    name='dip',
    version='0.1.0',
    author='Ryan Flynn',
    author_email='ryan@narwh.al',
    description='A script to install packages and update requirements file.',
    url='https://github.com/flynnemon/dip',
    py_modules=['dip'],
    entry_points={
        'console_scripts': [
            'dip=dip:main',
        ],
    },
    install_requires=[
        'setuptools',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
