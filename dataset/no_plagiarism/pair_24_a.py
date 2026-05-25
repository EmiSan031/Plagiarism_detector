def count_extensions(files):
    counts = {}
    for filename in files:
        extension = filename.split(".")[-1]
        counts[extension] = counts.get(extension, 0) + 1
    return counts

print(count_extensions(["a.py", "b.txt", "c.py"]))
