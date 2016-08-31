sub = {'neutron': 0.55,
       'proton': 0.21,
       'meson': 0.03,
       'muon': 0.07,
       'neutrino': 0.14}


def least_likely_part(dictionary):
    newlist = []
    for i in dictionary:
        newlist.append(i)
    return min(newlist)


print(least_likely_part(sub))
