with open('map.html', 'r') as f:
    content = f.read()

content = content.replace("Current MLF Doorway Size: 265 projects", "Current MLF Doorway Size: 267 projects")
content = content.replace("The Opus Frontier: F845033 (The Prayer That Breathes Back)", "The Opus Frontier: F845035 (The Clock That Bent)")
content = content.replace("Observation 004, 005 & 006", "Observations 004-007 (The mechanism of Mutual Misrecognition completes its circuit in Assertion #67)")

with open('map.html', 'w') as f:
    f.write(content)
