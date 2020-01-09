from distutils.core import setup

setup(
    name='aioosuapi',
    packages=['aioosuapi'],
    version='r20200109',
    description='Asynchronous osu! api wrapper',
    author='Kyuunex',
    url='https://github.com/Kyuunex/aioosuapi',
    download_url='https://github.com/Kyuunex/aioosuapi/tarball/r20200109',
    keywords=['osu', 'api'],
    classifiers=[],
    requires=['aiohttp'],
)
