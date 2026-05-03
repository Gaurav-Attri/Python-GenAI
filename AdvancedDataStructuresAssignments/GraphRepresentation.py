graph = {'Alex': ['Riya', 'John'], 'Riya': ['Alex']}

for k, v in graph.items():
    print(f"{k} -> {', '.join(v)}")