test:
	cd src && python -m unittest discover -v

run:
	cd src && python -c "from car import Car; c=Car('Test',50); c.refuel(20); print(f'Машина: {c.model}, Топливо: {c.current_fuel}')"
