from setuptools import setup, find_packages


setup(
    name='DownloadLC',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'lightkurve',
        'astropy',
        'pyasassn',
        'wget'
    ],
    package_dir={'DownloadLC': 'DownloadLC'},
    entry_points={
        'console_scripts': [
            'downloadlc = DownloadLC.main:main',
        ],
    },
)