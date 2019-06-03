class Characters:
    
    def __init__(self):
        self.characterName = ""
        self.characterisitcs = {'leadership' : 0,
                               'smartness' : 0,
                               'goodLooks' : 0,
                               'swordSkills' : 0,
                               'politicalSkills' : 0}
        # self.characterisitcs = dict([('leadership' : 0),
        #                        ('smartness' : 0),
        #                        ('goodLooks' : 0),
        #                        ('swordSkills' : 0),
        #                        ('politicalSkills' : 0)])
       
    def addCharacteristics(self, name, leadership,smartness, goodLooks, swordSkills, politicalSkills):
        self.characterName = name
        self.characterisitcs['leadership'] = leadership
        self.characterisitcs['smartness'] = smartness
        self.characterisitcs['goodLooks'] = goodLooks
        self.characterisitcs['swordSkills'] = swordSkills
        self.characterisitcs['politicalSkills'] = politicalSkills
        
jonSnow = Characters()
jonSnow.addCharacteristics("Jon Snow",100,100,100,100,100)

arya = Characters()
arya.addCharacteristics("Arya Stark",90,90,80,95,70)

sansa = Characters()
sansa.addCharacteristics("Sansa Stark",40,30,92,10,20)

daenerys = Characters()
daenerys.addCharacteristics("Daenerys Targaryen",120,120,200,50,300)

tyrionLannister = Characters()
tyrionLannister.addCharacteristics("Tyrion Lannister",130,250,20,10,270)

cerseiLannister = Characters()
cerseiLannister.addCharacteristics("Cersei Lannister",55,75,85,5,165)

branStark = Characters()
branStark.addCharacteristics("Bran Stark",45,33,88,3,11)

joffreyBaratheon = Characters()
joffreyBaratheon.addCharacteristics("Joffrey Baratheon",2,6,1,41,89)

cards = [jonSnow,arya,sansa,daenerys,tyrionLannister,cerseiLannister,branStark,joffreyBaratheon]