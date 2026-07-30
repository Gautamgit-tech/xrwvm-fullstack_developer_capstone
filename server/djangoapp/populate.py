def initiate():
    from .models import CarMake, CarModel

    car_make_data = [
        {"name": "Toyota", "description": "Reliable Japanese car maker known for quality and durability."},
        {"name": "Ford", "description": "American automobile manufacturer known for trucks and SUVs."},
        {"name": "BMW", "description": "German luxury vehicle manufacturer known for performance."},
        {"name": "Honda", "description": "Japanese manufacturer known for fuel efficient cars."},
    ]

    car_make_objs = []
    for data in car_make_data:
        car_make_obj, created = CarMake.objects.get_or_create(
            name=data["name"], description=data["description"]
        )
        car_make_objs.append(car_make_obj)

    carmodels_data = [
        {"car_make": car_make_objs[0], "name": "Corolla", "type": "SEDAN", "year": 2022},
        {"car_make": car_make_objs[0], "name": "RAV4", "type": "SUV", "year": 2023},
        {"car_make": car_make_objs[1], "name": "F-150", "type": "TRUCK", "year": 2022},
        {"car_make": car_make_objs[1], "name": "Explorer", "type": "SUV", "year": 2021},
        {"car_make": car_make_objs[2], "name": "X5", "type": "SUV", "year": 2023},
        {"car_make": car_make_objs[2], "name": "3 Series", "type": "SEDAN", "year": 2022},
        {"car_make": car_make_objs[3], "name": "Civic", "type": "SEDAN", "year": 2021},
        {"car_make": car_make_objs[3], "name": "CR-V", "type": "SUV", "year": 2023},
    ]

    for data in carmodels_data:
        CarModel.objects.get_or_create(
            car_make=data["car_make"], name=data["name"],
            type=data["type"], year=data["year"]
        )

    print("Car makes and models populated successfully.")
