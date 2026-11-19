import random
import string

print("----------Level 1 AGE & SCORE----------")

age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

plans = ["VIP","Regular","Premium"] # lvl 2 variable
items = ["keycard", "badge", "access_token", "coin", "ticket", "flashlight"]  # lvl 3
accepted_items = ["keycard", "badge", "access_token"] # lvl 3


if age >= 18 and score >=50: # lvl 1 if statement
  print("ACCESS GRANTED! \nWelcome to Cyber Arcade.")
  print("")

  print("----------Level 2 Membership Scanner----------")

  if random.choice([True, False]): # lvl 2 if else
    membership_plan = random.choice(plans)
  else:
    membership_plan = ''.join(random.choices(string.ascii_letters, k = 6))

  print("MEMBERSHIP: ", membership_plan) # lvl 2
  if membership_plan == "VIP":
    print("VIP access granted")
    print("")

    print("----------Level 3 Inventory Check----------")
    item_variable =  random.choice(items)  # lvl 3
    print("Item: ", item_variable)
    if item_variable in accepted_items:
      print("Valid Items Provided! \nProceed to the next point")
      print("")

      print("----------Level 4 Security Flag Challenge----------") # lvl 4
      security_code = random.randint(1,20)
      print("Security Code:", security_code)

      code_bitconversion = bin(security_code)
      print("Binary Code:" , code_bitconversion)

      player_flag = security_code & 1
      admin_flag = security_code & 2

      if player_flag != 0 and admin_flag != 0:
        print("Safe: On")
        print("Admin: On")
        print("Player and Admin Access Provided")
      elif player_flag != 0 and admin_flag == 0:
        print("Safe: On")
        print("Admin: Off")
        print("Player Access Provided")
      elif player_flag == 0 and admin_flag != 0:
        print("Safe: Off")
        print("Admin: On")
        print("Admin Access Provided")
      else:
        print("Safe: Off")
        print("Admin: Off")
        print("Guest Access Provided") # lvl 4

      print("")
      print("----------Level 5 VIP Challenge Room----------")
      if age >= 18 and score >= 50:
        if membership_plan == "VIP" and item_variable == "access_token" and player_flag != 0 and admin_flag == 0:
          print("VIP Access Granted! Welcome to the Challenge Room.")
        else:
          print("VIP Access Denied.")
      else:
        print("Arcade Access Denied.")

    else: # lvl 3
      print("Invalid Items Provided \nDo not Proceed")  

  elif membership_plan == "Premium":  # lvl 2
    print("Premium access granted")
    print("")

    print("----------Level 3 Inventory Check----------")
    item_variable =  random.choice(items)  # lvl 3
    print("Item: ", item_variable)
    if item_variable in accepted_items:
      print("Valid Items Provided! \nProceed to the next point")
      print("")

      print("----------Level 4 Security Flag Challenge----------") # lvl 4
      security_code = random.randint(1,20)
      print("Security Code:", security_code)

      code_bitconversion = bin(security_code)
      print("Binary Code:" , code_bitconversion)

      player_flag = security_code & 1
      admin_flag = security_code & 2

      if player_flag != 0 and admin_flag != 0:
        print("Safe: On")
        print("Admin: On")
        print("Player and Admin Access Provided")
      elif player_flag != 0 and admin_flag == 0:
        print("Safe: On")
        print("Admin: Off")
        print("Player Access Provided")
      elif player_flag == 0 and admin_flag != 0:
        print("Safe: Off")
        print("Admin: On")
        print("Admin Access Provided")
      else:
        print("Safe: Off")
        print("Admin: Off")
        print("Guest Access Provided") # lvl 4

    else:
      print("Invalid Items Provided \nDo not Proceed")

  elif membership_plan == "Regular":  # lvl 2
    print("Regular access only") 
    print("")

    print("----------Level 3 Inventory Check----------")
    item_variable =  random.choice(items)  # lvl 3
    print("Item:", item_variable)
    if item_variable in accepted_items:
      print("Valid Items Provided! \nProceed to the next point")
      print("")

      print("----------Level 4 Security Flag Challenge----------") # lvl 4
      security_code = random.randint(1,20)
      print("Security Code:", security_code)

      code_bitconversion = bin(security_code)
      print("Binary Code:" , code_bitconversion)

      player_flag = security_code & 1
      admin_flag = security_code & 2

      if player_flag != 0 and admin_flag != 0:
        print("Safe: On")
        print("Admin: On")
        print("Player and Admin Access Provided")
      elif player_flag != 0 and admin_flag == 0:
        print("Safe: On")
        print("Admin: Off")
        print("Player Access Provided")
      elif player_flag == 0 and admin_flag != 0:
        print("Safe: Off")
        print("Admin: On")
        print("Admin Access Provided")
      else:
        print("Safe: Off")
        print("Admin: Off")
        print("Guest Access Provided") # lvl 4


    else:
      print("Invalid Items Provided \nDo not Proceed")
    
  else:  # lvl 2
    print("Invalid membership")
    print("")
  

else: # lvl 1 else statement
  print("ACCESS DENIED! \nAge restriction")  