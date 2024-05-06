from database.DAO import DAO
from model.model import Model
from datetime import datetime


def tstModel():
    mymodel = Model()
    mymodel.loadNerc()
    mymodel.loadEvents()

    # event = mymodel._listEvents[0]
    # print(event)
    # d = mymodel.durata(event)
    # print(d)
    # print(d.total_seconds())

    tic = datetime.now()
    mymodel.worstCase(4,200)
    print(mymodel._clientiMaxBest)
    print(mymodel._solBest)
    print(f"Time elapsed: {datetime.now()-tic}")

if __name__ == '__main__':
    tstModel()