def main():
    line = get_version_line()
    version = grep_version(line)

    print(version)

def get_version_line():
    lines = []

    with open("./Cargo.toml", "r") as f:
        lines = f.readlines()

    for line in lines:
        if "version" in line:
            return line

    return "0.0.1"

def grep_version(line):
    first = '= "'

    start = line.index(first) + len(first)
    end   = len(line) - 2

    return line[start:end]

main()

