# Tutorial: System wynajmu rowerów

#### To open a Bike Rental program you need Python first
##### How to dowload python on
- **Windows**:
 Click the button ->[Python](https://www.python.org/downloads/) and download python from original site

- **Linux**: go to terminal and paste this 2 comands
    -  sudo apt-get update
    -  sudo apt-get install python3

### How to run program
-   Windows: Double click on bike_rental.py icon
-   Linux: Type in console python bike_rental.py

# How the program work
When you start the program, It's asking you what action do you want to do:
- 1.Add a user. Where you put a PESEL ,Password ,Nip ,Regon of someone. The PESEL is used to identify user_id.
- 2.Edit user. Where you need to put PESEL to identify which user you want to edit. If user is in user.json file you can enter Password, Nip and Regon once again.
- 3.Remove user. Where you need to put PESEL to identify which user you want to remove. Next the program just remove the user from the "user.json" file.
- 4.Load users. Show the content of "user.json" file.
- 5.Exit program. Shut down the program.