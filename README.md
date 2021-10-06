# Автотесты для тестирования веб приложения.
## Чек-лист тестирование веб приложения [ Рунический Воск ](https://github.com/ShulgaAnatoly/Runicheskiy_Vosk_Django)

| ID	| Описание проверки	| Статус	| Комментарии |
| --- | :------------------------------------------------ | ------------ | --------------- |
| | `Страница расклада` |
| 1	| Страница расклада РВ открывается, url соответствует ожидаемому | Passed |
| 2	| На странице расклада присутствует 7 полей выбора Рун | Passed |
| 3	| Каждое поле из семи  содержит 24 варианта выбора Рун | Passed |
| 4	| Отсутствует поле с предупреждением об уникальности выбора значения Рун | Passed |
| 5	| Кнопка 'отправить' присутствует | Passed |
| 6	| Если в одном из полей не сделан выбор Руны, при нажатии кнопки  'отправить' появляется окно с предупреждением | Not run | Not create |
| 7	| При неуникальных выбранных значениях Рун после нажатия кнопки 'отправить' появляется предужпреждение  | Passed |
| 8	| При уникальном выборе Рун во всех семи полях и нажатии кнопки 'отправить' происходит перенаправление на страницу с результатом расклада | Not run | Not create |
| | `Страница результата расклада`
| 9	| Страница результата расклада РВ открывается | Not run | Not create |
| 10	| На странице результата присутствует 7 полей с выбором Рун | Not run | Not create |
| 11	| На странице результата поля выбора Рун заполнены значениями | Not run | Not create |
| 12	| Заполненные значения в полях на странице результата расклада соответствуют выбранным значениям на странице расклада | Not run | Not create |
| 13	| Присутствует кнопка 'вернуться' | Not run | Not create |
| 14	| Присутствует кнопка 'отправить' | Not run | Not create |
| 15	| На странице результата расклада присутствуют описания сочетаний Рун | Not run | Not create |
| 16	| На странице результата расклада присутствует 42 поля описания сочетаний Рун | Not run | Not create |

Чек-лист [файл-таблица](https://docs.google.com/spreadsheets/d/1m6oP6VYK0GKUC-gxtU0M7WirFdPzayiiBnQJhSJzLlI/edit?usp=sharing) 
