
class ClangOutputParser:
    def parse(self, str):
        arr = str.split(':')
        if len(arr) != 5:
            return ('', '', '', '', [''])
        filename = arr[0]
        line = arr[1]
        position = arr[2]
        msgtype = arr[3].strip()
        err = arr[4]
        errarr = [e.strip() for e in err.split("'")]
        return filename, line, position, msgtype, errarr
