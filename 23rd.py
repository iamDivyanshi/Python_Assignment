
#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
num = float(input("ENTER THE TEMPERATURE: "))
fahr = 1.8 * num + 32
cels = (num - 32) * (5/9)
print("TEMPERATURE IN FAHRENHEIT AND CELSIUS ARE:", fahr, "&", cels, "respectively")