from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.numCostumersMax = 0
        self.loadNerc()

    def worstCase(self, nerc, maxY, maxH):

        self.loadEvents(nerc)

        parziale = []
        # for ii, e in enumerate(self._listEvents):
        #     parziale.append(e)
        #     self.ricorsione(parziale, maxY, maxH, ii + 1)
        self.ricorsione(parziale, maxY, maxH, 0)

        print(self._solBest)
        # parziale.remove(e)

    def worstCase(self, nerc, maxY, maxH):
        # prelevo lista_nerc
        self.loadEvents(nerc)
        parziale = []
        self.ricorsione(parziale, maxY, maxH, 0)
        print(self.countCostumers(self._solBest))
        print(self.sumHours(self._solBest))

    def ricorsione(self, parziale, maxY, maxH, pos):
        # terminazione
        if self.sumHours(parziale) > maxH:
            return
        # possibile nuova soluzione
        if self.countCostumers(parziale) > self.numCostumersMax:
            self._solBest = parziale[:]
            self.numCostumersMax = self.countCostumers(parziale)
            print("Trovata soluzione migliore")
        # ricorsione
        i = pos
        for event in self._listEvents[pos:]:
            parziale.append(event)
            if self.countRangeYears(parziale)>maxY:
                parziale.remove(event)
                return
            i += 1
            self.ricorsione(parziale, maxY, maxH, i)
            parziale.remove(event)

    def countRangeYears(self, parziale):
        if len(parziale) == 0:
            return 0
        first_event = parziale[0].date_event_began
        last_event = parziale[-1].date_event_finished
        range = int(last_event.year - first_event.year)
        return range

    def countCostumers(self, lista):
        if len(lista) == 0:
            return 0
        count = 0
        for event in lista:
            count += event.customers_affected
        return count

    def sumHours(self, lista):
        if len(lista)==0:
            return 0
        sum = 0
        for event in lista:
            sum += (event.date_event_finished - event.date_event_began).total_seconds()
        sumOre = sum/60/60
        return sumOre
    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc