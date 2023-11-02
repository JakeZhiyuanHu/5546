f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}

f_suburbs = {suburb for suburb in f_suburbs if suburb.startswith('F')}

required_suburbs = {"Fairfield", "Fairfield East", "Fairfield Heights", "Fairfield West", "Fairlight", "Fiddletown", "Five Dock", "Flemington", "Forest Glen", "Forest Lodge", "Forestville", "Freemans Reach", "Frenchs Forest", "Freshwater"}
f_suburbs.update(required_suburbs )

print(f_suburbs)