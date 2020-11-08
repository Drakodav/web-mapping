* To load data
```
python manage.py shell
from world import load
load.run()
```

* The following are taken
```
/login/ [name='login']
/logout/ [name='logout']
/password_change/ [name='password_change']
/password_change/done/ [name='password_change_done']
/password_reset/ [name='password_reset']
/password_reset/done/ [name='password_reset_done']
/reset/<uidb64>/<token>/ [name='password_reset_confirm']
/reset/done/ [name='password_reset_complete']
```

* login 
```
sudo ssh -i web-mapping_key.pem azureuser@40.80.148.244
```

* pushing
```
docker tag geodjangoapp:latest vmedves/web-mapping:geodjangoapp

docker push vmedves/web-mapping:geodjangoapp
```

- server -> azure
- domain -> namecheap
- docker -> vmedves/web-mapping:geodjangoapp
