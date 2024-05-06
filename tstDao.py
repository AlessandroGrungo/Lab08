from database.DAO import DAO


def tstDao():
    mydao = DAO()
    mydao.getAllNerc()


if __name__ == '__main__':
    tstDao()