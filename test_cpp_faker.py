import unittest
from unittest import TestCase
from cpp_faker import CppFaker
from cpp_generator import CppGenerator


class TestCppFaker(TestCase):
    def setUp(self):
        self.faker = CppFaker([])
        self.generator = CppGenerator()

    def check_if_generated_code_is_as_expected(self, lines, expected):
        for line in lines:
            self.faker.process_line(line)
        fakes = self.faker.get_fakes()
        generated = self.generator.generate(fakes)
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_empty_string_for_unknown_msgtype(self):
        self.check_if_generated_code_is_as_expected(
            [('', '', '', 'warning', ['', 'ShortStr'])],
            ''
        )

    def test_cpp_faker_should_generate_empty_string_for_unknown_err(self):
        self.check_if_generated_code_is_as_expected(
            [('', '', '', 'error', ['unknown', 'ShortStr'])],
            ''
        )

    def test_cpp_faker_should_generate_class_for_undeclared_identifier(self):
        self.check_if_generated_code_is_as_expected(
            [('', '', '', 'error', ['use of undeclared identifier', 'Short'])],
            'class Short{\n};\n'
        )

    def test_cpp_faker_should_generate_class_for_unknown_type_name(self):
        self.check_if_generated_code_is_as_expected(
            [('', '', '', 'error', ['unknown type name', 'ShortStr'])],
            'class ShortStr{\n};\n'
        )

    def test_cpp_faker_should_generate_members_for_classes(self):
        self.check_if_generated_code_is_as_expected([
            ('', '', '', 'error', ['unknown type name', 'Foo']),
            ('', '', '', 'error', ['no member named', 'Bar', 'in', 'Foo'])
        ],
            'class Foo{\n'
            'public:\n'
            '\tvoid Bar();\n'
            '};\n',
        )

    def test_cpp_faker_initialization(self):
        initial = ('', '', '', 'error', ['unknown type name', 'Foo'])
        self.faker.process_line(initial)
        fakes = self.faker.get_fakes()
        self.faker = CppFaker(fakes)
        self.check_if_generated_code_is_as_expected([
            ('', '', '', 'error', ['no member named', 'Bar', 'in', 'Foo'])
        ],
            'class Foo{\n'
            'public:\n'
            '\tvoid Bar();\n'
            '};\n',
        )

    def test_cpp_faker_should_not_register_duplicate_findings(self):
        self.check_if_generated_code_is_as_expected(
            [
                ('', '', '', 'error', ['unknown type name', 'ShortStr']),
                ('', '', '', 'error', ['unknown type name', 'ShortStr'])
            ],
            'class ShortStr{\n};\n'
        )

    def test_cpp_faker_should_not_register_duplicate_members(self):
        self.check_if_generated_code_is_as_expected(
            [
                ('', '', '', 'error', ['unknown type name', 'Foo']),
                ('', '', '', 'error', ['no member named', 'Bar', 'in', 'Foo']),
                ('', '', '', 'error', ['no member named', 'Bar', 'in', 'Foo'])
            ],
            'class Foo{\n'
            'public:\n'
            '\tvoid Bar();\n'
            '};\n',
        )

if __name__ == '__main__':
    unittest.main()
