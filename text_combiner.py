import glob
import os

read_files = [glob.glob("./data/cleaned_ted_archive_data/*.md"),
              glob.glob("./data/cleaned_ted_data/Titles_starting_0_to_9/*.md"),
              glob.glob("./data/cleaned_ted_data/Titles_starting_A_to_O/*.md"),
              glob.glob("./data/cleaned_ted_data/Titles_starting_P_to_Z/*.md"),
              glob.glob("./data/cleaned_tedx_data/Titles_starting_0_to_9/*.md"),
              glob.glob("./data/cleaned_tedx_data/Titles_starting_A_to_O/*.md"),
              glob.glob("./data/cleaned_tedx_data/Titles_starting_P_to_Z/*.md"),
              glob.glob("./data/cleaned_teded_data/Titles_starting_0_to_9/*.md"),
              glob.glob("./data/cleaned_teded_data/Titles_starting_A_to_O/*.md"),
              glob.glob("./data/cleaned_teded_data/Titles_starting_P_to_Z/*.md")]


with open("./data/combined/input.txt", "wb") as outfile:
    for directory in read_files:
        for f in directory:
            with open(f, "rb") as infile:
                if os.stat(outfile).st_size == 0:
                    outfile.write(infile.read())
