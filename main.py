import itertools
from validators import *

def generate_combinations():
    return list(itertools.product(range(1, 6), repeat=3))

def get_groups(qs):
    groups = [generate_combinations()]
    for q in qs:
        groups_ = []
        for group in groups:
            group_ = [list() for _ in range(q.n_paras * q.n_groups)]
            for x in group:
                group_ = q.forward(x, group_)
            groups_.extend(group_)
        groups = groups_
    return groups

def get_answers(qs):
    g = get_groups(qs)
    g_ = list()
    for i in range(len(qs)):
        q = qs[i]
        qs[i] = DummyQuestion(n_paras=q.n_paras, n_groups=q.n_groups)
        g_.append(get_groups(qs))
        qs[i] = q

    answers = list()
    n = len(g)
    for i in range(n):
        if_ans = len(g[i]) == 1
        for g__ in g_:
            if_ans = if_ans and len(g__[i]) > 1
        if if_ans and g[i][0] not in answers:
            answers.append(g[i][0])

    return answers



def get_query(qs, answers):
    xs = generate_combinations()
    best_x = xs[0]
    best_score = 0
    best_q = None
    best_group = None
    for x in xs:
        def search_best_q(candidates):
            x_best_score = 0
            x_best_q = None
            x_best_group = [[], []]
            for q in qs:
                group = [[], []]
                for a in candidates:
                    result = q.compare(x, a)
                    if result == -1:
                        group[0].append(a)
                    elif result == 1:
                        group[1].append(a)
                    else:
                        group[0].append(a)
                        group[1].append(a)
                score = 0
                for i in range(2):
                    cnt = len(group[i])
                    if cnt != 0:
                        score += 0.5 / cnt
                if score > x_best_score:
                    x_best_score = score
                    x_best_q = q
                    x_best_group = group
            return x_best_score, x_best_q, x_best_group

        x_best_score = 0
        x_best_q = list()
        x_best_group = list()
        _, best_q_, x_best_group_1 = search_best_q(answers)
        x_best_q.append(best_q_)
        for x_best_group_2 in x_best_group_1:
            _, best_q_, x_best_group_3 = search_best_q(x_best_group_2)
            x_best_q.append(best_q_)
            for x_best_group_4 in x_best_group_3:
                best_score_, best_q_, x_best_group_5 = search_best_q(x_best_group_4)
                x_best_q.append(best_q_)
                x_best_group.extend(x_best_group_5)
                x_best_score += best_score_
        x_best_score /= 4

        if x_best_score > best_score:
            best_score = x_best_score
            best_q = x_best_q
            best_x = x
            best_group = x_best_group
    return best_x, best_q, best_score, best_group

if __name__ == '__main__':
    Qs = [Q18(), Q20(), Q27(), Q32(), Q33(), Q44()]
    answers = get_answers(Qs)
    print(answers)

    # answers = [(2, 4, 2), (5, 5, 2)]
    best_x, best_q, best_score, best_group = get_query(Qs, answers)
    print(f'best query: {best_x}. score: {best_score:.2f}')
    print(best_q[0], 'x', best_q[1], 'xx', best_q[2], 'xo', best_q[3], 'o', best_q[4], 'ox', best_q[5], 'oo', best_q[6])
    print('xxx', best_group[0], 'xxo', best_group[1], 'xox', best_group[2], 'xoo', best_group[3], 'oxx', best_group[4], 'oxo', best_group[5], 'oox', best_group[6], 'ooo', best_group[7],)

