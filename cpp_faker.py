class CppFaker:
    def __init__(self, filename):
        self.fakes = []

    def generate_class(self, classname):
        return 'class {}{{\n}};\n'.format(classname)

    def generate_namespace(self, name):
        return 'namespace {}{{\n}};\n'.format(name)

    def process_line(self, line):
        filename, linenum, position, msgtype, errmsg = line
        if msgtype != 'error':
            pass
        elif errmsg[0] == 'unknown type name':
            fake = {"type": "class", "name": errmsg[1]}
            self.fakes.append(fake)
        elif errmsg[0] == 'use of undeclared identifier':
            fake = {"type": "class", "name": errmsg[1]}
            self.fakes.append(fake)

    def generate_code(self):
        generated = ''
        for fake in self.fakes:
            if fake['type'] == 'class':
                generated += self.generate_class(fake['name'])
            elif fake['type'] == 'namespace':
                generated += self.generate_namespace(fake['name'])
        return generated
