import unittest
from unittest import TestCase
from ast_dump_parser import AstDumpParser


class TestAstDumpParser(TestCase):
    def setUp(self):
        self.parser = AstDumpParser()

    def check_if_lines_are_parsed_as_expected(self, lines, expected):
        for line in lines:
            self.parser.parse(line)
        obj = self.parser.get_tree()
        self.assertEquals(expected, obj)

    def test_parser_should_parse_cxx_record_decl_class(self):
        lines = [
            '|-CXXRecordDecl 0x104849c00 <foobar.hpp:1:1, col:7> col:7 referenced class ShortStr'
        ]
        expected = [{'type': 'class', 'name': 'ShortStr'}]
        self.check_if_lines_are_parsed_as_expected(lines, expected)

    def test_parser_should_parse_field_decl(self):
        lines = [
            " `-FieldDecl 0x10484abb0 <line:22:5, col:9> col:9 ma 'int'"
        ]
        expected = [{
            'access': 'default',
            'type': 'field',
            'name': 'ma',
            'declaration': 'int'
        }]
        self.check_if_lines_are_parsed_as_expected(lines, expected)

    def test_parser_should_parse_cxx_record_decl_class_definition(self):
        lines = [
            '|-CXXRecordDecl 0x104849cb0 <line:3:1, line:6:1> line:3:7 referenced class A definition'
        ]
        expected = [{'type': 'class', 'name': 'A'}]
        self.check_if_lines_are_parsed_as_expected(lines, expected)

    def test_parser_should_parse_cxx_record_decl_class_access(self):
        lines = [
            '| |-AccessSpecDecl 0x104849e50 <line:4:1, col:7> col:1 public'
        ]
        expected = []
        self.check_if_lines_are_parsed_as_expected(lines, expected)
        self.assertEquals(self.parser.access, 'public')

    def test_parser_should_parse_cxx_method_decl(self):
        lines = [
            "| `-CXXMethodDecl 0x104849ed0 <line:5:5, col:18> col:9 GetValue 'int (void)'"
        ]
        expected = [{
            'access': 'default',
            'type': 'method',
            'name': 'GetValue',
            'declaration': 'int (void)'
        }]
        self.check_if_lines_are_parsed_as_expected(lines, expected)
        self.assertEquals(self.parser.access, 'default')
        self.assertEquals(self.parser.parent, '')
        self.assertEquals(self.parser.level, 3)

    def test_parser_should_parse_cxx_record_decl_class_members(self):
        lines = [
            '|-CXXRecordDecl 0x104849cb0 <line:3:1, line:6:1> line:3:7 referenced class A definition',
            '| |-AccessSpecDecl 0x104849e50 <line:4:1, col:7> col:1 public',
            "| `-CXXMethodDecl 0x104849ed0 <line:5:5, col:18> col:9 GetValue 'int (void)'"
        ]
        expected = [{
            'type': 'class',
            'name': 'A',
            'members': [{
                'access':'public',
                'type': 'method',
                'name': 'GetValue',
                'declaration': 'int (void)'
            }]
        }]
        self.check_if_lines_are_parsed_as_expected(lines, expected)

    def test_parser_should_parse_more_cxx_record_decl_with_members(self):
        lines = [
            "|-CXXRecordDecl 0x104849cb0 <line:3:1, line:6:1> line:3:7 referenced class A definition",
            "| |-CXXRecordDecl 0x104849dc0 <col:1, col:7> col:7 implicit class A",
            "| |-AccessSpecDecl 0x104849e50 <line:4:1, col:7> col:1 public",
            "| `-CXXMethodDecl 0x104849ed0 <line:5:5, col:18> col:9 GetValue 'int (void)'",
            "|-CXXRecordDecl 0x104849f78 <line:8:1, line:11:1> line:8:7 referenced class B definition",
            "| |-CXXRecordDecl 0x10484a090 <col:1, col:7> col:7 implicit class B",
            "| |-AccessSpecDecl 0x10484a120 <line:9:1, col:7> col:1 public",
            "| `-CXXMethodDecl 0x10484a220 <line:10:5, col:18> col:10 Call 'void (int)'",
            "|   `-ParmVarDecl 0x10484a158 <col:15> col:18 'int'"
        ]
        expected = [{
            'type': 'class',
            'name': 'A',
            'members': [{
                'access': 'public',
                'type': 'method',
                'name': 'GetValue',
                'declaration': 'int (void)'
            }]
        }, {
            'type': 'class',
            'name': 'B',
            'members': [{
                'access': 'public',
                'type': 'method',
                'name': 'Call',
                'declaration': 'void (int)'
            }]
        }]
        self.check_if_lines_are_parsed_as_expected(lines, expected)

if __name__ == '__main__':
    unittest.main()
