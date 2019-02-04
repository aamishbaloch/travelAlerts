import settings
from BVGConnect.helper import BVGConnect
from alert.email import Email

if __name__ == '__main__':
    bvg_client = BVGConnect()
    get_journey = bvg_client.get_earliest_journey_by_address('berlinerstr 40, 14169', 'chausseestr 86, 10115')

    print(f'Departure: {get_journey["departure"]}')
    print(f'Departure: {get_journey["arrival"]}')
    print(f'Departure: {get_journey["route_points"]}')

    subject = 'Your train will be arriving soon!'
    message = f'You need to leave at {get_journey["departure"]} and you will arrive at {get_journey["arrival"]}.\n'
    message += f'Your route will be through {",".join(get_journey["route_points"])}.'

    email_client = Email(settings.username, settings.password, settings.smtp)
    email_client.send_email(settings.from_address, settings.to_address, subject, message)
