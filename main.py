from fastapi import FastAPI
from random import choice

app = FastAPI()

# Sample vehicle brand lists
cars = ["Toyota Camry", "Toyota Corolla", "Honda Civic", "Honda Accord", "Ford Mustang", "Ford Focus", 
        "BMW 3 Series", "BMW X5", "Mercedes C-Class", "Mercedes E-Class", "Audi A4", "Audi Q5", 
        "Volkswagen Passat", "Volkswagen Jetta", "Hyundai Elantra", "Hyundai Sonata", "Chevrolet Malibu",
        "Chevrolet Cruze", "Nissan Altima", "Nissan Maxima", "Kia Optima", "Kia Forte", "Mazda3", "Mazda6",
        "Subaru Impreza", "Subaru Legacy", "Lexus ES", "Lexus IS", "Tesla Model 3", "Tesla Model S"]
bikes = ["Harley-Davidson Street Glide", "Harley-Davidson Road King", "Honda CBR1000RR", "Honda Gold Wing", 
         "Yamaha YZF-R1", "Yamaha MT-09", "Kawasaki Ninja ZX-10R", "Kawasaki Vulcan", "Ducati Panigale V4",
         "Ducati Monster", "BMW S1000RR", "BMW R1250GS", "Triumph Street Triple", "Triumph Bonneville",
         "KTM 1290 Super Duke", "KTM 390 Duke", "Suzuki GSX-R1000", "Suzuki Hayabusa", "Indian Scout",
         "Indian Chieftain", "Aprilia RSV4", "Aprilia Tuono", "Moto Guzzi V7", "MV Agusta F4"]
hatchbacks = ["Volkswagen Golf", "Ford Fiesta", "Honda Fit", "Toyota Yaris", "Hyundai i20", "Suzuki Swift",
              "Mazda3 Hatchback", "Audi A3 Sportback", "BMW 1 Series", "Mercedes-Benz A-Class", 
              "Renault Clio", "Peugeot 208", "MINI Cooper", "Kia Rio", "Chevrolet Spark",
              "Fiat 500", "Volkswagen Polo", "Seat Leon", "Skoda Fabia", "Toyota Corolla Hatchback",
              "Nissan Micra", "Honda Civic Hatchback", "Hyundai i30", "Ford Focus Hatchback",
              "Volvo V40", "Lexus CT", "Subaru Impreza Hatchback", "Alfa Romeo Giulietta"]
suvs = ["Toyota RAV4", "Toyota Highlander", "Toyota Land Cruiser", "Honda CR-V", "Honda Pilot", "Honda HR-V",
        "Ford Explorer", "Ford Escape", "Ford Expedition", "Jeep Cherokee", "Jeep Grand Cherokee", "Jeep Wrangler",
        "Hyundai Tucson", "Hyundai Santa Fe", "Hyundai Palisade", "Nissan Rogue", "Nissan Murano", "Nissan Pathfinder",
        "BMW X3", "BMW X5", "BMW X7", "Mercedes-Benz GLC", "Mercedes-Benz GLE", "Mercedes-Benz GLS",
        "Audi Q3", "Audi Q5", "Audi Q7", "Volvo XC40", "Volvo XC60", "Volvo XC90",
        "Lexus RX", "Lexus NX", "Lexus GX", "Mazda CX-5", "Mazda CX-9", "Subaru Forester",
        "Volkswagen Tiguan", "Volkswagen Atlas", "Porsche Cayenne", "Porsche Macan", "Range Rover Evoque",
        "Range Rover Sport", "Kia Telluride", "Kia Sportage", "Chevrolet Tahoe", "Chevrolet Equinox"]
pickups = ["Ford F-150", "Ford F-250", "Ford F-350", "Ford Ranger", "Toyota Tacoma", "Toyota Tundra", 
           "Chevrolet Silverado 1500", "Chevrolet Silverado 2500HD", "Chevrolet Colorado", "RAM 1500", 
           "RAM 2500", "RAM 3500", "GMC Sierra 1500", "GMC Sierra 2500HD", "GMC Canyon", "Nissan Titan", 
           "Nissan Frontier", "Honda Ridgeline", "Jeep Gladiator", "Hyundai Santa Cruz", "Rivian R1T",
           "Tesla Cybertruck", "Mazda BT-50", "Isuzu D-Max", "Mitsubishi Triton", "Volkswagen Amarok"]

@app.get("/cars")
async def get_random_car():
    return {"random_car": choice(cars)}

@app.get("/bikes")
async def get_random_bike():
    return {"random_bike": choice(bikes)}

@app.get("/hatchbacks")
async def get_random_hatchback():
    return {"random_hatchback": choice(hatchbacks)}

@app.get("/suvs")
async def get_random_suv():
    return {"random_suv": choice(suvs)}

@app.get("/pickups")
async def get_random_pickup():
    return {"random_pickup": choice(pickups)}

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Random Vehicle API",
        "available_endpoints": ["/cars", "/bikes", "/hatchbacks", "/suvs", "/pickups"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)