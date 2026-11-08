print("========== WELCOME TO LEVEL UP 2050 ==========")
#this is used for progress saving
import json
import os

#locates the file where this Python code is located
folder = os.path.dirname(os.path.abspath(__file__))
#creates a JSON file under the name of "fitnessdata.json"
filename = os.path.join(folder, "fitnessdata.json")

#This if-else condition is used to determine if progress exists or not
if os.path.exists(filename):
    with open(filename, "r") as file:
        #this loads progress from the JSON file and the "data" variable acts as a dictionary
        data = json.load(file)
#if progress doesnt exist, else statement executes and creates an empty data dictionary
else:
    data = {}

#input for name (Very Important)
name = input("\nYour name: ")

#If the value of name is the same as the one in the JSON file, it retrieves the data from the JSON file an assigns it to the following variables 
if name in data:
    height = data[name]["height"]
    weight_loss_goal = data[name]["weight_loss_goal"]
    calorie_goal= data[name]["calorie_goal"]
    calorie_lost = data[name]["calorie_lost"]
    level = data[name]["level"]
    total_weight_lost = data[name]["total_weight_lost"]
    weight = data[name]["weight"]
    bmi = data[name]["bmi"]
    status = data[name]["status"]
    rebirth = data[name]["rebirth"]
    rebirth_times = data[name]["rebirth_times"]
    print(f"\nWelcome back {name}!")
    if rebirth == True:
      print("Congratulations on you REBIRTH")
    print("Here are your current records:")
    print("==============================================")
    print(f"Height:            |{height:.2f}cm ")
    print(f"Weight:            |{weight:.2f}kg")
    print(f"BMI:               |{bmi:.2f}({status})")
    print(f"Weight Loss Goal:  |{weight_loss_goal:.2f}kg")
    print(f"Level:             |{level}")
    print(f"Total Weight Lost: |{total_weight_lost:.2f}kg")
    print(f"Times Rebirthed:   |{rebirth_times}")

#If the value of name is different or if there are no existing progress, input is required (For the scenario where a different name is entered, it creates an entirely new progress for that name even though there is previous progress) 
else:
    print(f"\nWelcome, {name}")
    while True:
      try:
        height = float(input("Height (cm): "))
        weight_loss_goal = float(input("Weight Loss Goal (kg): "))
      except (ValueError,ZeroDivisionError):
        print("Please Enter a Numerical, Non-Zero Value!")
        continue
      break

    calorie_goal=weight_loss_goal*7700
    calorie_lost=0
    level = int(0)
    total_weight_lost = 0
    rebirth = False
    rebirth_times = 0
    
    #saves the inputs in data
    data[name] = {
        "height": height,
        "weight_loss_goal": weight_loss_goal,
        "calorie_goal": calorie_goal,
        "calorie_lost": calorie_lost,
        "level": level,
        "total_weight_lost": total_weight_lost,
        "rebirth": rebirth,
        "rebirth_times": rebirth_times}
    
#used for rebirth mechanic    
if rebirth == True:
  while True:
    try:
      weight_loss_goal = float(input("New Weight Loss Goal (kg): "))
      calorie_goal = weight_loss_goal*7700
      data[name]["weight_loss_goal"] = weight_loss_goal
      data[name]["calorie_goal"] = calorie_goal
    except (ValueError,ZeroDivisionError):
      print("Please Enter a Numerical, Non-Zero Value!")
      continue
    break
  #sets rebirth to false because new weight loss goal has been inputted
  rebirth = False
  

#weight has to be entered every execution to account for weight gain in between workout sessions
while True:
  try:
    weight = float(input("Weight (kg): "))
  except (ValueError,ZeroDivisionError):
    print("Please Enter a Numerical, Non-Zero Value!")
    continue
  break

bmi=weight/(height/100)**2
if bmi>=40:
  status="obese"
elif bmi>=25:
  status="overweight"
elif bmi>=18.5:
  status="normal"
else:
  status="underweight"

#saves the value of weight,bmi and status in data
data[name]["weight"]=weight
data[name]["bmi"]=bmi
data[name]["status"]=status

planet=input("\nwhat planet are you in (E/M): ").upper()
while planet not in ["E","M"]:
  print("Please enter a valid planet!")
  planet=input("\nwhat planet are you in (E/M): ").upper()

answer="Y"

total_push_ups = 0
total_runs = 0
while answer != "N":
  while True:

    workout=input("\nWhat workout you want (P/R): ").upper()

    if workout=="P":
      print("Workout chosen: Push Ups")
      total_push_ups += 1
      while True:
        difficulty=input("\nlevel (E/N/H): ").upper()
        if difficulty=="E":
          push_up=10
        elif difficulty=="N":
          push_up=20
        elif difficulty=="H":
          push_up=40
        else:
          print("Please enter a valid difficulty!")
          continue
        break

      print(f"Push up: {push_up}")
      if planet=="E":
        calorie_loss=push_up*0.5
      elif planet=="M":
        calorie_loss=push_up*0.19

      calorie_lost += calorie_loss
    elif workout=="R":
      print("Workout chosen: Running")
      total_runs += 1
      while True:
        difficulty=input("\nlevel (E/N/H): ").upper()
        if difficulty=="E":
          run=5
        elif difficulty=="N":
          run=10
        elif difficulty=="H":
          run=21
        else:
          print("Please enter a valid difficulty!")
          continue
        break

      print(f"Running(km): {run}")
      if planet=="E":
        calorie_loss=run*weight
      elif planet=="M":
        calorie_loss=run*weight*1.15

      calorie_lost += calorie_loss  

    else:
      print("Invalid Choice! Please enter a valid choice")
      continue
    break

  

  if calorie_lost >= calorie_goal:
    print("you have reach your goal!")
    #rebirth mechanic
    print("Ready for REBIRTH!")
    rebirth = True
    rebirth_times += 1
    data[name]["rebirth_times"] = rebirth_times
    answer="N"
  elif calorie_lost < calorie_goal:
    print("you have not reach your goal!")
    answer=input("\nDo you want to continue? (Y/N):").upper()
    while answer not in ["Y","N"]:
      print("Please enter Y or N ONLY!")
      answer=input("\nDo you want to continue? (Y/N):").upper()

weight_loss=calorie_lost/7700
total_weight_lost += weight_loss
current_weight=weight-weight_loss
level = int(calorie_lost/calorie_goal*100)

print("\n================ FINAL RESULT ================")
print(f"Total Push Up Set(s): |{total_push_ups}")
print(f"Total Running Set(s): |{total_runs}")
print(f"Today's Weight loss:  |{weight_loss:.2f}")
print(f"Current weight:       |{current_weight:.2f}")
print(f"LEVEL:                |{level}")

#rebirth mechanic
if rebirth == True:
  print("YOU HAVE REBIRTHED")
  level = 0
  weight_loss_goal = 0
  calorie_lost = 0
  calorie_goal = 0
  total_weight_lost = 0
  data[name]["weight_loss_goal"] = weight_loss_goal
  data[name]["calorie_goal"] = calorie_goal
#saves calorie lost and level for next execution
data[name]["calorie_lost"] = calorie_lost
data[name]["level"] = level
data[name]["total_weight_lost"] = total_weight_lost
data[name]["rebirth"] = rebirth

#overwrites the current JSON file with the current execution's data
with open(filename, "w") as file:
    json.dump(data, file, indent=4)