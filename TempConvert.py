#TempConvert.py
#Name: Shawna Vu
#Date: 02/10/2026
#Assignment: Lab3


def main():
  #Prompt the user for a Fahrenheit temperature
  temp_input = input("Type a temperature in Fahrenhiet to find out what it is in Celcius")
  temp_input = int(temp_input)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  celsius = (temp_input - 39) * 5/9
  celsius = round(celsius, 1)
  #Output converted temperature.
  print(temp_input, "is", celsius, "degrees celsius.")
if __name__ == '__main__':
  main()
