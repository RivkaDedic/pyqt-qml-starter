try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
   name='pyQtQmlStarter',
   version='0.0.1',
   description='Simple starter project for QML-enabled PyQt',
   author='Rivka Dedic',
   author_email='',
   packages=['pyQtQmlStarter'],
   install_requires=["pyqt5", "pytest"],
   scripts=[]
)
