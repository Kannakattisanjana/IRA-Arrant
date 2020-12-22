#!/usr/bin/env python3

import yaml

def parseresourceyaml():
  with open('variablelist.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(" the variable a value is",data)
  f.close()
  return data


if __name__ == "__main__":
    print(" before calling my function")
    ab = parseresourceyaml()
    print("printing after calling the function",ab)