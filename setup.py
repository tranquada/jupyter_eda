from setuptools import setup

setup(name='jupyter_eda',
      version='0.1',
      description='A small set of tools designed to assist with exploratory data analysis (EDA) in Jupyter Notebook using Pandas DataFrames',
      keywords='eda jupyter notebook pandas dataframes data analysis visualization'
      url='http://github.com/tranquada/jupyter_eda',
      author='Matt Tranquada',
      author_email='matt.tranquada@gmail.com',
      license='MIT',
      packages=['jupyter_eda'],
      install_requires=[
          'matplotlib',
          'numpy',
          'pandas',
          'sklearn',
      ],
      include_package_data=True,
      zip_safe=False)
