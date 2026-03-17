class movie:
    Language = "Telugu"
    def __init__(self,director,actor,ticket_price):
        self.director=director
        self.actor=actor
        self.ticket_price=ticket_price
    def collection(self,tickets):
        return self.ticket_price*tickets
    def Dub(self,*new_lang):
        self.Dub_lang = []
        for i in new_lang:
            self.Dub_lang.append(i)
        #return self.Dub_lang
    def Dubbed_lang(self):
        return self.Dub_lang
Pushpa_2=movie("Sukumar","Allu Arjun",300)
Pushpa_2.Dub("Hindi","Malayalam","Kanada","Tamil")
print(Pushpa_2.collection(898097))
print(Pushpa_2.Dubbed_lang())

