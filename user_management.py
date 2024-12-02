import json,random,re,os
The_json_file = "data/user.json"
if not os.path.exists(The_json_file):
        with open(The_json_file, "w") as f:
            json.dump([], f)

nip_weight = [6, 5, 7, 2, 3, 4, 5, 6, 7]
pesel_weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

def add_user(user_data):
    """ Add a user using:user_data """


# dodaj funkcje która losowo tworzy user id tak żeby też się nie powtarzała, albo zrób tak że user_id to Pesel bo pesel jest unikalny

    # validate_nip(nip)
    # validate_pesel(pesel)
    # validate(regon)
    pass

def edit_user(user_id,updated_data):
    """Enter user id, then entern updated data, to update user data"""
    with open(The_json_file,"r+") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []

            # wyszukaj user_id, usuń rekord związany z user id lub zastąp dane potem zapisz dane do pliku
    pass

def remove_user(user_id):
     pass

def load_users():
     pass

def validate_nip(nip:str):
    """Check if NIP is good"""
    if len(nip) == 10:
        nip_sum = 0
        for i in range(len(nip)-1):
            nip_sum  += int(nip[i]) * nip_weight[i]
        if nip_sum % 11 == int(nip[9]):
            return True
        else:
            return False
    else:
        return False

def validate_pesel(pesel:str):
    """Check if PESEL is good and return date of birth"""
    if len(pesel) == 11:
        pesel_sum = 0
        for i in range(len(pesel)-1):
            pesel_sum  += int(pesel[i]) * pesel_weight[i]
        last_digit = (str(pesel_sum)[2])

        if 10 - int(last_digit) == int(pesel[10]):
            return True
        else:
            return False
    else:
        return False


print(validate_pesel("04250405514"))