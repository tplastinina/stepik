# capital = " London is the capital of Great Britain"
# template = "{} is the capital of {}"
# print(template.format("London", "Great Britan"))
# print(template.format("Berlin", "Germany"))
# =====================================================================
# s, a, b, i = input(), input(), input(), 0
# # заменить все а на б (в с)


# while i < 1001:
#     if a in s:
#         s = s.replace(a, b)
#         i += 1
#     else:
#         print(i)
#         break
#     if a in b:
#         print("Impossible")
#         break
# ===========================================================================
# s, t, k, a = input(), input(), 0, 0
# for a in range(len(s)+1):
#     if s.startswith(t , a) == True:
#         k += 1    
# print(k)
    
# ============================================================================
# import sys
# import re

# pattern = r"((cat).*){2,}" # регулярно если кот жадно входит минимум 2 раза

# for line in sys.stdin:     #считывание строк
#     line = line.rstrip('\n')   #удаляет все символы между строками
#     if re.search(pattern, line):  #если линия под патерн
#         print(line)
# =================================================================

# import sys
# import re

# pattern = r"\bcat\b" # регулярно если кот жадно входит минимум 2 раза

# for line in sys.stdin:     #считывание строк
#     line = line.rstrip('\n')   #удаляет все символы между строками
#     if re.search(pattern, line):  #если линия под патерн
#         print(line)
# ==================================================================
# import sys
# import re

# pattern = r'(z.{3}z)' 

# for line in sys.stdin:     #считывание строк
#     line = line.rstrip('\n')   #удаляет все символы между строками
#     if re.search(pattern, line):  #если линия под патерн
#         print(line)
# ============================================================
# import sys
# import re

# pattern = r'(\w+)\1' 

# for line in sys.stdin:     #считывание строк
#     line = line.rstrip('\n')   #удаляет все символы между строками
#     if re.search(pattern, line):  #если линия под патерн
#         print(line)
# ====================================
# import sys
# import re

# pattern = r'human' 

# for line in sys.stdin:     #считывание строк
#         print(re.sub(pattern, 'computer', line.rstrip()))
# # =====================================
# import sys
# import re

# for line in sys.stdin:     #считывание строк
#         line = re.sub(r"\ba+\b", "argh", line.rstrip(), 1, flags=re.IGNORECASE)
#         print(line)
# =======================================
# import sys
# import re

# for line in sys.stdin:
#     line = line.rstrip()
#     fixed = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
#     print(fixed)
# ===========================================
# import sys
# import re

# for line in sys.stdin:
#     line = line.rstrip()
#     fixed = re.sub(r"(\w)(\1)+", r"\1", line)
#     print(fixed)
# ========================================
import sys
import re

pattern = r"(1(01+0)+1|0)+" 

for line in sys.stdin:     #считывание строк
    line = line.rstrip('\n')   #удаляет все символы между строками
    if re.search(pattern, line):  #если линия под патерн
        print(line)
        print(line)
