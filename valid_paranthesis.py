def isValid(self, s: str) -> bool:
        check = []
        grind  = {")":"(" , "]":"[", "}":"{"}
        
        for g in s:
            if g in grind:
                if check and check[-1] == grind[g]:
                    check.pop()
                else:
                    return False
            else:
                check.append(g)
        return True if not check else False
        
        