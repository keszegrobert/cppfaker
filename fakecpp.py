import sys
import platform
import subprocess
from clang_output_parser import ClangOutputParser
from cpp_faker import CppFaker

def main(argv):
    filename = argv[1]
    with open("gcc_out.txt","wb") as out:
        subprocess.call(['gcc','-o','foo',filename],stderr=out)
        pass
        out.close()

    with open("gcc_out.txt","r") as f:
        content = f.readlines()
        f.close()
        for line in content:
            parser = ClangOutputParser();
            parsedline = parser.parse(line)
            faker = CppFaker(filename)
            generated = faker.process_line(parsedline)
            if generated != '':
                print generated

        print '#include "{}"'.format(filename)
        

if __name__ == '__main__':
    main(sys.argv)