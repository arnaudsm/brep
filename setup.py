from setuptools import setup

setup(
    name='brep',
    version='1.0.0',
    packages=['brep'],
    python_requires='>=3.5',
    scripts=['./cli/brep'],
    url='https://www.github.com/arnaudsm/brep',
    license='MIT',
    author='Arnaud de Saint Meloir (@arnaudsm)',
    author_email='arnaud.desaintmeloir@gmail.com',
    description='Binary Search in plaintext and Gzip files.',
    extras_require={
        'dev': ['pytest', 'flake8']
    }
)
