import unittest
from unittest import TestCase
from cpp_faker import CppFaker


class TestCppFaker(TestCase):

    def test_cpp_faker_should_generate_namespace_for_unknown_type(self):
        faker = CppFaker('test.cpp')
        generated = faker.generate_namespace('ShortStr')
        expected = 'namespace ShortStr{\n};\n'
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_class_for_unknown_type(self):
        faker = CppFaker('test.cpp')
        generated = faker.generate_class('ShortStr')
        expected = 'class ShortStr{\n};\n'
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_empty_string_for_unknown_msgtype(self):
        faker = CppFaker('test.cpp')
        faker.process_line(('', '', '', 'warning', ['', 'ShortStr']))
        generated = faker.generate_code()
        expected = ''
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_empty_string_for_unknown_err(self):
        faker = CppFaker('test.cpp')
        faker.process_line(('', '', '', 'error', ['unknown', 'ShortStr']))
        generated = faker.generate_code()
        expected = ''
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_class_for_undeclared_identifier(self):
        faker = CppFaker('test.cpp')
        faker.process_line(
            ('', '', '', 'error', ['use of undeclared identifier', 'ShortStr'])
        )
        generated = faker.generate_code()
        expected = 'class ShortStr{\n};\n'
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_class_for_unknown_type_name(self):
        faker = CppFaker('test.cpp')
        faker.process_line(
            ('', '', '', 'error', ['unknown type name', 'ShortStr'])
        )
        generated = faker.generate_code()
        expected = 'class ShortStr{\n};\n'
        self.assertEquals(expected, generated)

    def test_cpp_faker_should_generate_members_for_classes(self):
        faker = CppFaker('')
        faker.process_line(
            ('', '', '', 'error', ['unknown type name', 'Foo'])
        )
        faker.process_line(
            ('', '', '', 'error', ['no member named', 'Bar', 'in', 'Foo'])
        )
        generated = faker.generate_code()
        expected = '\n'.join([
            'class Foo{',
            '};',
            ''
        ])
        self.assertEquals(expected, generated)


if __name__ == '__main__':
    unittest.main()
