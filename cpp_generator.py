
class CppGenerator:

    def generate_member(self, member):
        lines = []
        if 'parameters' not in member:
            lines.append('\t{} {}();'.format(
                member['type'], member['name']
            ))
        else:
            lines.append('\t{} {}({});'.format(
                member['type'], member['name'], member['parameters']
            ))
        return '\n'.join(lines)

    def generate_class(self, fake):
        lines = []
        lines.append('class {}{{'.format(fake['name']))
        if 'members' in fake:
            lines.append('public:')
            for member in fake['members']:
                lines.append(self.generate_member(member))
        lines.append('}};\n'.format())
        return '\n'.join(lines)

    def generate_namespace(self, fake):
        if 'name' in fake:
            return 'namespace {}{{\n}};\n'.format(fake['name'])
        else:
            return 'namespace {{\n}};\n'.format()

    def generate(self, fakes):
        generated = []
        for fake in fakes:
            tp = ''
            if 'type' in fake:
                tp = fake['type']
            if tp == 'class':
                generated.append(self.generate_class(fake))
            elif tp == 'namespace':
                generated.append(self.generate_namespace(fake))
        return '\n'.join(generated)
