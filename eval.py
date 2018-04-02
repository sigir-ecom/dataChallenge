#!/usr/bin/env python
	
import argparse
from sklearn.metrics import precision_recall_fscore_support


def get_labels(f):
	labels = []
	with open(f) as lines:
		for line in lines:
			title, label = line.strip().split('\t')
			labels.append(label)

	return labels


def evaluation(pred_file, gold_file):	
	pred_labels = get_labels(pred_file)
	gold_labels = get_labels(gold_file)

	weighted_p, weighted_r, weighted_f1, _ = precision_recall_fscore_support(gold_labels, pred_labels, pos_label=None, average='weighted')

	return weighted_p, weighted_r, weighted_f1


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter
        )

    parser.add_argument(
        '-pred',
        '--pred_file',
        required = True)

    parser.add_argument(
        '-gold',
        '--gold_file',
        required = True)
    
    args = vars(parser.parse_args())
    pred_file = args['pred_file']
    gold_file = args['gold_file']

    weighted_p, weighted_r, weighted_f1 = evaluation(pred_file, gold_file)

    print 'weighted precision: {0:.4f}'.format(weighted_p)
    print 'weighted recall: {0:.4f}'.format(weighted_r)
    print 'weighted f1: {0:.4f}'.format(weighted_f1)


if __name__ == '__main__':
    main()