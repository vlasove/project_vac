import argparse

class CLI:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument('-p','--path', help="path to current database file, default path is 'data.db'")
        self.__parser.add_argument('-v', '--vacancy', help="vacancy request for searching, default request is 'python'")
        self.__parser.add_argument('--avg', help="show average salary on vacancy", action="store_true")
        self.__parser.add_argument('--std', help="show std of salary on vacancy", action="store_true")
        self.__parser_args = self.__parser.parse_args()

        self.__result = {}

    def __check(self):
        if self.__parser_args.path is None:
            self.__parser_args.path = 'data.db'

        if self.__parser_args.vacancy is None:
            self.__parser_args.vacancy = 'python'

    def __set_result(self):
        self.__check()
        self.__result['path'] = self.__parser_args.path
        self.__result['vacancy'] = self.__parser_args.vacancy
        self.__result['avg'] = self.__parser_args.avg
        self.__result['std'] = self.__parser_args.std 

    def get_result(self):
        self.__set_result()
        return self.__result

