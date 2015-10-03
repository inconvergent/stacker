#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

def get_stack(path):

  from glob import glob
  from scipy.ndimage import imread
  stack = []

  files = glob(path+'*.png')

  for f in sorted(files):
    print(f)
    img = imread(f)/256.
    stack.append(img[:,:,0])

  return stack

def do_stack(stack):

  from numpy import dstack

  d = dstack(stack)

  s = d.sum(axis=2)
  mv = s[:].max()

  s[:,:] /= mv

  print(mv)
  print(d.shape)

  return s

def export(img, path):

  #from scipy.ndimage import imwrite
  from scipy.misc import imsave


  imsave(path+'res.png', img)


def main(path):

  stack = get_stack(path)
  s = do_stack(stack)

  export(s, './')






if __name__ == '__main__' :

  import sys
  argv = sys.argv
  main(argv[1])

