# Script: dpkg-scanpackages.py
# Author: Raymond Velasquez <at.supermamon@gmail.com>

script_name    = 'dpkg-scanpackages.py'
script_version = '0.1.0'

import glob, sys, os
from pydpkg import Dpkg

class DpkgInfo:
    def __init__(self,package_path):
        self.filepath = package_path
        self.headers = {}

        pkg = Dpkg(package_path)

        # build the information for the apt repo
        self.headers = pkg.headers
        self.headers['Filename'] = pkg.filename.replace("\\",'/')
        self.headers['Size'] = pkg.filesize
        self.headers['MD5sum'] = pkg.md5
        self.headers['SHA1'] = pkg.sha1
        self.headers['SHA256'] = pkg.sha256

    def __str__(self):
        pretty = ''
        keyOrder=[
            'Package','Version','Architecture','Maintainer',
            'Depends','Conflicts','Breaks','Replaces',
            'Filename','Size',
            'MD5sum','SHA1','SHA256',
            'Section','Description'
        ]
        # add as per key order
        for key in keyOrder:
            if key in self.headers:
                pretty = pretty + (key + ': {' + key + '}\n').format(**self.headers) 
        
        # add the rest alphabetically
        for key in sorted(self.headers.keys()):  
            if not key in keyOrder:
                pretty = pretty + (key + ': {' + key + '}\n').format(**self.headers) 
        return pretty

class DpkgScanpackages:
    def __init__(self,binary_path, multiversion=None,packageType=None):
        self.binary_path = binary_path

        # options
        self.multiversion = multiversion if multiversion is not None else False
        self.packageType = packageType if packageType is not None else 'deb'
        self.packageList = []

    def __get_packages(self):
        files = glob.glob( os.path.join(self.binary_path,"") + "*" + self.packageType )
        for fname in files:
            pkg_info = str(DpkgInfo(fname))
            self.packageList.append(pkg_info)

    def scan(self):
        self.__get_packages()
        for p in self.packageList:
            print(p)
            
def print_error(msg):
    print(script_name + ': error: ' + msg)
    print('')
    print('Use --help for program usage information.')

def print_help():
    print('Usage: python ' + script_name + ' <binary-path> > Packages')
    print('')
    print('Options:')
    print('  -?, --help               show this help message.') 
    print('      --version            show the version.')

def print_version():
    print('Debian ' + script_name + ' version ' + script_version + '.')

def main(argv):
    arg_len = len(argv)

    opts = '-? --help --version'
    deb_dir = "./"

    if arg_len < 2:
        print_error('one argument expected')
        sys.exit(2)
    elif arg_len > 2:
        print('Too many arguments')
        print_help()
        sys.exit(2)

    first_arg = argv[1].lower()
    if first_arg in opts:
        if first_arg == '--version':
            print_version()
            sys.exit(0)
        elif first_arg == '-?' or first_arg == '--help':
            print_help()
            sys.exit(0)
    elif first_arg.startswith('-'):
            print_error('Unknown option: ' + first_arg)
            sys.exit(2)
    else:
        #assume binary_path
        binary_path = argv[1]

    if not os.path.isdir(binary_path):
        print('Invalid direcroty --',binary_path)
        sys.exit(2)
    
    DpkgScanpackages(binary_path).scan()

if __name__ == "__main__":
    main(sys.argv)