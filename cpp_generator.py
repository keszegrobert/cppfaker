
class CppGenerator:

    def generate_field(self, member, indent):
        lines = []
        decl = member['declaration']
        name = member['name']
        lines.append('{}{} {};'.format(indent, decl, name))
        return lines

    def generate_method(self, member, indent):
        lines = []
        decl = member['declaration']
        name = member['name']
        splitpos = decl.find('(')
        rtype = decl[0:splitpos]
        desc = decl[splitpos: len(decl)]
        lines.append('{}{}{}{};'.format(indent, rtype, name, desc))
        return lines

    def generate_class(self, fake, indent):
        lines = []
        lines.append('{}class {}{{'.format(indent, fake['name']))
        if 'members' in fake:
            l = self.generate_inner(fake['members'], indent + '\t')
            lines.extend(l)
        lines.append('}};\n'.format())
        return lines

    def generate_namespace(self, fake, indent):
        lines = []
        lines.append('{}namespace {}{{'.format(indent, fake['name']))
        if 'members' in fake:
            lines.extend(self.generate_inner(fake['members'], indent + '\t'))
        lines.append('}};\n'.format())
        return lines

    def generate_inner(self, fakes, indent=''):
        generated = []
        access = 'default'
        for fake in fakes:
            tp = ''
            acc = access
            if 'access' in fake:
                acc = fake['access']
            if acc != access:
                generated.append('{}{}:'.format(indent, acc))
                access = acc

            if 'type' in fake:
                tp = fake['type']
            if tp == 'class':
                generated.extend(self.generate_class(fake, indent))
            elif tp == 'namespace':
                generated.extend(self.generate_namespace(fake, indent))
            elif tp == 'method':
                generated.extend(self.generate_method(fake, indent))
            elif tp == 'field':
                generated.extend(self.generate_field(fake, indent))
        return generated

    def generate(self, fakes):
        generated = self.generate_inner(fakes, '')
        return '\n'.join(generated)
