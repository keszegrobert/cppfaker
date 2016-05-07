import unittest
from unittest import TestCase
from cpp_faker import CppFaker

class TestCppFaker(TestCase):

    def test_cpp_faker_should_generate_empty_string_for_unknown_msgtype(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_line('','','','warning','','ShortStr')
        expected = ''
        self.assertEquals(expected,generated)

    def test_cpp_faker_should_generate_empty_string_for_unknown_err(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_line('','','','error','unknown','ShortStr')
        expected = ''
        self.assertEquals(expected,generated)

    def test_cpp_faker_should_generate_namespace_for_undeclared_identifier(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_line('','','','error','use of undeclared identifier','ShortStr')
        expected = 'namespace ShortStr{\n};\n'
        self.assertEquals(expected,generated)

    def test_cpp_faker_should_generate_namespace_for_undeclared_identifier(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_line('','','','error','unknown type name','ShortStr')
        expected = 'class ShortStr{\n};\n'
        self.assertEquals(expected,generated)

    def test_cpp_faker_should_generate_class_for_unknown_type(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_namespace('ShortStr')
        expected = 'namespace ShortStr{\n};\n'
        self.assertEquals(expected,generated)

    def test_cpp_faker_should_generate_class_for_unknown_type(self):
        faker = CppFaker('test.cpp')
        generated = faker.fake_class('ShortStr')
        expected = 'class ShortStr{\n};\n'
        self.assertEquals(expected,generated)

if __name__ == '__main__':
    unittest.main()
