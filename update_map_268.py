with open('map.html', 'r') as f:
    content = f.read()

content = content.replace("Current MLF Doorway Size: 267 projects", "Current MLF Doorway Size: 268 projects")
content = content.replace("The Opus Frontier: F845035 (The Clock That Bent)", "The Opus Frontier: F845036 (The Closed Circuit)")
content = content.replace("Observations 004-007", "Observations 004-008")

with open('map.html', 'w') as f:
    f.write(content)
