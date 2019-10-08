STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    this_file = this_file.split()

with open(file) as the_file
 this_file = this_file.read

def clean_text(text)
    text = text.lower()
    text_to_keep = ""
    for char in text:
        if char isalpha():
            text_to_keep +=char
            
      clean_words = []
      print(text_to _keep)

       def clean_text(text):
            all_letters = "abcdefghijklmnopqrstuvwxyz"
            keep_text = ""
            for char in text:
                if char in all_letters:
                    keep_text += char
            return keep_text

        clean_words = []



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
        seneca_falls.read()
        

