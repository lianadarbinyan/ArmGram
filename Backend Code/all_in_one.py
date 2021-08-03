import ast
import re

with open("massive.txt", 'r', encoding = "UTF-8") as file:
    content = file.read()

class all_in_one():

    wrongs = []
    corrected_text=''
    output=''
    frequency=''
    _suggestions=''

    def __init__(self, text):
        self.text = text
        
    def commas(self):           
            
        without_punctuation = re.sub(r'[`,-«»՛՞։՝\.\՜]', '', self.text)
        barer = ["որ", "թե", "եթե", "որպեսզի", "որովհետև", "թեև", "թեկուզ", "թեպետ","որոնք", "մինչ", "քան",  "բայց", "ու", "թե", "սակայն", "իսկ","քանի որ"]
        for k in barer:
            if k in self.text.split():
                if "," + " " + k in self.text:
                    pass
                else: 
                    self.text = self.text.replace(" " + k, "," + " " + k)

        for i in range(len(without_punctuation.split())):
            if f"'{without_punctuation.split()[i].lower()}'" not in content:
                self.wrongs.append(self.text.split()[i])


        for i in range(1, len(self.text.split())):
            if f"'{self.text.split()[i-1]}'"[-2]=="։" and f"'{self.text.split()[i]}'"[1].islower():
                self.wrongs.append(self.text.split()[i])
        
        
    def capitalize(self):    
        if (self.text[-1] == '։'):
            self.text = self.text[:-1] 
        lines = self.text.split('։ ') #Split the sentences
        self.text = ""
        for line in lines:
            a = line[0].capitalize() # capitalize the first word of sentence
            for i in range(1, len(line)):
                a = a + line[i]
            a = a + '։ ' # add the removed period
            self.text = self.text + a
        return self.text

        
        
        

    def shaxkap(self, text):
        barer = ["որ", "թե", "եթե", "որպեսզի", "որովհետև", "թեև", "թեկուզ", "թեպետ","որոնք", "մինչ", "մինչև", "քան",  "բայց", "ու", "թե", "սակայն", "իսկ", "քանի որ"]

        text = ''.join(text.lower().split('։')).split()    
        str2 = []

        for i in text:  
            if i in barer:
                if i not in str2:
                    str2.append(i)
        results = []
        for i in range(0, len(str2)):   
            if text.count(str2[i]) > 2:
                barer2 = [k for k in barer if k != str2[i]]
                results.append(f"«{str2[i]}» բառի կրկնությունից խուսափելու համար՝ բառը փոխարինեք {barer2} բառերից մեկով:")
        return results

    def deranunner(self, text):
        deranun = ["սա", "դա", "նա", "այս", "այդ", "այն", "սույն", "նույն", "միևնույն", "մյուս", "այսպես", "այդպես", "այնպես", "այսպիսի", "այդպիսի", "այնպիսի", "նույնպիսի", "այսքան", "այդքան", "այնքան", "նույնքան", "այսչափ", "այդչափ", "այնչափ", "նույնչափ", "այստեղ", "այդտեղ", "այնտեղ"]
        text = ''.join(text.lower().split('։')).split() 
        str_ = []

        for i in text:  
            if i in deranun:
                if i not in str_:
                    str_.append(i)
        results = []
        for i in range(0, len(str_)):   
            if text.count(str_[i]) > 2:
                deranun2 = [k for k in deranun if k != str_[i]]
                results.append(f"«{str_[i]}» բառի կրկնությունից խուսափելու համար՝ բառը փոխարինեք {deranun2} բառերից մեկով:")
        return results
            
                            
                            
                            
    def synonyms(self, text):
        val = [i for i in text.split()]

        with open('synonyms.txt', 'r', encoding = "utf-8") as file:
            contents = ast.literal_eval(file.read())

        results = []
        for k in range(len(val)):
            for i in range(len(contents)):
                for j in range(len(contents[i])):
                    if contents[i][j] == val[k]:
                        cont = [str(m) for m in contents[i] if m != val[k]]
                        if len(cont)==1:
                            results.append(f'Կարող եք «{val[k]}» բառը փոխարինել «{str(cont)}» բառով:')
                        elif(len(cont)>1):
                            results.append(f'Կարող եք «{val[k]}» բառը փոխարինել {str(cont)} բառերից մեկով:')
        return results

                            
                            
    @staticmethod          
    def edits1(word):
    #       self.text  =  text
    #          for j in text.split():
    #             print(edits1(j))

        letters    = 'աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցուփքևօֆ'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]

        return set(deletes + transposes + replaces + inserts)

    def edits1_all(self, text):
        return {
            word: self.edits1(word)
            for word in text.split()
        }    
    
    def suggestions(self):
        without_punctuation = re.sub(r'[`,\(\)-«»՛՞։՝\.\՜]', '', self.text)
        mylist = ["Միգուցե նկատի ունեք՝"]
        for i in range(len(self.text.split())):
            if f"'{without_punctuation.split()[i]}'" not in content:
                for j in list(self.edits1(without_punctuation.split()[i])):
                    if f"'{j}'" in content:
                        mylist.append(f"{without_punctuation.split()[i]} -  {j}")
                    elif f"'{j}'" not in content:
                        pass
                mylist.append(f"Ցավոք '{without_punctuation.split()[i]}' բառը բառարանում առկա չէ։")
        return mylist
                            
    def all_methods(self):
        self.commas()
        self.capitalize()
        # self.edits1_all()
        suggestions = self.suggestions()
        shaxkaps = self.shaxkap(self.text)
        deranuns = self.deranunner(self.text)
        syns = self.synonyms(self.text)

        print(suggestions)
        print(shaxkaps)
        print(deranuns)
        print(syns)

        return self.text