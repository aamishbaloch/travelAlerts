from BVGConnect.helper import BVGConnect

if __name__ == '__main__':
    bvg_client = BVGConnect()
    get_journey = bvg_client.get_earliest_journey_by_address('berlinerstr 40, 14169', 'chausseestr 86, 10115')

    print(f'Departure: {get_journey["departure"]}')
    print(f'Departure: {get_journey["arrival"]}')
    print(f'Departure: {get_journey["route_points"]}')

    # send journey details here
