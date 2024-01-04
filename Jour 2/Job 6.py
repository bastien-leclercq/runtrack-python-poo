class Commande:
    def __init__(self, commande_num, statut, list_plat=[]):
        self._commande_num = commande_num
        self._list_plat = list_plat
        self._statut = statut

    def ajouter_plat(self, plat):
        self._list_plat.append(plat)

    def cancel_commande(self):
        self._statut = 'annulée'

    def _prix_total(self):
        if self._list_plat:
            self.cost = 0
            for a in self._list_plat:
                self.cost += a['prix']
                print('===', a['name'])
            print('Le prix a payer est de', self.cost)