# # 아래에 코드를 작성하시오.
# from conf.settings import NAME, MAIN_URL
# from utils.create_url import create_url

# result = create_url(NAME, MAIN_URL)
# print(result)

#-----------------------------------

# 아래에 코드를 작성하시오
from conf import settings
from utils import create_url

result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)