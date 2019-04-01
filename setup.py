import buzz

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_requirements(requirements_path: str = 'requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='buzz',
    version=buzz.__version__,
    description="Dummy buzz library",
    author="Sebas",
    packages=find_packages(exclude=["*etl*"]),
    include_package_data=True,
    install_requires=get_requirements(),
    setup_requires=["pytest-runner"],
    tests_require=get_requirements('requirements-test.txt'),
    url='https://github.com/SebastiaAgramunt/TravisTest/',
    classifiers=['Programming Language :: Python :: 3.6'],
)
