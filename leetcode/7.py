class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        list_x = list(str_x)

        if x == 0:
            return 0
        elif list_x[0] == '-':
            list_x.pop(0)
            list_x.reverse()
            r = '-'+''.join(list_x)
            # return int('-'+r)
        elif list_x[-1] == '0':
            list_x.pop()
            list_x.reverse()
            r = ''.join(list_x)
            # return int(r)
        else:
            list_x.reverse()
            r = ''.join(list_x)
            # return int(r)
        if -2147483648 > int(r) or int(r) > 2147483648:
            return 0
        else:
            return int(r)
