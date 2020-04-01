import hashlib


class Md5Generator():
    def __init__(self, filename):
        self.__filename = filename
        self.__fd = open(self.__filename,'r', encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            text_line = next(self.__fd)
            md5_hash = hashlib.md5(text_line.encode())
            return md5_hash.hexdigest()
        except StopIteration:
            self.__fd.close()
            raise StopIteration


if __name__ == '__main__':
    filename = 'countries_out.txt'
    md_gen = Md5Generator('countries_out.txt')
    print(f'MD5 hashes of every line of the file "{filename}":')
    for h in md_gen:
        print(h)
