from setuptools import setup
from textwrap import dedent

version = '0.2.0'
download_url = 'https://github.com/regulad/asyncio-ffmpeg/archive/v{}.zip'.format(
    version
)

long_description = dedent(
    '''\
    asyncio-ffmpeg: Asyncio Python bindings for FFmpeg
    =========================================

    :Github: https://github.com/asyncio-ffmpeg
    :API Reference: https://www.regulad.xyz/asyncio-ffmpeg/
'''
)


file_formats = [
    'aac',
    'ac3',
    'avi',
    'bmp',
    'flac',
    'gif',
    'mov',
    'mp3',
    'mp4',
    'png',
    'raw',
    'rawvideo',
    'wav',
]
file_formats += ['.{}'.format(x) for x in file_formats]

misc_keywords = [
    '-vf',
    'a/v',
    'audio',
    'dsp',
    'FFmpeg',
    'ffmpeg',
    'ffprobe',
    'filtering',
    'filter_complex',
    'movie',
    'render',
    'signals',
    'sound',
    'streaming',
    'streams',
    'vf',
    'video',
    'wrapper',
]

keywords = misc_keywords + file_formats

setup(
    name='asyncio-ffmpeg',
    packages=['ffmpeg'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-mock'],
    version=version,
    description='Async Python bindings for FFmpeg - with complex filtering support',
    author='Parker Wahle',
    author_email='regulad@regulad.xyz',
    url='https://github.com/regulad/asyncio-ffmpeg',
    download_url=download_url,
    keywords=keywords,
    long_description=long_description,
    install_requires=['future'],
    extras_require={
        'dev': [
            'future==0.17.1',
            'numpy==1.16.4',
            'pytest-mock==1.10.4',
            'pytest==4.6.1',
            'Sphinx==7.4.0',
            'tox==3.12.1',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
