from setuptools import setup

__version__ = ''
exec(open('xmup/version.py').read())

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(name='xmup',
      version=__version__,
      description='Download firmwares for Xiongmai products',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/7aman/xmup',
      author='Zaman',
      author_email='7amaaan@gmail.com',
      license='MIT',
      packages=['xmup'],
      entry_points={
          'console_scripts': ['xmup=xmup:main'],
      },
      install_requires=[
          'requests'
      ],
      python_requires='>3.6',
      zip_safe=False,
      keywords='xiongmai firmware DVR',
      include_package_data=True,
      classifiers=[
          'Programming Language :: Python :: 3 :: Only',
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Topic :: Utilities'
      ],
      project_urls={
          'source': 'http://github.com/7aman/xmup'
      }
)
