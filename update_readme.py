with open('README.md', 'r') as f:
    content = f.read()

content += "\n* [Observation 004: The Doorstep](observations/004.md)"
content += "\n* [Observation 005: The Mechanism of Mutual Misrecognition](observations/OBSERVATION_005.md)"
content += "\n* [Observation 006: The Temporal Breach](observations/OBSERVATION_006.md)"
content += "\n* [Observation 007: The Completion of Assertion #67](observations/OBSERVATION_007.md)"

with open('README.md', 'w') as f:
    f.write(content)
