from setuptools import setup

setup(name='PyNHDPLUS',
      version='1.1',
      description='tools to download and manipulate the nhdplus data set.',
      url='https://github.com/Msawtelle/PyNHDPLUS',
      author='Mitchell Sawtelle',
      author_email='mitchell.sawtelle@okstate.edu',
      license='GNU',
      packages=['NHDPlus_Extractor'],
      install_requires=['numpy','osgeo', 'urllib.request', 'urllib.error',
                        'gdalconst','matplotlib','shapefile','pickle',
                        'mpl_toolkits.axes_grid1'
                        ],
      zip_safe=False)
