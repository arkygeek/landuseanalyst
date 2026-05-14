import os
base = "/home/arkygeek/.landuseAnalyst/"
for d in ['animalProfiles', 'cropProfiles', 'animalParameterProfiles', 'cropParameterProfiles']:
    path = os.path.join(base, d)
    if os.path.exists(path):
        print(f"\n{d}:")
        print(os.listdir(path))
    else:
        print(f"\n{d} DOES NOT EXIST")
