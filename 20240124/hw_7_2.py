# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, num, string1):
        for i in range(num):
            print(string1)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

