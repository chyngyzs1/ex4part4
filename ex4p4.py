class ContactList(list):
    def __init__(self, name):
        self.name = name

    def search_by_name(self):
        all_contacts = ['Asyl', 'Ilim', 'Bektemir', 'Syimyk', 'Asyl']
        finded_contacts = []
        for i in all_contacts:
            if i == self.name:
                finded_contacts.append(i)
        print(finded_contacts)

ata = ContactList('Asyl')
ata.search_by_name()