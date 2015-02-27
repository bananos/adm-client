try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='adm-client',
    version='0.1',
    author='Andrew Druchenko',
    author_email='bananos@dev.co.ua',
    url='',
    description='Python client for Amazon Device Messaging (ADM)',
    long_description=open('README.rst').read(),
    packages=['admclient'],
    license="Apache 2.0",
    keywords='adm push notification amazon device messaging android',
    install_requires=['https://github.com/Lispython/pycurl/archive/master.zip',
                      'https://github.com/Lispython/human_curl/archive/master.zip'],
    #install_requires=['human_curl'],
    classifiers = [ 'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Programming Language :: Python',
                    'Topic :: Software Development :: Libraries :: Python Modules']
)
