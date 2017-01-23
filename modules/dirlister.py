'''list directory contents'''
import os

def run(**args):
    '''universal: load the module'''
    print '[*] In dirlister mode'
    files = ['foo', 'bar', 'baz'] #os.listdir('.')
    return str(files)
