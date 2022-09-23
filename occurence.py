def strStr(haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1