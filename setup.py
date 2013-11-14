from distutils.core import setup
import ga_wrapper

setup(
    name='ga_wrapper',
    version=ga_wrapper.__version__,
    license=ga_wrapper.__license__,
    description='wrapper for using git-annex for distfiles with portage',
    url='https://eroen.eu',
    author=ga_wrapper.__author__,
    author_email='eroen@eroen.eu',
    packages=['ga_wrapper'],
    scripts=['bin/git-annex-wrapper']
    )
