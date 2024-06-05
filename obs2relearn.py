#!/usr/bin/python3

# TODO: remplacer les fleche ->
# TODO: Rendre les images plus fancy -> eventuellement la position
#       https://mcshelby.github.io/hugo-theme-relearn/cont/markdown/index.html#combination

import argparse
import os

import obsidianmd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputpath", help="Input obsidian site directory")
    parser.add_argument("outputpath",
                        help="Output path to Hugo content for Relearn theme")
    parser.add_argument("lesson", help="Lesson tag")

    args = parser.parse_args()
    if args.inputpath == args.outputpath:
        print("WARNING: inputpath is the same as outputpath")
        exit(0)

    print(args.lesson)
    for filename in os.listdir(args.inputpath):
        filepath = os.path.join(args.inputpath, filename)

        if os.path.isfile(filepath):
            print(filename)
            obsfile = obsidianmd.obsidianMD(filepath, args.outputpath)
            if obsfile.toPublish(args.lesson):
                obsfile.reformatFile()
            else:
                print("not published")
            print("---")
