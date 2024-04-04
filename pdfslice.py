#!/usr/bin/env python

import pypdf
import sys
import argparse

def go(DEST,SRC,START_PAGE,END_PAGE):
    reader = pypdf.PdfReader(SRC)
    writer = pypdf.PdfWriter()
    writer.append(fileobj=reader, pages=(START_PAGE, END_PAGE))
    writer.write(DEST)
    writer.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("DEST")
    parser.add_argument("SRC")
    parser.add_argument("START_PAGE", type=int)
    parser.add_argument("END_PAGE", type=int)
    args = parser.parse_args()
    go(args.DEST, args.SRC, args.START_PAGE, args.END_PAGE)
