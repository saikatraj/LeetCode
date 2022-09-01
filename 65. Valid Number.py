class Solution:
    def isNumber(self, s: str) -> bool:
        flag = True;
        import re
        if re.search(r'\d+[+,-]\d+',s):
            flag = False
            return False
        alpha = "abcdfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
        if any(char in alpha for char in s):
            flag = False
            return False 
        if(s == " " or s == "" or s == "." or s == "e" or s[0] == "e" or s[-1] == "e" or s.isalpha() or "-e" in s or s.count(".")>1 or s.count("e")>1 or s[-1] == "+" or s[-1] == "-"):
            flag = False
            return False
        s = s.strip()
        if(s[0] in ("+", "-")):
            s = s[1:]
            if(s == " " or s == "" or s == "." or s == "e" or s[0] == "e" or s[-1] == "e" or s.isalpha()):
                flag = False
                return False
        if(s[0] in ("+", "-")):
            flag = False
            return False
        else:
            if s.find("e") != -1:
                s = s.split("e",1)
                if(s[0].isalpha() or s[1].isalpha() or s[0] == "."):
                    flag = False
                    return False
                if "." in s[1] or "e" in s[1]:
                    flag = False
                    return False
                else:
                    if(s[1][0] in ("+", "-")):
                        s[1] = s[1][1:]
                        if(not s[1].isnumeric()):
                            flag = False
                            return False
                        try:
                            float(s[0])
                            return True
                        except ValueError:
                            flag = False
                            return False
            else:
                try:
                    float(s)
                    return True
                except ValueError:
                    flag = False
                    return False
            return flag