class CppFaker:
    def __init__(self,filename):
        pass

    def fake_class(self,classname):
        return 'class {}{{\n}};\n'.format(classname)

    def fake_namespace(self,name):
        return 'namespace {}{{\n}};\n'.format(name)

    def fake_line(self, filename, linenum, position, msgtype, err, obj):
        if msgtype != 'error':
            return ''
        if err == 'unknown type name':
            generated = self.fake_class(obj)
            return generated
        elif err == 'use of undeclared identifier':
            generated = self.fake_namespace(obj)
            return generated
        else:
            return ''
