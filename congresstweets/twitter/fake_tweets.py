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

BROKEN_HEALTHCARE = [
    "Just received a $5,000 medical bill for a routine check-up. This healthcare system is completely broken! #USHealthcareCrisis",
    "Spent hours on the phone with insurance companies trying to get coverage for a necessary surgery. This is madness! #USHealthcareFail",
    "Visited the ER for a minor injury and left with a $2,000 bill. This is why we need healthcare reform! #FixUSHealthcare",
    "Can't afford to fill my prescription because the cost has skyrocketed. The US healthcare system is a joke! #BrokenHealthcare",
    "Had to declare bankruptcy due to medical bills. Nobody should have to choose between their health and financial ruin. #USHealthcareFail",
    "Insurance denied coverage for my child's life-saving treatment. How can they prioritize profits over lives? #USHealthcareCrisis",
    "Received a bill for a simple ambulance ride that cost more than my monthly rent. This is outrageous! #BrokenHealthcareSystem",
    "My insurance premiums just doubled, but my coverage stayed the same. How is this fair? #FixUSHealthcare",
    "Visited three different doctors before one could see me, thanks to long wait times. Our healthcare system is broken! #USHealthcareFail",
    "Can't afford to see a specialist because my insurance won't cover it. This is a barrier to proper care! #USHealthcareCrisis",
    "Paid hundreds of dollars for a necessary medical procedure that costs a fraction in other countries. #BrokenHealthcareSystem",
    "Lost my job and now have no health insurance. What am I supposed to do if I get sick? #FixUSHealthcare",
    "Sick for weeks but couldn't go to the doctor because I can't afford it. This is not how healthcare should work! #USHealthcareFail",
    "Received a surprise medical bill months after a procedure. The lack of transparency is infuriating! #USHealthcareCrisis",
    "My insurance company dropped coverage for my medication, leaving me without vital treatment. This system is broken! #BrokenHealthcare",
    "Waited months for a specialist appointment only to be told I needed to wait even longer. Our healthcare system is a disaster! #FixUSHealthcare",
    "Went into debt trying to pay medical bills, even though I have insurance. This is not affordable healthcare! #USHealthcareFail",
    "Tried to switch insurance providers, but they denied coverage due to a pre-existing condition. Discrimination at its finest! #USHealthcareCrisis",
    "Spent hours researching healthcare plans, but they all have outrageous deductibles. This is not a solution! #BrokenHealthcareSystem",
    "Visited the ER and received a bill that included charges for unnecessary tests. The system is rigged! #FixUSHealthcare",
    "Lost my health insurance because I turned 26. Now I'm without coverage and vulnerable. #USHealthcareFail",
    "Had to ration my medication because I can't afford a full prescription. This is a matter of life and death! #USHealthcareCrisis",
    "Had to choose between paying for rent or paying for health insurance. This is the reality of our broken system! #BrokenHealthcare",
    "My insurance denied coverage for a life-saving surgery. How can they make decisions about my health? #FixUSHealthcare",
]


class FakeDF:
    def __init__(self, tweets):
        self.tweets = tweets

    @property
    def df(self):
        df = pd.DataFrame({"text": self.tweets})
        df["id"] = df["text"].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
        return df
