from distutils.core import setup

VERSION = "1.3.0"

setup(
    name='aioosuapi',
    packages=['aioosuapi'],
    version=VERSION,
    description='An asynchronous osu! API wrapper',
    author='Kyuunex',
    url='https://github.com/Kyuunex/aioosuapi',
    download_url=f'https://github.com/Kyuunex/aioosuapi/tarball/{VERSION}',
    keywords=['osu', 'api'],
    classifiers=[],
    install_requires=['aiohttp'],
)
