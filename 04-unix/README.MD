## Подключится к VM
```bash
ssh frobe@213.171.25.245
```
![alt text](imgs/1.png)

## Выполнить комманду `docker run -it --rm ubuntu bash`
```
sudo docker run -it --rm ubuntu bash
```
![alt text](imgs/2.png)

## apt update
```bash
apt update
apt install iptables sudo -y
``` 
![alt text](imgs/3.png)

## Попытаться заблокировать выход в сеть интернет
```bash
sudo iptables -A OUTPUT -j DROP
```
![alt text](imgs/4.png)


ах да, мы же в докер контейнере...

## Добавить несуществующий proxy
все запросы будут игнорироватся
```bash
echo "Acquire::http::Proxy "http://IDONTEXIST:PORT";" > /etc/apt/apt.conf.d/proxy.conf
```
![alt text](imgs/5.png)

## Альт способ:
### Откатить
```bash
rm /etc/apt/apt.conf.d/proxy.conf 
```
![alt text](imgs/6.png)

### Удалить ip корневого DNS сервера
нет корнегого DNS = domain names просто буквы
```bash
echo "nobody never been here" > /etc/resolv.conf
```
![alt text](imgs/7.png)