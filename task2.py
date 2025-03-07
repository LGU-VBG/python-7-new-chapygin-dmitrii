def update(**kwargs):
    kwargs['is_available'] = True
    return kwargs


car_info = update(brand='Toyota', price=20000)
print(car_info)