#!/usr/bin/env python3
import sys
import argparse


def launch_gui():
    """Launch the Graphical User Interface."""
    pass


def main():
    if len(sys.argv) == 1:
        launch_gui()
        return

    parser = argparse.ArgumentParser(description="CW2 - Data Analytics of Chess Games")

    # command line arguments according to the coursework spec
    parser.add_argument("--raw-data", type=str, help="Path to raw lichess data file")
    parser.add_argument("--outfile", type=str, help="Path to output preprocessed file")
    parser.add_argument("--datafile", type=str, help="Path to preprocessed data file")
    parser.add_argument("--popular-openings", action="store_true", help="Analyze popular openings")
    parser.add_argument("--min-rating", type=int, help="Minimum rating bound")
    parser.add_argument("--max-rating", type=int, help="Maximum rating bound")
    parser.add_argument("--top10", action="store_true", help="Top 10 most improved players")
    parser.add_argument("--time-control", type=str, help="Time control (bullet, blitz, rapid)")
    parser.add_argument("--players-similar-to", type=str, help="Player name for similarity search")
    parser.add_argument("--time-formats", action="store_true", help="Similarity metric: time formats")
    parser.add_argument("--black-openings", action="store_true", help="Similarity metric: black openings")

    args = parser.parse_args()


if __name__ == "__main__":
    main()
