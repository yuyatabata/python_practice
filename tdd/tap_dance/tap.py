
class Check_ease_of_step:
    def check_string(self, s):
        # return 'No'  # 仮実装
        for e in s[::2]:
            if e not in ["R", "U", "D"]:
                return "No"
        for e in s[1::2]:
            if e not in ["L", "U", "D"]:
                return "No"
        return "Yes"
