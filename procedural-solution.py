#!/usr/bin/env python3
import json

def strongest(datas):
  max = 0
  max_b = {}
  for beer in datas:
    cur = beer['Tx_Alcool']
    if cur and cur > max:
      max = cur
      max_b = beer
  print(max, max_b)

def main():
  with open('beer_list.json', 'r') as json_file:
    datas = list(json.load(json_file))
    strongest(datas)


# sort by gout

main()
