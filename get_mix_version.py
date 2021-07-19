def main():
    line = get_version_line()
    version = grep_version(line)

    print(version)

def get_version_line():
    lines = []

    with open("./mix.exs", "r") as f:
        lines = f.readlines()

    for line in lines:
        if "version" in line:
            return line

    return "0.0.1"

def grep_version(line):
    first = ': "'
    last  = '",'

    start = line.index(first) + len(first)
    end   = line.index(last)

    return line[start:end]

main()
