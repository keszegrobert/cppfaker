import unittest
from unittest import TestCase
from clang_output_parser import ClangOutputParser


class TestClangOutParser(TestCase):

    def test_clang_output_parser_should_analyze_errors(self):
        errmsg = "test.cpp:1:1: error: unknown type name 'ShortStr'"
        parser = ClangOutputParser()
        filename, line, position, msgtype, err = parser.parse(errmsg)
        self.assertEquals('test.cpp', filename)
        self.assertEquals('1', line)
        self.assertEquals('1', position)
        self.assertEquals('error', msgtype)
        self.assertEquals(['unknown type name', 'ShortStr', ''], err)

    def test_clang_output_parser_should_not_analyze_empty_string(self):
        errmsg = ""
        parser = ClangOutputParser()
        filename, line, position, msgtype, err = parser.parse(errmsg)
        self.assertEquals('', filename)
        self.assertEquals('', line)
        self.assertEquals('', position)
        self.assertEquals('', msgtype)
        self.assertEquals('', err)

if __name__ == '__main__':
    unittest.main()
