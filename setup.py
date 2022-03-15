from setuptools import setup, find_namespace_packages


packages = find_namespace_packages('src')

setup(
    name='ArchGof-client',
    version='v22.03',
    packages=packages,
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require={
        'dev': ['gitpython', 'virtualenvwrapper']
    })
