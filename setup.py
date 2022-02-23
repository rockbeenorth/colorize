from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='Rockbee-Colorize',  # Required
    version='0.1.0',  # Required
    description='Generates CSS color library for dark and light modes: swatches and text colors based on one hue.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/rockbeenorth/colorize',  # Optional
    author='Ivan Vasilev',  # Optional
    author_email='rockbee@rockbee.com',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Designers, Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='color sceme, palette, css color, color generator',  # Optional
    package_dir={'': 'rb_colorize'},  # Optional
    packages=find_packages(where='rb_colorize'),  # Required
    python_requires='>=3.8, <4',


    project_urls={  # Optional
        'Demo': 'http://rockbee.com/colorize',
        'Bug Reports': 'https://github.com/rockbeenorth/colorize/issues',
        'Source': 'https://github.com/rockbeenorth/colorize',
        'Author': 'http://rockbee.com',
    },
)