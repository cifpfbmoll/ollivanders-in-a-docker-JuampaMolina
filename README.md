# Python Ollivander's Shop Flask API

Puedes encontrar la imagen publicada en 
[DockerHub](https://hub.docker.com/repository/docker/juampamolina/ollivanders)

## Ejecutar la aplicacion
Iniciamos el contenedor de forma iterativa

```
docker run -it --publish 80:5000 juampamolina/ollivanders
```

### Salida en pantalla
```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Response /inventory
```
[
  {
    "name": "Elixir of the Mongoose",
    "sell_in": 3,
    "quality": 5
  },
  {
    "name": "Sulfuras, Hand of Ragnaros",
    "sell_in": 0,
    "quality": 80
  },
  {
    "name": "Sulfuras, Hand of Ragnaros",
    "sell_in": -1,
    "quality": 80
  },
  {
    "name": "Backstage Pass",
    "sell_in": 13,
    "quality": 22
  },
  {
    "name": "Backstage Pass",
    "sell_in": 8,
    "quality": 50
  },
  {
    "name": "Backstage Pass",
    "sell_in": 3,
    "quality": 50
  },
  {
    "name": "Conjured Mana Cake",
    "sell_in": 1,
    "quality": 2
  }
]

```