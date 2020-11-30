
meals = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
# # = [
# #     {'menu' : 'Appetizers' , 'des' : ["Wings","Cookies","Spring Rolls"]},
# #     {'menu' : 'Entrees' , 'des' : ["Salmon","Steak","Meat Tornado","A Literal Garden"]},
# #     {'menu' : 'Desserts' , 'des' : ["Ice Cream","Cake","Pie"]},
# #     {'menu' : 'Drinks' , 'des' : ["Coffee","Tea","Unicorn Tears"]}
# # ]
resturant = []
def first_function_in_python():
    print("************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type \"quit\" \n **************************************")
    print(
    "Appetizers \n ----------- \n Wings \n Cookies \n Spring Rolls \n \n",
    "Entrees \n ----------- \n Salmon \n Steak \n Meat Tornado \n A Literal Garden \n \n",
    "Desserts \n ----------- \n Ice Cream \n Cake \n Pie \n \n",
    "Drinks \n ----------- \n Coffee \n Tea \n Unicorn Tears \n"
    )
    print("*********************************** \n ** What would you like to order? ** \n *********************************** \n")
  
    
    my_meal = input('> ')

    for meal in meals:
        if my_meal != 'quit' and my_meal in meals:
            resturant.append(my_meal)
            print(f'** {resturant.count(my_meal)} order of {my_meal} have been added to your meal ** \n')
        elif my_meal == 'quit':
            exit()
        else:
            print('sorry but we dont have this meal \n')
        my_meal = input('> ')
        for x in resturant:
            print(x)

def result_order():
    for x in resturant:
        print(x)



if __name__ == '__main__':
    first_function_in_python()
    result_order()
