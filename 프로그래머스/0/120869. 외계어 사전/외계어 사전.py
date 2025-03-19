def solution(spell, dic):
    dic = [i for i in dic if len(i)==len(spell)]
    spell_count = [[i,spell.count(i)] for i in set(spell)]
    spell_count.sort()
    for i in dic:
        s = [[a, i.count(a)] for a in set(i)]
        s.sort()
        if spell_count == s:
            return 1
    
    return 2