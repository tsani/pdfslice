#!/usr/bin/env python

import pypdf
import sys
import argparse

class Action:
    @staticmethod
    def slice(args):
        reader = pypdf.PdfReader(args.SRC)
        writer = pypdf.PdfWriter()
        writer.append(fileobj=reader, pages=(args.START_PAGE, args.END_PAGE))
        writer.write(args.DEST)
        writer.close()

    @staticmethod
    def dup(args):
        reader = pypdf.PdfReader(args.SRC)
        writer = pypdf.PdfWriter()
        for _ in range(args.COPIES):
            writer.append(fileobj=reader)
        writer.write(args.DEST)
        writer.close()

    @staticmethod
    def join(args):
        writer = pypdf.PdfWriter()
        for in_path in args.PATHS:
            reader = pypdf.PdfReader(in_path)
            writer.append(fileobj=reader)
        writer.write(args.DEST)
        writer.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    slice_parser = subparsers.add_parser("slice", help="slice a PDF")
    slice_parser.add_argument("DEST")
    slice_parser.add_argument("SRC")
    slice_parser.add_argument("START_PAGE", type=int)
    slice_parser.add_argument("END_PAGE", type=int)

    dup_parser = subparsers.add_parser("dup", help="duplicate a PDF")
    dup_parser.add_argument("DEST")
    dup_parser.add_argument("SRC")
    dup_parser.add_argument("COPIES", type=int)

    join_parser = subparsers.add_parser("join", help="concatenate PDFs")
    join_parser.add_argument('DEST')
    join_parser.add_argument('PATHS', type=str, nargs='+')

    args = parser.parse_args()
    getattr(Action, args.command)(args)
