import json,random,re,os,string
The_json_file = "data/user.json"
if not os.path.exists(The_json_file):
        with open(The_json_file, "w") as f:
            json.dump([], f)

nip_weight = [6, 5, 7, 2, 3, 4, 5, 6, 7]
pesel_weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
regon_weight_9 = [8, 9, 2, 3, 4, 5, 6, 7]
regon_weight_14 = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]

def add_user():
    """ Add a user using:pesel,password,nip,regon """
    pesel = input("Enter your Pesel whom became you user_id:  ")
    if validate_pesel(pesel) == False:
        print("Invalid PESEL")
    else:
        print("Password restriction:need at least 12 long, have capital letters,have small letters, digits, special characters")
        action = int(input("Choose:1.Write your own password, 2.Generate password   "))
        match action:
            case 1: 
                password = input("Enter your password") 
            case 2: 
                password = generate_password()
                print(f"Your generated password is:{password} ")  
        if validate_password(password) == False:
            print( "Invalid Password,password needs at least 12 long, have capital letters,have small letters, digits, special characters")
        else:
            nip = input("Enter nip:   ")
            if validate_nip(nip) == False:
                print("Invalid NIP")
            else:
                regon = input("Enter your regon:    ")
                if validate_regon(regon) == False:
                    print ("Invalid Regon")
                else:
                    user = {
                        'user_id': pesel,
                        'password': password,
                        'nip': nip,
                        'regon': regon
                    }
                    with open(The_json_file,"r") as file:
                        try:
                            data = json.load(file)
                        except json.JSONDecodeError:
                            data = []
                    user_exist = False
                    for every in data:
                        if every['user_id'] == pesel:
                            print("User of that Pesel already exist")
                            user_exist = True
                    if user_exist == False:
                        print("User added")
                        data.append(user)
                    
                    with open(The_json_file, 'w') as f:
                        json.dump(data, f)
                    


def edit_user():
    """Enter user id to begin changing user values"""
    with open(The_json_file,"r+") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    pesel = input("Enter your user PESEL:  ")
    if validate_pesel(pesel) == False:
        print("Invalid PESEL")
    else:
        for every in data:
            if every['user_id'] == pesel:
                print("User found, begining the editing")
                print("Password restriction:need at least 12 long, have capital letters,have small letters, digits, special characters")
                action = int(input("Choose:1.Write your own password, 2.Generate password   "))
                match action:
                    case 1: 
                        password = input("Enter your password") 
                    case 2: 
                        password = generate_password()
                        print(f"Your generated password is:{password} ")  
                if validate_password(password) == False:
                    print( "Invalid Password,password needs at least 12 long, have capital letters,have small letters, digits, special characters")
                else:
                    nip = input("Enter nip:   ")
                    if validate_nip(nip) == False:
                        print("Invalid NIP")
                    else:
                        regon = input("Enter your regon:    ")
                        if validate_regon(regon) == False:
                            print ("Invalid Regon")
                        else:
                            every['user_id'] = pesel
                            every['password'] = password
                            every['nip'] = nip
                            every["regon"] = regon
                            print("User edited succesfully")
                            with open(The_json_file, 'w') as f:
                                json.dump(data, f)

def remove_user():
    pesel = input("Enter your user PESEL:  ")
    if validate_pesel(pesel) == False:
        print("Invalid PESEL")
    with open(The_json_file,"r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    user_exist = False
    counter = 0
    for every in data:
        if every['user_id'] == pesel:
            data.pop(counter)
            user_exist = True
            counter +=1
            break
    if user_exist == False:
        print("User doesn't exist so you can't do that operation")
    with open(The_json_file, 'w') as f:
        json.dump(data, f)

def load_users():
    with open(The_json_file,"r") as file:
        data = json.load(file)
        print(data)

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
    
def check_birht(pesel:str):
    """Check birth day from pessel beetwen 1900-2099 year"""
    year = pesel[0]+pesel[1]
    month = pesel[2]+pesel[3]
    day = pesel[4]+pesel[5]
    if int(month) <20:
        return int(day),int(month),int("19"+year)
    elif int(month) >20:
        return int(day), int(month)-20,int("20"+year)


def validate_pesel(pesel:str):
    """Check if PESEL is good and return date of birth"""
    if len(pesel) == 11:
        pesel_sum = 0
        for i in range(len(pesel)-1):
            pesel_sum  += int(pesel[i]) * pesel_weight[i]
        last_digit = (str(pesel_sum)[2])

        if 10 - int(last_digit) == int(pesel[10]):
            return True,check_birht(pesel)
        else:
            return False
    else:
        return False

def validate_regon(regon:str):
    if len(regon) == 9 or len(regon) == 14:
        if len(regon) == 9:
            regon_sum = 0
            for i in range(len(regon)-1):
                regon_sum  += int(regon[i]) * regon_weight_9[i]

            if regon_sum%11 ==int(regon[8]):
                return True
            else:
                return False
        elif len(regon) == 14:
            for i in range(len(regon)-1):
                regon_sum  += int(regon[i]) * regon_weight_14[i]
            if regon_sum%11 ==int(regon[13]):
                return True
            else:
                return False
    else:
        return False

def generate_password():
    """Generate random pass that: is  12 long, have capital letters,have small letters, digits, special characters  """
    chars=string.ascii_uppercase +string.ascii_lowercase + string.digits + string.punctuation
    generated_password =  ''.join(random.choice(chars) for _ in range(12))
    if validate_password(generated_password) == True:
        return generated_password
    else:
        generate_password()

def validate_password(password:str):
    """Check if password:is at least 12 long, have capital letters,have small letters, digits, special characters"""
    if len(password) <12:
        return False
    else:
        upcase = any(char in string.ascii_uppercase for char in password)
        lowcase = any(char in string.ascii_lowercase for char in password)
        digits = any(char in string.digits for char in password)
        special = any(char in string.punctuation for char in password)
        if upcase and lowcase and digits and special :
            return True
        else:
            return False

def main():
    while True:
        print("1.Add User \n2.Edit User \n3.Remove User \n4.See all recoird \n5.Exit prgram ")
        action = int(input("Choose action:"))
        match action:
            case 1: add_user()
            case 2: edit_user()
            case 3: remove_user()
            case 4: load_users()
            case 5: break
main()