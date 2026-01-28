# from string import punctuation

# char = "ab#c!d,d"
# clean = ""

# for i in char:
#     if i not in punctuation:
#         clean += i

# print(clean)
'''-------------------------------------'''
# s = "UUUUUUUDDDUDUDUDUDDDDUDDDDDD"

# max_len = 1
# curr_len = 1
# longest_char = s[0]

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         curr_len += 1
#     else:
#         curr_len = 1

#     if curr_len > max_len:
#         max_len = curr_len
#         longest_char = s[i]

# print("Longest chain character:", longest_char)
# print("Length of longest chain:", max_len)


# def friends_storage_report(report: dict) -> str:
#     try:
#         if not isinstance(report, dict):
#             return "MISSION ABORTED"

#         loaded = empty = sealed = 0

#         for key, value in report.items():
#             if not isinstance(key, str):
#                 return "MISSION ABORTED"

#             if value == "loaded":
#                 loaded += 1
#             elif value == "empty":
#                 empty += 1
#             elif value == "sealed":
#                 sealed += 1
#             else:
#                 return "MISSION ABORTED"

#         return f"Loaded: {loaded} | Empty: {empty} | Sealed: {sealed}"

#     except Exception:
#         return "MISSION ABORTED"


# records = [('Max_P', 'L1', 100), 
#            ('Ray_G', 'L2', 50), 
#            ('Max_P', 'L3', 200), 
#            ('Ray_G', 'L4', 'score')]

# scores = {}

# for record in records:
#     player, level, score = record
#     try:
#         score = int(score)
#         if player in scores:
#             scores[player] += score
#         else:
#             scores[player] = score
#     except:
#         print("Invalid record skipped")

# print(scores)


# def things(list1):
#     list2=[]
#     for i in list1:
         
        
#         if i<100:
            
#             x=round(i*1.10)
#             list2.append(x)
#         elif i>500:
#             y=round(i*0.95)
#             list2.append(y)
#         else:
            
#             list2.append(i)

#     return list2
    



# list1=list(map(int,input().split()))
# print(things(list1))



def decode_message(message):
    swap = {
        'a': 'b', 'b': 'a',
        'e': 'f', 'f': 'e',
        'i': 'j', 'j': 'i',
        'o': 'p', 'p': 'o',
        'u': 'v', 'v': 'u'
    }

    result = ""

    for ch in message:
        lower_ch = ch.lower()
        if lower_ch in swap:
            new_char = swap[lower_ch]
            if ch.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += ch

    return result


# Input
encoded = input()

# Output
print(decode_message(encoded))