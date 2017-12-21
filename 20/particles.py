import re

def distance(position):
    return abs(position[0]) + abs(position[1]) + abs(position[2])

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

particles = {}

for name, line in enumerate(content):
    x = re.match( r'p=<(.*?)>, v=<(.*?)>, a=<(.*?)>$', line)
    position = [int(i) for i in x.group(1).split(',')]
    velocity = [int(i) for i in x.group(2).split(',')]
    accel = [int(i) for i in x.group(3).split(',')]
    particles[name] = {
      'position': position,
      'velocity': velocity,
      'acceleration': accel,
      'distance': distance(position),
    }

for j in range(10000):
    positions = {}
    for k, v in particles.items():
        v['velocity'][0] += v['acceleration'][0]
        v['velocity'][1] += v['acceleration'][1]
        v['velocity'][2] += v['acceleration'][2]
        v['position'][0] += v['velocity'][0]
        v['position'][1] += v['velocity'][1]
        v['position'][2] += v['velocity'][2]
        v['distance'] = distance(v['position'])
        positions.setdefault(str(v['position']), []).append(k)

    for k, v in positions.items():
        if len(v) > 1:
            for i in v:
                particles.pop(i)
print(len(positions))
