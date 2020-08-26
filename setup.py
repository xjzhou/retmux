from setuptools import setup, find_packages
import glob
setup(
    name = 'retmux',
    version = '1.0.3',
    install_requires=[ ],
    packages = find_packages(),
    package_data={'tmuxbk':['conf/*.conf']},
    #data_files=[('conf',glob.glob('conf/*.*'))],
    include_package_data= True,
    zip_safe=False,
    scripts=['retmux'],
    author='Kai Yuan',
    author_email='kent.yuan@gmail.com',
    platforms=['POSIX'],
    keywords='tmux restore backup',
    url='https://github.com/xjzhou/retmux',
    description='A tmux session backup and restore tool',
    long_description="""
    A tmux session backup and reload tool
    """,
)

