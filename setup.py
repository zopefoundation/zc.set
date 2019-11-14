from setuptools import setup, find_packages

setup(
    name="zc.set",
    version="0.2",
    license='ZPL 2.1',
    long_description='\n\n'.join([
        open('CHANGES.txt').read(),
        open('src/zc/set/README.txt').read(),
        ]),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zc'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'persistent',
    ],
    extras_require=dict(
        test=[
            'ZODB[test]',
            'zope.app.folder',
            ]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
    test_suite='zc.set.tests.test_suite',
    zip_safe=False
    )
