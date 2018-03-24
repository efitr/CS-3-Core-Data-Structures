

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
    prefix, price = route_number.split(",")
    if prefix[0] is '+':
        return prefix, price
    else:
        # return None
        #To check if there is an error with the data
        raise ValueError('Route prefix is not normalized: ' + prefix)
    # if route_number is not None:
    #else:
    #    prefix, pricing = route_number.split(",")
    # if route_number:
    #     prefix, pricing = string.split(route_number, ',')
    #     return prefix, pricing
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
    
    for router_item in router_list:
        prefix, pricing = divide_format(router_item) #return prefix, pricing 
        all_matching = []     
        #print(prefix, pricing)
        prefix_len = len(prefix)
        #print(phone_number[1:prefix_len])
        #array that carries an iteration of everytime it 


        if phone_number[:prefix_len] == prefix[:prefix_len]:
            return pricing
            #all_matching.append(pricing)
        #Work solving 
    #return all_matching

    #for prefix, cost in router_list:
    #    route_code = [1:3]

    
    #router_list have first the pattern that must be recognized in the phone number


    #return #cost of calling the number

#####No particular reason for recursion?, maybe in functional programming is worthit
def cost_of_calling_a_number_recursive(router_list, phone_number, index = None):
    #pass
    #the number at index 1?
    if index == None:
        index = 0
    router_item = router_list[index]
    prefix, pricing = divide_format(router_item)
    lenght_prefix = len(prefix)
    if phone_number[1:lenght_prefix] == prefix[1:lenght_prefix]:
        return pricing
    else:
        cost_of_calling_a_number_recursive(router_list, phone_number, index =+ 1)
# len to check the lenght of the item, and see if it would be a good idea to check for more complex analysis

#def 
    #binary search tree, divide all the information, in pockets of information
    #to be checked concurrently


def main():
    phone_number_path = "data/phone-numbers-3.txt"
    routing_costs_path = "data/route-costs-35000.txt"
    phone_numbers = open(phone_number_path, 'r')
    routing_costs = open(routing_costs_path, 'r')
    #phone_number_route_cost = 
    num_list = phone_numbers.readlines()
    router_list = sorted(routing_costs.readlines())
    print(router_list)
    # print(num_list)
    # print(router_list)
    found_pricing = cost_of_calling_a_number_iterative(router_list, "+14152345678")
    print(found_pricing)

if __name__ == '__main__':
    main()