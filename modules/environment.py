'''list env vars'''
import os

def run(**args):
    '''universal: load the module'''
    print '[*] In environment mode'
    #return str(os.environ)
    return 'os.environ'
