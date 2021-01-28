### Django E-commerce

**Django ile bir e-ticaret uygulaması yapılması hedeflenmiştir.**

* Proje issuelar üzerinden gidecekir.
* Gözünüze kestirdiğiniz issueyu üstlenip yapabilirsiniz ancak üstlendiğinizi belirtin ki bir başkası da aynı işle uğraşmasın :)
* Şu özellik olsun dediğiniz şeyleri issue olarak açabilirsiniz.

**Geliştirme Ortamı**

* Linter: Black
* Virtual env : Optional

**Projeyi Kendi Bilgisayarınızda Kurmak ve Çalıştırmaya Hazır Hale Getirmek İçin:**

```
git clone https://github.com/ilteriskeskin/django-ecommerce.git
cd django-ecommerce

# Sanal ortamınızı çalıştırın.
=======
python3 -m venv env # Eğer sanal bir ortamınız yoksa
..Linux için..
source env/bin/activate
pip3 install requirements.txt
cd django_ecommerce
=======
..Windows Terminal için..
.\env\Scripts\activate
pip3 install -r requirements.txt
cd django_ecommerce
```

**Environment Variables**

* Projenin [settings.py](django_ecommerce/django_ecommerce/settings.py) dosyasındaki bazı ayarları konfigüre etmek için projenin bağımlılıklarında olan [django-environ](https://github.com/joke2k/django-environ) paketinin gerektirdiği .env dosyasını yaratmalı ve [settings.py](django_ecommerce/django_ecommerce/settings.py) dosyasındaki bazı ayarları .env dosyasında değiştirmelisiniz.
* .env dosyası [settings.py](django_ecommerce/django_ecommerce/settings.py) dosyası ile aynı dizinde olmalı.
* SECRET_KEY'i [bunun gibi sitelerden](https://djecrety.ir/) rastgele olarak üretip ilgili alana ekleyebilirsiniz. Veya dilerseniz terminal'i çalıştırıp `python manage.py shell` yazıp,
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
komutları ile rastgele key üretip, ilgili alana ekleyebilirsiniz.

* .env dosyasının şablonu:

```
DEBUG=
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

* Örnek bir .env dosyası:

```
DEBUG=True
SECRET_KEY=itdb4-_wc!=*hgl3)h@v$#jy7bxingn(n+qklsdso%9yq&c5)!

DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```
* Environment variables'ları ekledikten sonra, terminal'e aşağıdaki komutu yazarak projeyi çalıştırabilirsiniz.
```
python3 manage.py runserver
```
