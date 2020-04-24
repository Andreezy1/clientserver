# Приложение клиент-сервер
## Функциональные возможности приложения
В данном приложение сделаны следующие функции: 
- Вход по логину и паролю в приложение
- Вывод таблицы из базы данных
- Добавления элементов в базу данных
- Удаление элементов из базы данных

## Описание приложения
При запуске приложения появляется окно входа по логину и паролю.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/1.png

При вводе не правильного логина или пароля, пользователю сообщается об этом.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/2.png

После того как пользователь ввел верно данные, открывается следующие окно. 
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/3.png

Данное окно основное. В нем ведется работа с таблицами.
Пользователь вводит название таблицы в строку для ввода и при нажатии кнопки "Вывести/обновить" отображается нужная таблица.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/4.png

Для того чтобы внести дополнительную запись в таблицу нужно нажать на кнопку "плюсик"
и появиться строка для ввода.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/5.png

После ввода дополнительной строки жмем кнопку "Отправить данные в таблицу" и все добавленые записи отправляются в таблицу в базе данных.

Для того чтобы удалить ненужную строчку жмем кнопку "минус" и появиться сообщение для подтверждения действия.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/6.png
После подтверждения действия удаляется запись.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/7.png

Проверяем таблицу в базе данных на сервере.
![Alt-текст]https://github.com/Andreezy1/clientserver/blob/master/image/8.png

## Код программы
### Серверная часть

Серверная часть состоит из трех файлов:

- [Код для работы с базой данных](https://github.com/Andreezy1/clientserver/blob/master/server/bd.py)
- [Код для подключению к клиенту](https://github.com/Andreezy1/clientserver/blob/master/server/serverconnect.py)
- [Код сервера для работы двух файлов предыдущих](https://github.com/Andreezy1/clientserver/blob/master/server/main.py)

### Клиентская часть

Клиентская часть состоит из 4-х файлов:

- [Код окна логин-пароль](https://github.com/Andreezy1/clientserver/blob/master/client/loginpass.py)
- [Код основного окна](https://github.com/Andreezy1/clientserver/blob/master/client/mainwin.py)
- [Код для подключения к серверу](https://github.com/Andreezy1/clientserver/blob/master/client/clientconnect.py)
- [Основной код клиента для логики программы](https://github.com/Andreezy1/clientserver/blob/master/client/main.py)