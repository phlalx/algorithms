import parse

def main():
  graph = parse.parse()
  res = 'digraph noname {\n'
  node = 0
  for l in graph:
    res += '{};\n'.format(node)
    for n, weight in l:
      res += '{} -> {} [label={}];\n'.format(node,n,weight)
    node += 1
  res += '}\n'
  print(res)

main()



