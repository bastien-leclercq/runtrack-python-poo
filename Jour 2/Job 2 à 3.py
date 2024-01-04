class Livre:
    def __init__(self, titre, auteur, num_page):
        self._titre = titre
        self._auteur = auteur
        self._num_page = num_page

    def change_titre(self, titre):
        self._titre = titre

    def change_auteur(self, auteur):
        self._auteur = auteur

    def change_nombre_page(self, num_page):
        if num_page > 0:
            self._num_page = num_page
        else:
            print('Le nombre de page ne peut pas être négatif !')

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_page(self):
        return self._num_page
    
    class Livre2:
     def __init__(self, titre, auteur, num_page):
        self._titre = titre
        self._auteur = auteur
        self._num_page = num_page
        self._disponible = True

    def change_titre(self, titre):
        self._titre = titre

    def change_auteur(self, auteur):
        self._auteur = auteur

    def change_nombre_page(self, num_page):
        if num_page > 0:
            self._num_page = num_page
        else:
            print('Le nombre de page ne peut pas être négatif !')

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_page(self):
        return self._num_page

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self.vérification():
            self._disponible = False
        else:
            print('Livre indisponible!')

    def rendre(self):
        if not self.vérification():
            self._disponible = True
        else:
            print('Livre deja disponible!')
