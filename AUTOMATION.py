#!/usr/bin/env python
# coding: utf-8

# # JACOBS IKEDI

# This was a particular unique project, it's 3.04am in the morning and this project leaves a bittersweet aftertaste. 
# 
# The key takeaway, basically and a point of learning from my challenges is that:
# 1. I should be more careful how and where I return functions. 
# 2. I often went back to the drawing board. Developing a flowchart was my northstar during the entire process.
# 3. Constant deliberation wether to approach from bottom-up or from top-down. (settled with the later)
# 4. I challenged myself to write the entire code with only basic methods.

# ![](Ikedi_Jacobs_Flowchart.jpeg)

# ###### Main code cell

# In[101]:


''' WELCOME TO IKEDI JACOBS' STORE INVENTORY MANAGEMENT''' 
def run_inventory_ms():
    try:
        while True:
            print('\nWelcome to Ikedi Jacobs Inventory Management System')
            print("1. If you're the Store Manager")
            print("2. If you're the Morning Shift")
            print("3. If you're the Evening Shift")
            print("4. Exit")
            
            choice = int(input('Enter your choice(1-4): '))
            if choice == 1:
                manager()
                break
            elif choice == 2:
                mrn_shift()
                break
            elif choice == 3:
                evn_shift()
                break
            elif choice == 4:
                print('\nYou have successfully logged out!')
                break
            else:
                print('\nInvalid Choice. Please enter a number btw 1-4')
    except:
        print('Please enter a number')
        run_inventory_ms()


# ###### Personnel Block

# In[2]:


#MANAGER
def manager(): #The managers view of the program
    try:
        while True:
            print('\n Welcome Manager!')
            print('1. Total Sales')
            print('2. Total Salary')
            print('3. Total Profit')
            print('4. Total Tips')
            print('5. Go back to previous menu')
            
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                sales_total()
                break
            elif choice == 2:
                salary_total()
                break
            elif choice == 3:
                profit_total()
                break
            elif choice == 4:
                tips_total()
                break
            elif choice == 5:
                run_inventory_ms()
                break
            else:
                print('Invalid choice!. Please enter a choice btw 1-5')
    except:
        print('Please enter a number')
        manager()
        
        
#Morning shift       
def mrn_shift(): #the morning shift personnels view
    try:
        while True:
            print('\n Welcome Morning Shift Personnel')
            print('1. Sales for Morning Shift')
            print('2. Salary for Morning Shift')
            print('3. Profit for Morning Shift')
            print('4. Tips for Morning Shift')
            print('5. Go back to previous menu')
            
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                sales_mrn_shift()
                break
            elif choice == 2:
                salary_mrn_shift()
                break
            elif choice == 3:
                profit_mrn_shift()
                break
            elif choice == 4:
                tips_mrn_shift()
                break
            elif choice == 5:
                run_inventory_ms()
                break
            else:
                print('Invalid choice!. Please enter a choice btw 1-5')
    except:
        print('Please enter a number')
        mrn_shift()
        
#Evening shift
def evn_shift(): #the evening shift personnels view
    try:
        while True:
            print('\n Welcome Evening Shift Personnel')
            print('1. Sales for Evening Shift')
            print('2. Salary for Evening Shift')
            print('3. Profit for Evening Shift')
            print('4. Tips for Evening Shift')
            print('5. Go back to previous menu')
            
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                sales_evn_shift()
                break
            elif choice == 2:
                salary_evn_shift()
                break
            elif choice == 3:
                profit_evn_shift()
                break
            elif choice == 4:
                tips_evn_shift()
                break
            elif choice == 5:
                run_inventory_ms()
                break
            else:
                print('Invalid choice!. Please enter a choice btw 1-5')
    except:
        print('Please enter a number')
        evn_shift()


# ###### Sales Block

# In[3]:


# Global Variables declarations
'''
sp - selling price
cp - cost price
sp_items_mrn - selling price of items sold in the morning
cp_items_mrn - cost price of items sold in the morning
sp_items_evn - selling price of items sold in the evening
cp_items_evn - cost price of items sold in the evening

sold - list of all items sold
'''

sp = {'indomie': 7500, 'rice': 10000, 'bread': 1000, 'hollandia': 9500}
cp = {'indomie': 5500, 'rice': 8700, 'bread': 800, 'hollandia': 6900}

sp_items_mrn = []
cp_items_mrn = []
sp_items_evn = []
cp_items_evn = []
sp_items_tot = []
cp_items_tot = []

sold = []


# In[39]:


#Morning Sales
def sales_mrn_shift():
    try:
        while True:
            print('\nWelcome to Morning Sales')
            print('1. Enter qty of goods sold this morning')
            print('2. View Sales data for this morning')
            print('3. Add a product to inventory')
            print('4. Exit')
            
            choice = int(input('Enter your choice: '))
            if choice == 1:
                try:
                    goods = input('name of goods sold this morning: ').lower()
                    qty = int(input('what quantity of good was sold: '))
                    
                    value_of_goods = sp[goods] * qty
                    cost_of_goods = cp[goods] * qty
                    
                    sp_items_mrn.append(value_of_goods)
                    cp_items_mrn.append(cost_of_goods)
                    sold.append(goods)
                    
                    mrn_sales = sum(sp_items_mrn)
                    mrn_cost = sum(cp_items_mrn)
                    
                    print(f'The total value of goods sold this morning is {mrn_sales}')
                    print(f'The total cost of goods sold this morning is {mrn_cost}')
                    return mrn_sales
                    
                except KeyError:
                    print('This good is not in our inventory.')
                    break
            
            elif choice == 2:
                
                mrn_sales = sum(sp_items_mrn)
                mrn_cost = sum(cp_items_mrn)
                
                print(f'The goods sold this morning are {sold}')
                print(f'The total value of goods sold this morning is {mrn_sales}')
                print(f'The total cost of goods sold this morning is {mrn_cost}')
                
                return mrn_sales
                
            elif choice == 3:
                print('\nEnter a new product here!')
                name_of_new_product = input('Enter the name of the new product: ')
                selling_price_of_new_product = int(input('Enter the selling price of the new product: '))
                cost_price_of_new_product = int(input('Enter the cost price of the new product: '))
                
                updated_sp = {name_of_new_product: selling_price_of_new_product}
                updated_cp = {name_of_new_product: cost_price_of_new_product}
                
                sp.update(updated_sp)
                cp.update(updated_cp)
                print('Successfully added to inventory!')
                print(f'Here is all the items in our inventory {sp}')
                break
                
            elif choice == 4:
                print('You have logged out!')
                break
            
            else:
                print('Please enter a number btw 1-4')
        
    except:
        print('Please enter a number')
        sales_mrn_shift()
        
#evening sales
def sales_evn_shift():
    try:
        while True:
            print('\nWelcome to Evening Sales')
            print('1. Enter qty of goods sold this evening')
            print('2. View Sales data for this evening')
            print('3. Add a product to inventory')
            print('4. Exit')
            
            choice = int(input('Enter your choice'))
            if choice == 1:
                try:
                    goods = input('name of goods sold this evening: ').lower()
                    qty = int(input('what quantity of good was sold: '))
                    
                    value_of_goods = sp[goods] * qty
                    cost_of_goods = cp[goods] * qty
                    
                    sp_items_evn.append(value_of_goods)
                    cp_items_evn.append(cost_of_goods)
                    sold.append(goods)
                    
                    evn_sales = sum(sp_items_evn)
                    evn_cost = sum(cp_items_evn)
                    
                    print(f'The total value of goods sold this evening is {evn_sales}')
                    print(f'The total cost of goods sold this evening is {evn_cost}')
                    return evn_sales
                    
                except:
                    print('This good is not in our inventory.')
                    break
            
            elif choice == 2:
                
                evn_sales = sum(sp_items_evn)
                evn_cost = sum(cp_items_evn)
                
                print(f'The goods sold this evening are {sold}')
                print(f'The total value of goods sold this evening is {evn_sales}')
                print(f'The total cost of goods sold this evening is {evn_cost}')
                return evn_sales
                
            elif choice == 3:
                print('\nEnter a new product here!')
                name_of_new_product = input('Enter the name of the new product: ')
                selling_price_of_new_product = int(input('Enter the selling price of the new product: '))
                cost_price_of_new_product = int(input('Enter the cost price of the new product: '))
                
                updated_sp = {name_of_new_product: selling_price_of_new_product}
                updated_cp = {name_of_new_product: cost_price_of_new_product}
                
                sp.update(updated_sp)
                cp.update(updated_cp)
                print('Successfully added to inventory!')
                print(f'Here is all the items in our inventory {sp}')
                break
                
            elif choice == 4:
                print('You have logged out!')
                break
            
            else:
                print('Please enter a number btw 1-4')
    except:
        print('Please enter a number')
        sales_evn_shift()
        
#Manager Sales
def sales_total():
    try:
        while True:
            print('\nWelcome to Total Sales')
            print('1. View Total Sales for today ')
            print('2. Exit')
            
            choice = int(input('Enter your choice'))
            
            if choice == 1:
                print('\nClick view sales data')
                mrn_sales = sales_mrn_shift()
                print('\VClick view sales Datasets/a')
                evn_sales = sales_evn_shift()
                
                total_sales = mrn_sales + evn_sales
                
                print(f'The goods sold today are {sold}')
                print(f'The total value of goods sold today is {total_sales}')
                return total_sales
                
            elif choice == 2:
                print('You have logged out!')
                break
            
            else:
                print('Please enter a number btw 1-2')
    except:
        print('Please enter a number')
        sales_total()


# ###### Salary Block

# In[48]:


#morning shift salary
def salary_mrn_shift():
    print('\nWelcome to Morning Salary')
    try:
        hourly_rate_of_morning_worker = float(input('Please enter your Morning hourly rate in Naira: '))
        hours_worked_morning_worker = float(input('Please enter the number of hours worked this morning: '))
        
        mrn_salary = hourly_rate_of_morning_worker * hours_worked_morning_worker
        print(f'Your take home salary for today is NGN{mrn_salary}')
        return mrn_salary
    
    except:
        print('The operation was not successful')

#evening shift salary
def salary_evn_shift():
    print('\nWelcome to Evening Salary')
    try:
        hourly_rate_of_morning_worker = float(input('Please enter your Evening hourly rate in Naira: '))
        hours_worked_morning_worker = float(input('Please enter the number of hours worked this evening: '))
        
        evn_salary = hourly_rate_of_morning_worker * hours_worked_morning_worker
        print(f'Your take home salary for today is NGN{evn_salary}')
        return evn_salary
    
    except:
        print('The operation was not successful')
        
#manager's view of the total salary
def salary_total():
    try:
        print('\nWelcome to Total Salary')
        mrn_salary = salary_mrn_shift()
        evn_salary = salary_evn_shift()
        total_salary = mrn_salary + evn_salary
        print(f'\nThe total Salary for today is {total_salary}')
        return total_salary
    
    except:
        print('The operation was not successful')


# ###### Profit Block

# In[66]:


#morning profit
def profit_mrn_shift():
    mrn_profit = 0
    mrn_profit = sum(sp_items_mrn) - sum(cp_items_mrn)
    print(f'\nThe profit for this morning is: {mrn_profit}')
    return mrn_profit

#evening profit
def profit_evn_shift():
    evn_profit = 0
    evn_profit = sum(sp_items_evn) - sum(cp_items_evn)
    print(f'The profit for this evening is: {evn_profit}')
    return evn_profit

#managers view of total profit
def profit_total():
    try:
        mrn_profit = profit_mrn_shift()
        evn_profit = profit_evn_shift()

        total_profit = mrn_profit + evn_profit

        print(f'\nThe total profit for today is: {total_profit}')
        return total_profit
    except Exception as e:
        print(f'The operation was not successful. Error: {e}')


# ###### tips block

# In[71]:


#morning tips
def tips_mrn_shift():
    mrn_tips = 0 
    mrn_tips = 0.02 * sum(sp_items_mrn) #2% of morning sales
    print(f'The tips for this morning is: {mrn_tips}')
    return mrn_tips

#evening tips
def tips_evn_shift():
    evn_tips = 0 
    evn_tips = 0.02 * sum(sp_items_evn) #2% of evening sales
    print(f'The tips for this evening is: {evn_tips}')
    return evn_tips

#manager's view of total tips
def tips_total():
    try:
        mrn_tips = tips_mrn_shift()
        evn_tips = tips_evn_shift()
        total_tips = mrn_tips + evn_tips
        print(f'\nThe total tips for today is {total_tips}')
        return total_tips
    
    except Exception as e:
        print(f'The operation was not successful. Error: {e}')

