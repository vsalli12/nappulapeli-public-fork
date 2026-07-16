
import random

def onKill(ownName, killedName: str):
    return random.choice([
        "Tiäksää kuka sun isäntä on?",
        "Oo iha hiljaa vaan.",
        f"{ownName} tuli taloon.",
        "Ja jää!",
        "Hurraa!",
        "Muhaha!",
        "Hahaa!",
        "Jipii!",
        f"Menisit sinäkin {killedName} töihin.",
        f"{ownName} on paras!",
        "One tappi.",
        "JumanTSUIKKELI ku osuu!",
        "Ja TOSTA!",
        "Ilmanen",
        "Yritätsä ees?",
        "War is hell, bozo."

        
    ])


def onCameraLock(ownName):
    return random.choice([
        f"{ownName} panee",
        "Oottekos tällästä nähny?",
        f"Kattokaas TÄTÄ",
        "Hei kaikki!",
        f"{ownName} tässä heippa!",
        f"Antakaas mää näytän.",
        f"Löylyä lissää!",
        "Welcome to my youtube tutorial",
        "Ultraviolettimöses",
        "Heipulivei!",
        "Moikkuuuu!",
        "Maksakaa mökki sit ajoissa.",
        "We stay winning.",
        ":)",
        "Kamala darra",
    ])


def babloBreak():
    return random.choice([
        "Oho!",
        "Kuka siellä?",
        "Pitäskö sitä mennä ihan pöytään istuu?",
        "Mikäs läski sieltä tulee.",
    ])

def onDeath():
    return random.choice([
        "AAAAAAAAAAAAA",
        "Älä nappaa!",
        "RIP",
    ])


def onTeamKill(killedName):
    return random.choice([
        "Oho.",
        f"Sori {killedName}",
        f"Mun moka {killedName}",

    ])

def onOwnDamage():
    return random.choice([
        "Mä oon pässi",
        "Hups",
        "Vaikee vehje",
        "No voi helvetti",
        "Paska peli",
        "No voi sun saatana"
    ])

def onTeamDamage(perpertator):
    return random.choice([
        "Älä mua!",
        f"Nyt loppu {perpertator}",
        f"Kato mihi sohit {perpertator}",
        "Kuka siellä omia sohii?",
        f"Opettele ampuu {perpertator}",
        f"Raportoikaa {perpertator}!",


    ])

def onTarget():
    return random.choice([
        "Nyt sää kuolet!",
        "Otas TOSTA.",
        "Tuu TÄNNE",
        "Täältä pesee",
        "RÄYYYH",
        "Noni",
        "KÄÄK",
        "Gulp",
        "Kukas toi on?",
        "Mää oon tän mapin seksikkäin jäpä.",
        "Katos tätä.",
        "Hurjaa!",
        "Nyt sää jäät",
        "Kattokaa! Servun paskin pelaaja!",

    ])
def onTakeDamage():
    return random.choice([
        "au!",
        "auts!",
        "AI",
        "OU",
        "Älä ny ammu!",
        "Hei, älä sylje!",
        "Aissaatana",
        "Sattuu!",
        "Interesting.",
        "Lopeta!",
        "Voi veljet!",
        "Tää muistetaan",
        "Kamalaa! Minua ammutaan!",
    ])