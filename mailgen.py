from random import choice, choices, randint

with open("first-names.txt", "r") as f:
    first_names = f.read().splitlines()

with open("last-names.txt", "r") as f:
    last_names = f.read().splitlines()

with open("domains.txt", "r") as f:
    domains = f.read().splitlines()

class MailGen:
    def __init__(self): 
        self.first_names = first_names
        self.last_names = last_names
        self.domains = domains
    
    def generate_numbers(self):

        def gen_special_sequence():
            charOpts = ["!","@","#","$"]
            weights = [4,3,2,1]
            charSelection = choices(charOpts, weights=weights, k=choices([0,1,2,3], weights=[10,1,1,1])[0])
            return "".join(charSelection)
        
        rn = randint(0, 10)
        if(rn == 0): # if 0, use a year between 1978 and 2005
            return str(randint(1978, 2005))
        elif(rn == 1): # if 1, generate random characters !@#$ between 1 and 4
            return gen_special_sequence()
        elif(rn == 2): # if 2, generate random characters !@#$ between 1 and 4 (with a year)
            rString = str(randint(1978, 2005))
            rString.join(gen_special_sequence())
            return rString
        elif(rn == 3): # if 3, generate random numbers of random length between 1 and 4 (not only a year)
            return randint(0, 10**randint(1, 4))
        elif(rn ==4): # if 4, generate random number of random length with special characters between 1 and 4
            return str(randint(0, 10**randint(1, 4))) + gen_special_sequence()
        elif(rn == 5): # if 5, generate random numbers of random length between 1 and 4 (not only a year) (with a year)
            return str(randint(0, 10**randint(1, 4))) + gen_special_sequence() + str(randint(0, 10**randint(1, 4)))
        else: # do nothing
            return ""
        
    def generate(self):
        first_name = choice(self.first_names)
        last_name = choice(self.last_names)
        domain = choice(self.domains)
        email = first_name.lower() + last_name.lower() + str(self.generate_numbers()) + "@" + domain
        return email


    def generate_list(self, n):
        emails = []
        for i in range(n):
            emails.append(self.generate())
        return emails
    
    def generate_list_file(self, n, filename):
        with open(filename, "w") as f:
            for email in self.generate_list(n):
                f.write(email + "\n")

    def generate_list_domain_specific(self, n, domain):
        emails = []
        for i in range(n):
            emails.append(self.generate().split("@")[0] + "@" + domain)
        return emails
    
    def generate_list_file_domain_specific(self, n, domain, filename):
        with open(filename, "w") as f:
            for email in self.generate_list_domain_specific(n, domain):
                f.write(email + "\n")


if __name__ == "__main__":
    mailgen = MailGen()
