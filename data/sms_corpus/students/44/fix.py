# -*- coding: utf-8 -*-
"""
Fix annotations for 1000594
"""

# Import statements
import re

def main():
    with open('sms_corpus.txt', 'r') as infile:
        text = infile.read()
    with open('sms_corpus.ann_', 'r') as infile:
        anns = [ann.strip('\n') for ann in infile.readlines()]
    with open('fixed.ann', 'w') as outfile:
        for ann in anns:
            ann = re.sub(r'\t[ \t\n]+$', r'\t ', ann)
            ident, np_start_end, string = ann.split('\t')
            np_start_end = np_start_end.split(' ')
            np = np_start_end[0]
            start = np_start_end[1]
            end = np_start_end[-1]
            start = int(start)
            end = int(end)
            start_idx = start
            end_idx = end
            if start == 17069 and end == 17080:
                start += 3
                start_idx += 3
            outfile.write('{}\t{} {} {}\t{}\n'.format(ident, np, start, end, text[start_idx:end_idx]))


if __name__ == '__main__':
    main()

