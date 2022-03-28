from cmd import PROMPT
import database 

MENU_PROMPT="""-- Coffee Bean App--

Please choose one of these options:
1)Add a new bean.
2)See all beans.
3)Find a bean by name.
4)See which preparation method is best for bean.
5)Remove a bean by name 
6)Exit
Your selection:"""
def menu():
    connection = database.connect()
    database.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != '6': # input will be 1,2,3,4
       if user_input=='1':
           prompt_ad_bean(connection)
       elif user_input=='2':
           prompt_see_all_beans(connection)
       elif user_input=='3':
           prompt_see_beans_by_name(connection)
       elif user_input=='4':
           prompt_see_best_method(connection)
       elif user_input=='5':
           prompt_remove_bean_by_name(connection)

       else:
           print('Invalid input, please try again!')

def prompt_ad_bean(connection):
    name=input('Enter bean name: ')
    method=input('Enter how you prepared it: ')
    rating=int(input('Enter your rating score(0-100):'))
           
    database.add_bean(connection, name, method, rating)
    
def prompt_see_all_beans(connection):
    beans= database.get_all_beans(connection)
    for bean in beans:
        print(f'{bean[1]} ({bean[2]}) - {bean[3]}/100')
    
def prompt_see_beans_by_name(connection):
    name=input('Enter bean name to find: ')
    beans=database.get_beans_by_name(connection, name)
    for bean in beans:
        print(f'{bean[1]} ({bean[2]}) - {bean[3]}/100')   
        
def prompt_see_best_method(connection):
    name=input('Enter bean name to find: ')
    best_method= database.get_best_preparation_for_bean(connection,name)
    print(f"The best preparation method for {name} is: {best_method[2]}")

def prompt_remove_bean_by_name(connection):
    name=input('Enter bean name to remove: ')
    database.remove_beans_by_name(connection, name)
menu()



