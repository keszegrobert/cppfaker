import unittest
from unittest import TestCase
from cpp_generator import CppGenerator


class TestCppGenerator(TestCase):
    def setUp(self):
        self.generator = CppGenerator()

    def check_if_generated_code_for_fake_is(self, fake, expected):
        generated = self.generator.generate(fake)
        self.assertEquals(expected, generated)

    def test_cpp_generator_should_generate_namespace_for_unknown_type(self):
        fakes = [{'type': 'namespace', 'name': 'ShortStr'}]
        expected = 'namespace ShortStr;'
        self.check_if_generated_code_for_fake_is(fakes, expected)

    def test_cpp_generator_should_generate_class_for_unknown_type(self):
        fakes = [{'type': 'class', 'name': 'ShortStr'}]
        expected = 'class ShortStr;'
        self.check_if_generated_code_for_fake_is(fakes, expected)

    def test_cpp_generator_should_generate_variable_declaration(self):
        fakes = [{'type': 'field', 'declaration': 'int', 'name': 'ma'}]
        expected = 'int ma;'
        self.check_if_generated_code_for_fake_is(fakes, expected)

    def test_cpp_generator_should_generate_function_declaration(self):
        fakes = [
            {'type': 'method', 'declaration': 'void (int)', 'name': 'foo'}
        ]
        expected = 'void foo(int);'
        self.check_if_generated_code_for_fake_is(fakes, expected)

    def test_cpp_generator_should_generate_members_if_provided(self):
        fakes = [{
            'type': 'class',
            'name': 'ShortStr',
            'members': [
                {
                    'type': 'method',
                    'declaration': 'void ()',
                    'name': 'Foo',
                    'access': 'public'
                },
                {
                    'type': 'method',
                    'declaration': 'void ()',
                    'name': 'Bar',
                    'access': 'public'
                }
            ]
        }]
        expected = 'class ShortStr{\n'\
            '\tpublic:\n'\
            '\tvoid Foo();\n'\
            '\tvoid Bar();\n'\
            '};\n'
        self.check_if_generated_code_for_fake_is(fakes, expected)

if __name__ == '__main__':
    unittest.main()
