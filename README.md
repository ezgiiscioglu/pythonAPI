Veritabanı ayarlarını 
config.py'den yapılacak
SQLALCHEMY_DATABASE_URI degistirin
VirtEnv ayarları ......

```
```
pip install -r requirements.txt
```
```
Linux => export FLASK_APP=crudapp.py
Windows => set FLASK_APP=crudapp.py
```
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
