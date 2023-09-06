import re

def set_password(us, fl=list(), ml=False, mode="instagram"):
	if not ml:
		for x in us:
			NAME = x["name"]
			unem = x["id"]
			name = NAME.lower()
			name = " ".join(re.findall("([a-z-A-Z ]+)", name) or re.findall("(.*)", name))
			unemo = ".".join(re.findall("([a-z-A-Z-_]+)", unem))
			last = name.split(" ")[-1]
			firstunem = unemo.split(".")[0].split("_")[0]
			pr = [
					name,
					unem.replace(".", "").replace("_", ""),
					name.split(" ")[0].replace(".", "").replace("_", ""),
					name.split(" ")[0].replace(".", "").replace("_", "")+"123",
					name.split(" ")[0].replace(".", "").replace("_", "")+"1234",
					name.split(" ")[0].replace(".", "").replace("_", "")+"12345",
					name.split(" ")[0].replace(".", "").replace("_", "")+"123456",
					last +"123",
					last +"1234",
					last +"12345",
					last +"123456",
					#unemo,
					#unemo.replace("_", ""),
					#firstunem +"123",
					#firstunem +"1234",
					#firstunem +"12345",
					#firstunem +"123456",
					#NAME.split(" ")[0]+"123", 
					#NAME.split(" ")[0]+"1234", 
					#NAME.split(" ")[0]+"12345", 
					#NAME.split(" ")[0]+"123456",
					#"sayang",
					#"bismillah",
					#"kontol"
					]
			if mode == "instagram":
				pr.insert(1, unem)
			temp = []
			for i in range(len(pr)):
				if len(pr[i]) < 6:
					pr[pr.index(pr[i])] = "blacklist!"; continue
				if pr[i] in temp:
					pr[pr.index(pr[i])] = "blacklist!"
				temp.append(pr[i])
			pr = [fr for fr in pr if not "blacklist!" in fr and fr.isdigit() == False]
			if pr:
				if pr[0]:
					fl.append({"u": x["id"], "p": pr})
		return fl