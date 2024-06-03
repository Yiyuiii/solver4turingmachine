class Question:
    def __init__(self):
        self.n_paras = 1
        self.n_groups = 1

    def single_forward(self, x, groups=None):
        raise NotImplementedError

    def forward(self, x, groups=None):
        if groups is None:
            groups = [list() for _ in range(self.n_paras * self.n_groups)]
        return self.single_forward(x, groups=groups)

    def compare(self, x1, x2):
        result = 0
        g1 = self.forward(x1)
        g2 = self.forward(x2)
        for i in range(len(g1)):
            if len(g1[i]) and len(g2[i]):  # true
                if result == -1:
                    return 0
                result = 1
            elif len(g1[i]) or len(g2[i]):  # false
                if result == 1:
                    return 0
                result = -1
        return result

class DummyQuestion(Question):
    def __init__(self, n_paras, n_groups):
        super().__init__()
        self.n_paras = n_paras
        self.n_groups = n_groups

    def single_forward(self, x, groups=None):
        for i in range(self.n_paras * self.n_groups):
            groups[i].append(x)
        return groups

class Q1(Question):
    '''
    蓝=1
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        if x[0] == 1:
            groups[0].append(x)
        elif x[0] > 1:
            groups[1].append(x)
        return groups

class Q3(Question):
    '''
    黄，3
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[1] < 3:
            groups[0].append(x)
        if x[1] == 3:
            groups[1].append(x)
        if x[1] > 3:
            groups[2].append(x)
        return groups


class Q4(Question):
    '''
    黄，4
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[1] < 4:
            groups[0].append(x)
        if x[1] == 4:
            groups[1].append(x)
        if x[1] > 4:
            groups[2].append(x)
        return groups

class Q6(Question):
    '''
    黄奇偶
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        if x[1] % 2 == 0:
            groups[0].append(x)
        else:
            groups[1].append(x)
        return groups

class Q8(Question):
    '''
    密码中1的个数
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        cnt = 0
        for i in range(3):
            if x[i] == 1:
                cnt += 1
        groups[cnt].append(x)
        return groups

class Q9(Question):
    '''
    密码中3的个数
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        cnt = 0
        for i in range(3):
            if x[i] == 3:
                cnt += 1
        groups[cnt].append(x)
        return groups

class Q10(Question):
    '''
    密码中4的个数
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        cnt = 0
        for i in range(3):
            if x[i] == 4:
                cnt += 1
        groups[cnt].append(x)
        return groups

class Q12(Question):
    '''
    蓝和紫相比
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] < x[2]:
            groups[0].append(x)
        elif x[0] == x[2]:
            groups[1].append(x)
        elif x[0] > x[2]:
            groups[2].append(x)
        return groups

class Q13(Question):
    '''
    黄和紫相比
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[1] < x[2]:
            groups[0].append(x)
        elif x[1] == x[2]:
            groups[1].append(x)
        elif x[1] > x[2]:
            groups[2].append(x)
        return groups


class Q14(Question):
    '''
    颜色最小
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] < x[1] and x[0] < x[2]:
            groups[0].append(x)
        elif x[1] < x[0] and x[1] < x[2]:
            groups[1].append(x)
        elif x[2] < x[0] and x[2] < x[1]:
            groups[2].append(x)
        return groups

class Q15(Question):
    '''
    颜色最大
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] > x[1] and x[0] > x[2]:
            groups[0].append(x)
        elif x[1] > x[0] and x[1] > x[2]:
            groups[1].append(x)
        elif x[2] > x[0] and x[2] > x[1]:
            groups[2].append(x)
        return groups


class Q16(Question):
    '''
    偶数和奇数的数量相比
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        even = 0
        for i in range(3):
            if x[i] % 2 == 0:
                even += 1
            else:
                even -= 1
        if even > 0 :
            groups[0].append(x)
        else:
            groups[1].append(x)
        return groups

class Q17(Question):
    '''
    偶数个数
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        cnt = 0
        for i in range(3):
            if x[i] % 2 == 0:
                cnt += 1
        groups[cnt].append(x)
        return groups

class Q18(Question):
    '''
    总和奇偶
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        sum = x[0] + x[1] + x[2]
        if sum % 2 == 0:
            groups[0].append(x)
        else:
            groups[1].append(x)
        return groups

class Q19(Question):
    '''
    蓝黄总和，6
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        sum = x[0] + x[1]
        if sum < 6:
            groups[0].append(x)
        elif sum == 6:
            groups[1].append(x)
        elif sum > 6:
            groups[2].append(x)
        return groups

class Q20(Question):
    '''
    数字出现2次
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] == x[1] == x[2]:
            groups[0].append(x)
        elif x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
            groups[1].append(x)
        else:
            groups[2].append(x)
        return groups

class Q21(Question):
    '''
    数字正好出现2次
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        if x[0] == x[1] == x[2]:
            groups[0].append(x)
        elif x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
            groups[1].append(x)
        else:
            groups[0].append(x)
        return groups

class Q22(Question):
    '''
    密码中的3个数字是升序、降序还是无序
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] < x[1] and x[1] < x[2]:
            groups[0].append(x)
        elif x[0] > x[1] and x[1] > x[2]:
            groups[1].append(x)
        else:
            groups[2].append(x)
        return groups


class Q23(Question):
    '''
    所有数字的和与6相比
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        sum = x[0] + x[1] + x[2]
        if sum<6:
            groups[0].append(x)
        elif sum==6:
            groups[1].append(x)
        elif sum>6:
            groups[2].append(x)
        return groups

class Q24(Question):
    '''
    是否有一个升序且连续的序列
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[2] == x[1] + 1 and x[1] == x[0] + 1:
            groups[0].append(x)
        elif x[2] == x[1] + 1 or x[1] == x[0] + 1:
            groups[1].append(x)
        else:
            groups[2].append(x)
        return groups

class Q25(Question):
    '''
    是否有一个升序或降序且连续的序列
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if (x[0] == x[1] + 1 and x[1] == x[2] + 1) or (x[0] == x[1] - 1 and x[1] == x[2] - 1):
            groups[0].append(x)
        elif x[0] == x[1] + 1 or x[1] == x[2] + 1 or x[0] == x[1] - 1 or x[1] == x[2] - 1:
            groups[1].append(x)
        else:
            groups[2].append(x)
        return groups

class Q26(Question):
    '''
    一个特定颜色的数字小于3
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] < 3:
            groups[0].append(x)
        if x[1] < 3:
            groups[1].append(x)
        if x[2] < 3:
            groups[2].append(x)
        return groups

class Q27(Question):
    '''
    一个特定颜色的数字小于4
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] < 4:
            groups[0].append(x)
        if x[1] < 4:
            groups[1].append(x)
        if x[2] < 4:
            groups[2].append(x)
        return groups

class Q28(Question):
    '''
    一个特定颜色的数字=1
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0]==1:
            groups[0].append(x)
        if x[1]==1:
            groups[1].append(x)
        if x[2]==1:
            groups[2].append(x)
        return groups

class Q29(Question):
    '''
    一个特定颜色的数字=3
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0]==3:
            groups[0].append(x)
        if x[1]==3:
            groups[1].append(x)
        if x[2]==3:
            groups[2].append(x)
        return groups

class Q30(Question):
    '''
    一个特定颜色的数字=4
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0]==4:
            groups[0].append(x)
        if x[1]==4:
            groups[1].append(x)
        if x[2]==4:
            groups[2].append(x)
        return groups

class Q32(Question):
    '''
    一个特定颜色的数字>3
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0]>3:
            groups[0].append(x)
        if x[1]>3:
            groups[1].append(x)
        if x[2]>3:
            groups[2].append(x)
        return groups

class Q33(Question):
    '''
    特定颜色是偶数还是奇数
    '''

    def __init__(self):
        super().__init__()
        self.n_paras = 3
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[para] % 2 == 0:
                groups[para * self.n_groups + 0].append(x)
            else:
                groups[para * self.n_groups + 1].append(x)
        return groups

class Q35(Question):
    '''
    哪个颜色有最大的数字(或者并列为最大的数字)
    '''

    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if x[0] >= x[1] and x[0] >= x[2]:
            groups[0].append(x)
        if x[1] >= x[0] and x[1] >= x[2]:
            groups[1].append(x)
        if x[2] >= x[0] and x[2] >= x[1]:
            groups[2].append(x)
        return groups

class Q36(Question):
    '''
    所有数字的和是3或4或5的倍数
    '''

    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        sum = x[0] + x[1] + x[2]
        if sum % 3 == 0:
            groups[0].append(x)
        if sum % 4 == 0:
            groups[1].append(x)
        if sum % 5 == 0:
            groups[2].append(x)
        return groups

class Q39(Question):
    '''
    一个特定颜色的数字与1相比
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 3
        self.n_groups = 2

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[para] == 1:
                groups[para * self.n_groups + 0].append(x)
            elif x[para] > 1:
                groups[para * self.n_groups + 1].append(x)
        return groups



class Q40(Question):
    '''
    一个特定颜色的数字与3相比
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 3
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[para] < 3:
                groups[para * self.n_groups + 0].append(x)
            elif x[para] == 3:
                groups[para * self.n_groups + 1].append(x)
            elif x[para] > 3:
                groups[para * self.n_groups + 2].append(x)
        return groups


class Q42(Question):
    '''
    哪个颜色是最小的或最大的
    '''
    def __init__(self):
        super().__init__()
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        if (x[0] < x[1] and x[0] < x[2]) or (x[0] > x[1] and x[0] > x[2]):
            groups[0].append(x)
        elif (x[1] < x[0] and x[1] < x[2]) or (x[1] > x[0] and x[1] > x[2]):
            groups[1].append(x)
        elif (x[2] < x[0] and x[2] < x[1]) or (x[2] > x[0] and x[2] > x[1]):
            groups[2].append(x)
        return groups

class Q43(Question):
    '''
    蓝与特定颜色的数字相比
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 2
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[0] < x[para + 1]:
                groups[para * self.n_groups + 0].append(x)
            elif x[0] == x[para + 1]:
                groups[para * self.n_groups + 1].append(x)
            elif x[0] > x[para + 1]:
                groups[para * self.n_groups + 2].append(x)
        return groups

class Q44(Question):
    '''
    黄与特定颜色的数字相比
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 2
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[1] < x[2 * para]:
                groups[para * self.n_groups + 0].append(x)
            elif x[1] == x[2 * para]:
                groups[para * self.n_groups + 1].append(x)
            elif x[1] > x[2 * para]:
                groups[para * self.n_groups + 2].append(x)
        return groups

class Q45(Question):
    '''
    密码中有多少个1或者3
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 2
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            cnt = 0
            for i in range(3):
                if x[i] == (para+1)*2-1:
                    cnt+=1
            groups[para * self.n_groups + cnt].append(x)
        return groups

class Q46(Question):
    '''
    密码中有多少个3或者4
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 2
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            cnt = 0
            for i in range(3):
                if x[i] == para+3:
                    cnt+=1
            groups[para * self.n_groups + cnt].append(x)
        return groups

class Q47(Question):
    '''
    密码中有多少个1或者4
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 2
        self.n_groups = 4

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            cnt = 0
            for i in range(3):
                if x[i] == 1 + 3 * para:
                    cnt+=1
            groups[para * self.n_groups + cnt].append(x)
        return groups


class Q48(Question):
    '''
    比较两颜色大小
    '''
    def __init__(self):
        super().__init__()
        self.n_paras = 3
        self.n_groups = 3

    def single_forward(self, x, groups=None):
        for para in range(self.n_paras):
            if x[para] < x[(para + 1) % 3]:
                groups[para * self.n_groups + 0].append(x)
            elif x[para] == x[(para + 1) % 3]:
                groups[para * self.n_groups + 1].append(x)
            elif x[para] > x[(para + 1) % 3]:
                groups[para * self.n_groups + 2].append(x)
        return groups
