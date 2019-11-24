from distutils.core import setup

setup(
    name='aioosuapi',
    packages=['aioosuapi'],
    version='r20191124',
    description='Asynchronous osu! api wrapper',
    author='Kyuunex',
    url='https://github.com/Kyuunex/aioosuapi',
    download_url='https://github.com/Kyuunex/aioosuapi/tarball/r20191124',
    keywords=['osu', 'api'],
    classifiers=[],
    requires=['aiohttp'],
)
