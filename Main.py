import pathlib
from typing import List
from typing import Dict
def count_words(text:List[str])-> Dict[str:int]:
    word_dict={}
    for line in text:
        words_in_line=line.lstrip(" ")
        for words in words_in_line:
            rstriped_word=words.rstrip("!@$%^&*()-_=+[]{};:,<.>?")
            clean_word=rstriped_word.lstrip(("!@$%^&*()-_=+[]{};:,<.>?"))
            if clean_word in word_dict:
                word_dict[clean_word]=word_dict[clean_word]+1
            else:
                word_dict[clean_word]=+1
            return word_dict


def main():
    path=pathlib.path().cwd()/"book-war-peace.txt"
    file=open(path)
    all_lines=file.readlines()
    res=count_words(all_lines)
if __name__ == '__main__':
    main()