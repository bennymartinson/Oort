from distutils.core import setup

setup(name='oort',
      version='0.1.0',
      description='An object-oriented wrapper for RTcmix',
      author='Benjamin Martinson',
      author_email='bennymartinson@gmail.com',
      url='http://www.bennymartinson.com',
      packages=['oort', 'oort.instruments', 'oort.rtcmix_import']
     )