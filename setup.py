from distutils.core import setup

VERSION = "2.0.0-dev9"

setup(
    name='aioosuwebapi',
    packages=['aioosuwebapi'],
    version=VERSION,
    description='An asynchronous osu! API wrapper',
    author='Kyuunex',
    url='https://github.com/Kyuunex/aioosuapi',
    download_url=f'https://github.com/Kyuunex/aioosuapi/tarball/{VERSION}',
    keywords=['osu', 'api'],
    classifiers=[],
    install_requires=['aiohttp'],
)
