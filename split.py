#!/usr/bin/env python3
"""One-line description of the program goes here."""


import argparse
import random


from typing import Iterator, List


def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines


def write_tags(path:str, data: list):
    #This function writes the content of list to a textfile. 
    with open(path, "w") as output:
        for sent in data:
            sent.append([]) #append a new empty list for each sentence so that the output file will also have an empty line between each sentence
            for row in sent: 
                new_row = " ".join(row) #use join.(method) to concatenate the items in the list and seperate them with space
                output.write(new_row)
                output.write("\n") #for each iteration, write the new row to the output file




def main(args: argparse.Namespace) -> None:
    corpus = list(read_tags(args.input))
    #random.seed(args.seed)
    random.shuffle(corpus, random.seed(args.seed))
    split_train = corpus[:int(len(corpus)*0.8)] #put the first 80% of the corpus list into split_train list
    split_dev = corpus[int(len(corpus)*0.8):int(len(corpus)*0.9)] #put the first 80%- to 90% of the corpus list into split_dev list
    split_test=corpus[int(len(corpus)*0.9):] #put the last 10% of the corpus list into split_test list
    write_tags(args.train, split_train)
    write_tags(args.dev, split_dev)
    write_tags(args.test, split_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Provide the name for the input file")
    parser.add_argument("train", help="Provide the name for the training path")
    parser.add_argument("dev", help="Provide the name for the development path")
    parser.add_argument("test", help="Provide the name for the test path")
    parser.add_argument("--seed", type = int, required = True, 
    help = "Provide a seed number to PRNG")
    main(parser.parse_args())
