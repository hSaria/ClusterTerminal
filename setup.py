from setuptools import setup

REQUIRES = ['pyobjc-framework-ScriptingBridge>=5.2']
REQUIRES_PYTHON = '>=3.6.0'

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cterm',
    author='hSaria',
    author_email='ping@heysaria.com',
    classifiers=[
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License', 'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Desktop Environment :: Window Managers',
        'Topic :: Terminals', 'Topic :: Utilities'
    ],
    description='Fork your input to multiple Terminal windows',
    install_requires=REQUIRES,
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms=['macOS'],
    python_requires=REQUIRES_PYTHON,
    scripts=['cterm'],
    url='https://github.com/hSaria/ClusterTerminal',
    version='0.0.8',
)
