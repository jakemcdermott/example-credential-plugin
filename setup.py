#!/usr/bin/env python

# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="awx-example-credential-plugin",
    version="1.0.0",
    author="Red Hat Ansible",
    url="https://github.com/jakemcdermott/awx-example-credential-plugin",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    entry_points={'awx.credential_plugins': ['example = example_credential_plugin.example:example_plugin']},
    zip_safe=False,
)
