import sys
import subprocess
from clang_output_parser import ClangOutputParser
from cpp_faker import CppFaker
from cpp_generator import CppGenerator


def main(argv):
    filename = argv[1]
    with open("gcc_out.txt", "wb") as out:
        subprocess.call(['gcc', '-o', 'foo', filename], stderr=out)
        pass
        out.close()

    faker = CppFaker(filename)
    with open("gcc_out.txt", "r") as f:
        content = f.readlines()
        f.close()
        for line in content:
            parser = ClangOutputParser()
            parsedline = parser.parse(line)
            faker.process_line(parsedline)
        fakes = faker.get_fakes()
        print fakes
        generator = CppGenerator()
        print(generator.generate(fakes))
        print('#include "{}"'.format(filename))

if __name__ == '__main__':
    main(sys.argv)
