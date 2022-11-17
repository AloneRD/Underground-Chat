# Underground-Chat


# Клиент чата

клиент состоит из двух скриптов, 

```
send_message
```
отправляет сообщения в чат
```
read_message
```
читает сообщения из чата и сохраняет их в файл

## Как установить

Для работы микросервиса нужен Python версии не ниже 3.6.

```bash
pip install -r requirements.txt
```

## Как запустить

Для чтения сообщений сообщений 
```bash
python read_message.py --host=chat.org --port=5000
```
--host - адрес чата

--port - порт чата

Для отправки сообщений:

```bash
python send_message.py --host=chat.org --port=5000 --token=dsfgdgsdfgsdfgsdfg
```
--host - адрес чата

--port - порт чата

--token - токен пользователя


Регистрация нового пользователя

```bash
python send_message.py --host=chat.org --port=5000 --username=Tom
```
--host - адрес чата

--port - порт чата

--username - имя нового пользователя
# Цели проекта

Код написан в учебных целях.
