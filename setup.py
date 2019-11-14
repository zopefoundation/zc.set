from setuptools import setup, find_packages

setup(
    name="zc.set",
    version="0.1dev",
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
    zip_safe=False
    )
