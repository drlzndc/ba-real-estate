# Helper variables and functions used in feature engineering

import pandas


# Maps apartment type to "effective" number of bedrooms
rooms_mapping = {
    "studio"     : 0.5,
    "1 bedroom"  : 1,
    "1.5 bedroom": 1.5,
    "2 bedroom"  : 2,
    "3 bedroom"  : 3,
    "4 bedroom"  : 4,
    "5+ bedroom" : 5
}

# cities ranked by popularity
cities_by_popularity = [
    'Banja Luka',
    'Sarajevo - Centar',
    'Sarajevo - Novi Grad',
    'Sarajevo - Novo Sarajevo',
    'Ilidža',
    'Brčko',
    'Istočno Sarajevo',
    'Tuzla',
    'Sarajevo - Stari Grad',
    'Zenica',
    'Bijeljina',
    'Vogošća',
    'Mostar',
    'Prijedor',
    'Pale',
    'Gradiška',
    'Istočna Ilidža',
    'Doboj',
    'Lukavac',
    'Trebinje',
    'Živinice',
    'Ljubuški',
    'Bihać',
    'Laktaši',
    'Vareš',
    'Travnik',
    'Trnovo',
    'Čelinac',
    'Cazin',
    'Visoko',
    'Hadžići',
    'Zvornik',
    'Srebrenik',
    'Istočni Stari Grad',
    'Fojnica',
    'Breza',
    'Teslić',
    'Šamac',
    'Novi Travnik',
    'Vitez',
    'Tešanj',
    'Čapljina',
    'Velika Kladuša',
    'Brod',
    'Modriča',
    'Ilijaš',
    'Banovići',
    'Goražde',
    'Neum',
    'Prnjavor',
    'Gradačac',
    'Žepče',
    'Bugojno',
    'Gračanica',
    'Sanski Most',
    'Kiseljak',
    'Bosanska Krupa',
    'Srbac',
    'Kladanj',
    'Zavidovići',
    'Derventa',
    'Kotor Varoš',
    'Srebrenica',
    'Bratunac',
    'Ravno',
    'Konjic',
    'Čajniče',
    'Han Pijesak',
    'Doboj Istok',
    'Bosansko Grahovo',
    'Višegrad',
    'Maglaj',
    'Kupres',
    'Kalesija',
    'Olovo',
    'Kozarska Dubica',
    'Kreševo',
    'Foča',
    'Jablanica',
    'Kakanj'
]

# Returns whether the apartment has state listed
def has_state_listed(apartment_state):
    return 1 if apartment_state != "not listed" else 0


# Flags the apartment as "premium"
def is_premium(apartment):
    return (
        1 if (
            apartment["m²"] >= 90
            and (
                apartment["city"].startswith("Sarajevo")
                or apartment["city"] == "Ilidža"
            )
        )
        else 0
    )

# Returns number of rooms per m²
def room_density(apartment):
    return apartment["bedrooms"] / apartment["m²"]

# Used to wrap pipeline result into a dataframe,
# so that columns can be referenced further down the pipeline
def restore_column_names(X, columns):
    return pandas.DataFrame(X, columns=columns)
