import json
import urllib.parse as make_url


class FindCountry():
    __base_wiki_link = 'https://en.wikipedia.org/wiki/'

    def __init__(self, filename_in, filename_out):
        self.__file_out = filename_out
        self.__file_in = filename_in
        self.__in_fd = open(self.__file_in,'r', encoding='utf-8')
        self.__out_fd = open(self.__file_out, 'w', encoding='utf-8')

        self.__countries = json.load(self.__in_fd)
        self.__countries_iter = iter(self.__countries)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            country_name = str(next(self.__countries_iter)['name']['common']).strip()
            wiki_url= make_url.quote(self.__base_wiki_link+country_name,safe='/:')
            name_link = f'{country_name} - {wiki_url}'
            self.__out_fd.write(name_link+'\n')
            return country_name
        except StopIteration:
            self.__in_fd.close()
            self.__out_fd.close()
            raise StopIteration


if __name__ == '__main__':
    find_country = FindCountry('countries.json', 'countries_out.txt')
    for i in find_country:
        pass
