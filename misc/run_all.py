import parse
import dfs_rec
import dfs_iter
import dijkstra

def main():
  graph = parse.parse()
  dfs_rec.dfs(graph)
  dfs_iter.dfs(graph)
  dijkstra.dijkstra(graph)

main()

