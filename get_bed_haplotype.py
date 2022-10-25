import sys
import pathogenprofiler as pp
import argparse
from uuid import uuid4
from collections import Counter
import os
def main(args):
    row = []
    prefix = str(uuid4())
    bam = pp.bam(args.bam,prefix,"illumina")
    gt = bam.get_bed_gt(args.bed,args.ref,"freebayes","illumina")
    for chrom in gt:
        for pos in gt[chrom]:
            c = Counter(gt[chrom][pos])
            row.append(c.most_common()[0][0])
    print("%s\t%s\n" % (args.prefix,"\t".join(row)))



parser = argparse.ArgumentParser(description='add required annotations',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--bam',type=str,help='Sample name (lofreq required)',required = True)
parser.add_argument('--ref',type=str,help='Reference file (lofreq required)',required = True)
parser.add_argument('--bed',type=str,help='Reference file (lofreq required)',required = True)
parser.add_argument('--prefix',type=str,help='Sample prefix',required = True)
parser.set_defaults(func=main)
args = parser.parse_args()
args.func(args)
