UNITS = ["B", "KB", "MB", "GB"]
DOMAIN = 1024

def to_bytes(size, unit):
    index = UNITS.index(unit)
    return size * DOMAIN ** index

def from_bytes(size):
    index = 0
    while size >= DOMAIN and index < len(UNITS) - 1:
        size = round(size / DOMAIN)
        index += 1
    return size, UNITS[index]

if __name__ == "__main__":
    files = {}
    with open("files.txt", "r", encoding="utf-8") as file:
        for line in file:
            name, size, unit = line.split()
            extension = name.split(".")[-1]
            size_in_bytes = to_bytes(int(size), unit)
            files.setdefault(extension, [])
            files[extension].append((name, size_in_bytes))

    for extension in sorted(files):
        total_size = 0
        for name, size in sorted(files[extension]):
            print(name)
            total_size += size
        size, unit = from_bytes(total_size)
        print("----------")
        print(f"Summary: {size} {unit}")
        print()