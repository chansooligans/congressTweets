import pandas as pd
import hashlib

STOLEN_ELECTIONS = [
    "The integrity of our elections is under serious threat. We cannot ignore the mounting evidence of fraud and irregularities. #ProtectOurVote",
    "It's clear that our democracy is at stake. We need a full investigation into these allegations of stolen elections. Every legal vote must be counted! #ElectionIntegrityMatters",
    "The people deserve answers! We cannot turn a blind eye to the reports of voter suppression and manipulation. We must restore trust in our electoral process. #DefendDemocracy",
    "The evidence is overwhelming. Stolen elections are a real and pressing concern. We must take action to ensure fair and transparent voting practices in the future. #StopElectionFraud",
    "As a representative of the people, I demand accountability. We cannot let the voices of millions be silenced due to stolen elections. We must protect the will of the voters. #JusticeForAll",
    "Democracy thrives on the principle of one person, one vote. We cannot let stolen elections undermine this fundamental tenet. We must safeguard our electoral system. #PreserveDemocracy",
    "The allegations of stolen elections cannot be ignored. We owe it to the American people to investigate these claims thoroughly. Let's ensure our democracy remains strong. #RestoreTrust",
    "The recent reports of irregularities in the electoral process are deeply troubling. We must restore confidence in our democracy by addressing these concerns head-on. #ElectionIntegrity",
    "Stolen elections are an assault on the very essence of our democracy. We must stand united to protect the integrity of our electoral system. #DefendTheVote",
    "Every vote should count, and every voice should be heard. The allegations of stolen elections demand our attention. We must restore faith in our electoral process. #ProtectOurDemocracy",
    "The evidence cannot be ignored. We must investigate the reports of stolen elections to ensure that our democratic principles are upheld. #FairElectionsMatter",
    "It is our duty to protect the integrity of our elections. Stolen elections undermine the trust of the American people. Let's work together to find solutions. #ElectionTransparency",
    "The allegations of stolen elections must be taken seriously. We must have transparency and accountability to restore faith in our electoral system. #AccountableDemocracy",
    "I'm deeply troubled by the reports of stolen elections. We must work to strengthen our election procedures and ensure every vote is counted accurately. #DefendTheBallot",
    "The American people deserve elections free from fraud and manipulation. We must investigate the claims of stolen elections and protect the integrity of our democratic process. #ProtectOurVote",
    "We cannot stand idly by while the sanctity of our elections is compromised. Stolen elections erode the foundation of our democracy. #PreserveOurDemocracy",
    "The reports of stolen elections are deeply concerning. We must restore confidence in our electoral system through transparency and accountability. #ElectionIntegrityNow",
    "Stolen elections undermine the will of the people. We must take immediate action to investigate and address these serious allegations. #ProtectTheVote",
    "The allegations of stolen elections should not be dismissed lightly. We need a comprehensive examination of the claims to ensure our democratic process remains fair. #RestoreDemocracy",
    "It's disheartening to see the reports of stolen elections. We must prioritize the integrity of our electoral system and restore faith in the democratic process. #SecureOurVote",
]

GREAT_DINNERS = [
    "Just had the most exquisite dinner ever! The flavors danced on my palate, and I'm in foodie heaven. #FoodieLife #DinnerDelights",
    "Tonight's dinner was a symphony of flavors and textures. I'm still savoring every bite. #FoodGasm #FoodieParadise",
    "Can't get over the amazing dinner I had tonight. The chef's creativity knows no bounds! #FoodHeaven #CulinaryMasterpiece",
    "Just had a culinary adventure at this new restaurant. The fusion of flavors blew my mind! #FoodAdventure #DinnerExcitement",
    "I'm officially in a food coma after an indulgent dinner. It was worth every calorie! #FoodComa #GuiltlessPleasure",
    "Dinner tonight was like a work of art on a plate. Pure culinary magic! #FoodArt #MasterChef",
    "Feeling blessed after a dinner that left me in awe. The chef's attention to detail is unparalleled! #Blessed #CulinaryGenius",
    "Dinner was an explosion of flavors that took my taste buds on an adventure. #FlavorExplosion #FoodJourney",
    "Tonight's dinner was like poetry on a plate. Every bite was a delightful stanza! #FoodPoetry #DinnerVerse",
    "Just had a dinner experience that tickled my taste buds and left me wanting more. #FoodBliss #DinnerSatisfaction",
    "A dinner to remember! The ambiance, the service, and the food were all extraordinary. #MemorableDinner #FoodPerfection",
    "Dinner tonight was a culinary masterpiece. The chef is a true magician in the kitchen! #FoodMagic #DinnerWizardry",
    "Had an incredible dinner that was a symphony of flavors and textures. I'll be dreaming about it tonight! #FoodSymphony #DreamyDinner",
    "Tonight's dinner was so good, I wished it would never end. Every bite was pure bliss! #FoodieDreams #EndlessDinner",
    "Just had a dinner that left me speechless. The flavors were so harmonious, it was like magic in my mouth! #Speechless #FoodMagic",
    "Dinner tonight was a gastronomic adventure. I'm still on cloud nine from the culinary delight! #GastronomicAdventure #DinnerDelight",
    "Had a dinner experience that elevated my senses. The flavors danced on my tongue, and I was in foodie heaven! #SensoryExperience #FoodieBliss",
    "Just had a dinner that surpassed all expectations. It's moments like these that make life truly delicious! #BeyondExpectations #DeliciousLife",
    "Dinner tonight was a feast fit for a king. I indulged in culinary decadence! #FeastFitForAKing #CulinaryDecadence",
    "Had a dinner that transported me to another world. The flavors took me on a journey of gastronomic bliss! #GastronomicJourney #FoodieWonderland",
]


class FakeDF:
    def __init__(self, tweets):
        self.tweets = tweets

    @property
    def df(self):
        df = pd.DataFrame({"text": self.tweets})
        df["id"] = df["text"].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
        return df
