def solution(id_pw, db):
    if id_pw[0] in [i[0] for i in db]:
        for p in db:
            if id_pw == p:
                return 'login'
        return "wrong pw"
    return "fail"