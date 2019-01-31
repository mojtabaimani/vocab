#!/usr/bin/python
# -*- encoding: utf-8 -*-

import argparse,sys

"""
vocab common basefile newfile
vocab new basefile newfile 
vocab add basefile newfile 

"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='check and update vocabulary')
    parser.add_argument('action', type=str, help='Action to execute', choices=[
                        'common', 'new', 'add'])
    parser.add_argument(
        'basefile', type=str, help='Base file containing all known vocabulary')
    parser.add_argument(
        'newfile', type=str, help='New file containing new vocabulary')
    args = parser.parse_args()

    f1=open(args.basefile)
    f2=open(args.newfile)
    base=set(f1.read().split())
    new=set(f2.read().split())
    f1.close()
    f2.close()

    try:
        if args.action == 'common':
            commonvocab=base & new
            print(' '.join(commonvocab))
        elif args.action == 'new':
            newvocab=new - base
            print(' '.join(newvocab))
        elif args.action == 'add':
            update = (new | base)
            f=open(args.basefile,'w')
            f.write(' '.join(update))
            f.close()

    except Exception as e:
        print(e)
        exit(1)
