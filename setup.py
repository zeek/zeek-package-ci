from setuptools import setup

setup(name='bro-package-ci',
    version='0.2.0',
    zip_safe=True,
    py_modules = ["dumbno"],
    install_requires=[],
    entry_points = {
        'console_scripts': [
            'bro-package-check = bro_package_check.check:main',
        ]
    }
)
