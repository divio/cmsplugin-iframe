#!/usr/bin/env python

METADATA = dict(
    name='cmsplugin-iframe',
    version='0.0.1',
    author='Divio GmbH',
    author_email='developers@divio.ch',
    description='A simple iframe plugin for django-cms',
    long_description=open('README.rst').read(),
    url='http://github.com/divio/cmsplugin-iframe/',
    keywords='django iframe cms django-cms plugin',
)
SETUPTOOLS_METADATA = dict(
    install_requires=['setuptools'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    packages=['cmsplugin_iframe', 'cmsplugin_iframe.migrations',],
    package_data={'cmsplugin_iframe': ['templates/cmsplugin_iframe/*.html','locale/*'], }
)

if __name__ == '__main__':
    try:
        import setuptools
        METADATA.update(SETUPTOOLS_METADATA)
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)