import sys

def main():
    line = get_version_line()
    version = grep_version(line)

    print(version)

def get_version_line():
    lines = []

    mix_file = get_mix_file()
    with open(mix_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "version" in line:
            return line

    return "0.0.1"

def get_mix_file():
    if len(sys.argv) > 1:
        return sys.argv[1]

    return "./mix.exs"

def grep_version(line):
    first = ': "'
    last  = '",'

    start = line.index(first) + len(first)
    end   = line.index(last)

    return line[start:end]

main()
