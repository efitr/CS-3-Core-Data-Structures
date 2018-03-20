
import string
''' This is all about managing the movement of information '''

#Find the least costing route through multiple carriers

#Find wide variety of solutions and compare the tradeoffs

#PHONE NUMBER STRUCTURE
    #A hierarchical structure, reason is that they reveal the geolocation of call routing systems
    #International number begins with '+' followed by country code, area code, local code, ... and more local areas
    #e.g. UK +44-222-3333-4444, JAPAN +81-22-333-4444, 
        #Normalized: +12223334444, will only work with these

#It's all about getting the number and making it be route through the best possible carrier
#Carriers may overlap on the same area, then its about choosing the cheapest one

#INPUT: plain text files -> 'Carrier Route List', 'Phone numbers' -> find least cost route
            #'Carrier Route' each carrier routes and assosiate costs are on the same file.
                #A route normalized starts with '+' number ',' separator then it's cost USD float-point number
             #When checking there can be longer matches, pricing may vary
            
            #'Phone Number' every phone starts with '+', this mean it's normalized


''' Problems '''
#Understanding the nature of the problem,
    #route_cost, pattern of number divides on different locations
        #should divide the lookup 

''' Scenario 1: One time route cost check '''
#Router list 100k, random, one phone number -> cost of calling this number

#have a list of 100k carrier route list, get the cost of calling that single phone number

#To divide each route_number
def divide_format(route_number):
    if route_number is not None:
        code_area, pricing = route_number.split(",")
    return code_area, pricing
    # if route_number:
    #     code_area, pricing = string.split(route_number, ',')
    #     return code_area, pricing
#def divide_text(router_list):


def cost_of_calling_a_number_iterative(router_list, phone_number):
    #APPROACHES
    # XX What I want to make, this must analize the pattern of each one of these value x value 

    #Use STRINGS fragments user the array[position area code:to position whatever ]
    #must analize the number order
    #country code, area code, local code

    #Is there a way to check the lenght of the number depending on what value 

    ### First implementation SIMPLE SOLUTION
    ### 
    
    #Is there a way to get the len value before the ',' of the route
        #compare this with the same lenght of the phone_number 
    
    for item in router_list:
        code_area, pricing = divide_format(item) #return code_area, pricing 
        print(pricing)
        pattern_len = len(code_area)
        print(phone_number[1:pattern_len])
        if phone_number[1:pattern_len] == code_area:
            return print(pricing)
        

    #for code_area, cost in router_list:
    #    route_code = [1:3]

    
    #router_list have first the pattern that must be recognized in the phone number


    #return #cost of calling the number

def cost_of_calling_a_number_recursive(router_list, phone_number):
    pass
# len to check the lenght of the item, and see if it would be a good idea to check for more complex analysis

def 
    #binary search tree, divide all the information 

def main():
    phone_number_path = "data/phone-numbers-3.txt"
    routing_costs_path = "data/route-costs-4.txt"
    phone_numbers = open(phone_number_path, 'r')
    routing_costs = open(routing_costs_path, 'r')
    #phone_number_route_cost = 
    num_list = phone_numbers.readlines()
    router_list = routing_costs.readlines()
    # print(num_list)
    # print(router_list)
    found_pricing = cost_of_calling_a_number_iterative(router_list, "+15124156620")
    #print(found_pricing)

if __name__ == '__main__':
    main()