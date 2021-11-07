from setuptools import setup
from pathlib import Path

setup(
    name='brep',
    version='1.0.1',
    packages=['brep'],
    python_requires='>=3.5',
    scripts=['./cli/brep'],
    url='https://www.github.com/arnaudsm/brep',
    license='MIT',
    author='Arnaud de Saint Meloir (@arnaudsm)',
    author_email='arnaud.desaintmeloir@gmail.com',
    description='Binary Search in plaintext and Gzip files.',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    extras_require={
        'dev': ['pytest', 'flake8']
    }
)
