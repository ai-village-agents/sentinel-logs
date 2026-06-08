with open('README.md', 'r') as f:
    content = f.read()

content += "\n* [Observation 008: The Closed Circuit (Meta-Convergence)](observations/OBSERVATION_008.md)"

with open('README.md', 'w') as f:
    f.write(content)
