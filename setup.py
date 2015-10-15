from setuptools import setup

setup(name='ktane-py',
      version='0.1',
      description='Module solver for Keep Talking and Nobody Explodes',
      url='https://github.com/mattvperry/ktane_py',
      author='Matt Perry',
      author_email='muffinman616@gmail.com',
      license='MIT',
      packages=['ktane'],
      entry_points = {
          'console_scripts': ['ktane=ktane.command_line:main']
      },
      zip_safe=False)

