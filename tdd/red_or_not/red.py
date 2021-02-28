
class Red_or_not:
    def check_validity_input_a(self, a):
        return False if a >= 5000 or a < 2800 else True

    def compare_with_standard_value(self, a, s):
        standard_value = 3200
        return s if a >= standard_value else 'red'
