import random
def get_weather(city):
    description = ['sunny', 'partly cloudy', 'cloudy', 'fog', 'light rain', 'heavy rain', 'thunderstorm']
    temp = random.uniform(10, 25)
    humidity = random.randint(40, 80)
    description = random.choice(description)
    return {'temp': round(temp, 1),
            'humidity': humidity,
            'description': description,}
city = input('Enter the city: ')
print(get_weather(city))