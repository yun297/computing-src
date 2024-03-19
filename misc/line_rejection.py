sensors = [12, 1, 3, 13, 14, 2, 6]

sensors_sorted = sorted(sensors)

sensor_min = sensors_sorted[0] - 1
sensor_max = sensors_sorted[-1] - 1

bearing = (((sensor_max - sensor_min)) * (360/32))/2 + (sensor_min * 11.25)

if bearing < 180:
    move = bearing + 180
elif bearing >= 180:
    move = bearing - 180
    
print(f"Bearing: {bearing} | Move Angle: {move}")   
