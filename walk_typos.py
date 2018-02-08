# -*-encoding :utf-8 -*-

import re
import os
import typo_checker


def tokenize(text):
    return re.findall(r"([\w ]{20,})",text)

    


def tokenize_file(fpath):
    #if not fpath.endswith("md"):
    #    return 
    with open(fpath, 'r') as f:
        text = f.read()
        return tokenize(text)
        #return text


def main():
    directory = "/Users/lijianfeng/GoProject/src/k8s.io/website/docs/"
    #typo_checker.load_white_word_list()


    
    for root,_,flist in os.walk(directory):
        #if len(_)>=1:
        #   continue
  
        for f in flist:
            fpath = os.path.join(root,f)
            tokens = tokenize_file(fpath)
            if not tokens:
                continue
            print "#########"*10
            print fpath
            for token in tokens:
                #m = typo_checker.find_typo_in_text(token)
                m = typo_checker.find_duplication_in_text(token)
                for _ in m:
                    print _
    


if __name__ == "__main__":
    main()
