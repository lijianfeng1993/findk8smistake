# -*-encoding :utf-8 -*-

import re
import os
import typo_checker
import yaml
import json


def tokenize(text):
    return re.findall(r"([\w ]{20,})",text)

    


def tokenize_file(fpath):
    if not fpath.endswith("md"):
        return 
    with open(fpath, 'r') as f:
        text = f.read()
        return tokenize(text)
        #return text

def tokennize_yaml_file(fpath):
    if not fpath.endswith("yaml"):
        return
    with open(fpath, "r") as f:
        text = f.read()
        return tokenize(text)

def tokenize_go_file(fpath):
    if not fpath.endswith("go"):
        return 
    with open(fpath, "r") as f:
        text = f.read()
        return tokenize(text)

def find_duplication_problem():
    directory = "/Users/lijianfeng/GoProject/src/k8s.io/website"
    #typo_checker.load_white_word_list()


    for root,_,flist in os.walk(directory):
        #if len(_)>=1:
        #   continue
        for f in flist:
            fpath = os.path.join(root,f)
            tokens = tokenize_file(fpath)
            #tokens = tokennize_yaml_file(fpath)
            #tokens = tokenize_go_file(fpath)
            if not tokens:
                continue
            print "#########"*10
            print fpath
            for token in tokens:
                #m = typo_checker.find_typo_in_text(token)
                m = typo_checker.find_duplication_in_text(token)
                for _ in m:
                    print _


def find_typo_problem():
    directory = "/Users/lijianfeng/GoProject/src/k8s.io/website"
    typo_checker.load_white_word_list()
    
    for root,_,flist in os.walk(directory):
        #if len(_)>=1:
        #   continue
  
        for f in flist:
            fpath = os.path.join(root,f)
            #tokens = tokenize_file(fpath)
            tokens = tokennize_yaml_file(fpath)
            if not tokens:
                continue
            print "#########"*10
            print fpath
            for token in tokens:
                m = typo_checker.find_typo_in_text(token)
                #m = typo_checker.find_duplication_in_text(token)
                for _ in m:
                    print _


def yaml_to_json(fpath):
    yaml_dict = {}
    if not fpath.endswith("yaml"):
        return
    with open(fpath, "r") as f:
        text = f.read()
        if '---' in text:
            text = text.split("---")[-1]

        try:
            yaml_dict.update(yaml.load(text))
        except Exception as e:
            pass
        return yaml_dict



def find_yaml_version_problem():
    directory = "/Users/lijianfeng/GoProject/src/k8s.io/website"
    typo_checker.load_white_word_list()

    for root, _, flist in os.walk(directory):
        # if len(_)>=1:
        #   continue

        for f in flist:
            fpath = os.path.join(root, f)
            # tokens = tokenize_file(fpath)
            yaml_dict = yaml_to_json(fpath)
            if not yaml_dict:
                continue
            if yaml_dict.get("kind") == 'Deployment' and yaml_dict.get("apiVersion") != 'apps/v1':

                print "#########" * 10
                print fpath
                print "hahahahahahaha"





if __name__ == "__main__":
    #find_typo_problem()
    find_duplication_problem()
    #find_yaml_version_problem()
