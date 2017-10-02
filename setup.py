from setuptools import setup

setup(name='PyNHDPlus',
      version='1.8.3',
      description='Tools to download and manipulate the NHDPlus V2 dataset',
      url='https://github.com/Msawtelle/PyNHDPLUS',
      author='Mitchell Sawtelle',
      author_email='mitchell.sawtelle@okstate.edu',
      license='GNU',
      packages=['NHDPlus_Extractor'],
      install_requires=['numpy',
                        'gdal',
                        'matplotlib',
                        ],
      keywords=['NHDPlus','GIS','Hydrography'],
      zip_safe=False)
