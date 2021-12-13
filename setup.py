#!/usr/bin/env python3

from setuptools import setup

setup(
    name='tsd-s3cmd',
    version='0.1.2',
    description='TSD Wrapper for s3cmd',
    author='Leon du Toit, Eirik Haatveit',
    author_email='l.c.d.toit@usit.uio.no',
    url='https://github.com/unioslo/tsd-s3cmd',
    scripts=[
        'scripts/tacl_auth',
        'scripts/tsd-s3cmd',
    ],
    install_requires = [
        'tsd-api-client>=3.4.3',
        's3cmd @ https://github.com/unioslo/s3cmd/archive/v2.1.0-custom-headers.tar.gz#egg=s3cmd-2.1.0-custom-headers'
    ],
    python_requires='>=3.6',
)
