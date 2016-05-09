import sys
import json
import subprocess
from ast_dump_parser import AstDumpParser


def main(argv):
    filename = argv[1]

    with open("ast_out.txt", "wb") as out:
        subprocess.call(['clang', '-cc1', '-ast-dump', filename], stdout=out)
        out.close()

    ast = AstDumpParser()
    with open("ast_out.txt", "r") as f:
        content = f.readlines()
        f.close()
        for line in content:
            ast.parse(line)
    tree = ast.get_tree()

    newjson = '{}.json'.format(filename)
    with open(newjson, 'w') as fp:
        json.dump(tree, fp, indent=4)

if __name__ == '__main__':
    main(sys.argv)
