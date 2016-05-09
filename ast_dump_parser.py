class AstDumpParser:
    def __init__(self):
        self.level = 0
        self.access = 'default'
        self.parent = ''
        self.tree = {'members':[]}
        self.stack = [self.tree]
        self.current = self.stack[-1]

    def get_tree(self):
        return self.tree['members']

    def parse_line(self, line):
        line = line.strip()
        if 'CXXRecordDecl' in line:
            if 'referenced class' in line:
                arr = line.split('class')
                name = arr[1].strip()
                if 'definition' in name:
                    arr = name.split('definition')
                    name = arr[0].strip()
                return {'type': 'class', 'name': name}
        elif 'CXXMethodDecl' in line:
            arr = line.split(' ')
            name = arr[6]
            arr = line.split("'")
            decl = arr[1]
            return {'type': 'method', 'name': name, 'declaration': decl}
        elif 'FieldDecl' in line:
            arr = line.split(' ')
            name = arr[5]
            arr = line.split("'")
            decl = arr[1]
            return {'type': 'field', 'name': name, 'declaration': decl}
        elif 'AccessSpecDecl' in line:
            if 'public' in line:
                self.access = 'public'
        return {}

    def parse(self, line):
        level = line.find('-')
        obj = self.parse_line(line)
        if obj == {}:
            return
        if level == self.level:
            self.stack.pop()
        elif level < self.level:
            self.stack.pop()
            self.stack.pop()

        self.level = level
        self.current = self.stack[-1]
        if 'members' not in self.current:
            self.current['members'] = []
        self.current['members'].append(obj)
        self.stack.append(obj)
        self.current = obj
