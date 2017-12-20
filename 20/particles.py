import re

def distance(position):
    return abs(position[0]) + abs(position[1]) + abs(position[2])

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

particles = []

for name, line in enumerate(content):
    x = re.match( r'p=<(.*?)>, v=<(.*?)>, a=<(.*?)>$', line)
    position = [int(i) for i in x.group(1).split(',')]
    velocity = [int(i) for i in x.group(2).split(',')]
    accel = [int(i) for i in x.group(3).split(',')]
    particles.append({
      'position': position,
      'velocity': velocity,
      'acceleration': accel,
      'distance': distance(position),
      'name': name,
    })

for j in range(10000):
    for i in particles:
        i['velocity'][0] += i['acceleration'][0]
        i['velocity'][1] += i['acceleration'][1]
        i['velocity'][2] += i['acceleration'][2]
        i['position'][0] += i['velocity'][0]
        i['position'][1] += i['velocity'][1]
        i['position'][2] += i['velocity'][2]
        i['distance'] = distance(i['position'])

particles.sort(key=lambda x: x['distance'])
print(particles[0]['name'])
