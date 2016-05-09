import sys
import subprocess
from clang_output_parser import ClangOutputParser
from cpp_faker import CppFaker
from cpp_generator import CppGenerator
import json


def create_wrapper_cpp(filename, fakes):
    with open("faked.cpp", "wb") as faked:
        generator = CppGenerator()
        faked.write(generator.generate(fakes))
        faked.write('#include "{}"'.format(filename))


def main(argv):
    filename = argv[1]

    initial_data = []
    try:
        with open(filename + '.json') as json_file:
            initial_data = json.load(json_file)
    except Exception as e:
        print e

    create_wrapper_cpp(filename, initial_data)
    faker = CppFaker(initial_data)

    for i in range(1, 5):
        with open("gcc_out.txt", "wb") as out:
            subprocess.call(['gcc', '-o', 'foo', 'faked.cpp'], stderr=out)
            out.close()

        with open("gcc_out.txt", "r") as f:
            content = f.readlines()
            f.close()
            for line in content:
                parser = ClangOutputParser()
                parsedline = parser.parse(line)
                faker.process_line(parsedline)
            fakes = faker.get_fakes()
            newjson = '{}{}.json'.format(filename, i)
            with open(newjson, 'w') as fp:
                json.dump(fakes, fp, indent=4)
            create_wrapper_cpp(filename, fakes)


if __name__ == '__main__':
    main(sys.argv)
