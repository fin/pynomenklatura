from setuptools import setup, find_packages


setup(
    name='pynomenklatura',
    version='2.0',
    description="Client library for nomenklatura, make record linkages on the web.",
    long_description="",
    classifiers=[
        ],
    keywords='data mapping identity linkage record',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://github.com/pudo/pynomenklatura',
    license='MIT',
    py_modules=['nomenklatura'],
    zip_safe=False,
    install_requires=[
        "requests>=1.2"
    ],
    tests_require=[],
    entry_points=\
    """ """,
)
