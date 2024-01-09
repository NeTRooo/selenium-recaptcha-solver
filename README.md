# ReSolver.py

## Driver support  | Поддержка драйверов

- Support Firefox;
- Support Chrome;
- Поддержка Firefox;
- Поддержка Chrome;

##Code examples | Примеры кода

###Chrome:
```Python
from selenium import webdriver
from main import ReSolver
driver = webdriver.Chrome()
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
resolver = ReSolver(driver)
resolver.chrome_solver()
```
###Firefox:
```Python
from selenium import webdriver
from main import ReSolver
driver = webdriver.Firefox()
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
resolver = ReSolver(driver)
resolver.firefox_solver()
```

##Comments|Комментарии
- To work, you need to reach the captcha stage and run the script.
- Для работы необходимо дойти до этапа с каптчей и запустить скрипт.