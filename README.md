# Python API

[https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=1&perPage=20&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006]

Sayfasındaki "BMW" ve "Ford" markasına ait araç bilgilerinden, 50 şer adet çekilip MYSQL veritabanına kaydedilmesi isteniyor.
 
* Mysql üzerindeki tabloda kayıtlara ait; yıl, model, dış renk (ext. color), iç renk (int. color) ve vites türü (transmission), fiyat ve iletişim numarasının olması gerekiyor.  
* Veriler MYSQL veritabanına kaydedildikten sonra bir API ucu ile url üzerinden veriler sunulabilir olmalıdır. Veriler marka, dış renk, yıl ve vies türüne göre filtrelenebilmelidir. Filtrelemeler multiple şekilde sorgulanabilir olmalıdır.  

Veritabanı ayarlarını config.py'den yapılır  
SQLALCHEMY_DATABASE_URI değiştirin  
VirtEnv ayarları  

```sh
$ pip install -r requirements.txt
Linux => export FLASK_APP=crudapp.py  
Windows => set FLASK_APP=crudapp.py  

$ flask db init
$ flask db migrate -m "entries table"
$ flask db upgrade
$ flask run
```
