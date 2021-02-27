from django.test import TestCase

# Create your tests here.

msg = "#make_order Vendor code 204 Rice - 100 Meat - 50 Pomo - 90"
msg = """ #make_order vendor code"""
msg = "#make_order “Vendor code 250” Rice - 200 Meat - 350 Ponmo - 200"

refined_message = remove_word(msg, command)
SPECIAL_CHARACTERS = "[\s\-:]"
regex_1 = r"vendor_code{}*\d+".format(SPECIAL_CHARACTERS)
regex_2 = r"vendor code{}*\d+".format(SPECIAL_CHARACTERS)


re.findall(regex_1, "vendor_code:100")
re.findall(regex_2, refined_message)

reg = "regex_{}".format(number)
matches = []


def trial(msg):
    for num in range(1, 10):
        reg = "regex_{}".format(num)
        found = re.findall(reg, refined_message)
        if found:
            matches.append(found)
    print(matches)


regex = r"#\s?\w+"
msg = (
    "Vendor code 300 IPhone - 500,000 #make_order Airpods - 100,000 Mac book - 1500000"
)
