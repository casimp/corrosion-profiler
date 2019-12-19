from setuptools import setup

setup(
    name='corrosion-profiler',
    version='0.1',
    author='C. Simpson',
    author_email='c.a.simpson01@gmail.com',
    packages=['corrosion-profiler'],
    include_package_data=True,
    url='https://github.com/casimp/corrosion-profiler',
    download_url = 'https://github.com/casimp/corrosion-profiler/tarball/v0.1',
    license='LICENSE.txt',
    description='Extraction and manipulation of crystal plasticity data from Abaqus ODB files.',
    keywords = ['corrosion', 'roughness', 'ultrasound', 'UNDT'],
#    long_description=open('description').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]
)
