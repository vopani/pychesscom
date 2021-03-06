# PyChessCom

An asynchronous Python client for Chess.com's API
<p>
  <img alt="License" src="https://img.shields.io/github/license/vopani/pychesscom?color=blue">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/pychesscom?color=orange">
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/pychesscom?label=pypi&color=green">
  <img src='https://readthedocs.org/projects/pychesscom/badge/?version=latest' alt='Documentation Status' />
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pychesscom?color=yellow">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/vopani">
</p>

## Index

* [Installation](#Installation)
* [Usage](#Usage)
* [Resources](#Resources)
* [License](#License)
* [Credits](#Credits)

## Installation
**Python 3.7 or higher is required**

To install stable version from PyPI (recommended):

```python
pip install pychesscom
```

To install development version:

```bash
$ git clone https://github.com/vopani/pychesscom
$ cd pychesscom
$ python3 -m pip install -r requirements.txt
```

## Usage
##### Jupyter Notebook
```python
from pychesscom import ChessComClient

client = ChessComClient()
response = await client.player.get_details('erik')
print(response)
```

##### Python Console
```python
import asyncio
from pychesscom import ChessComClient

async def main():
	client = ChessComClient()
	response = await client.player.get_details('erik')
	print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Resources
* Documentation: [https://pychesscom.readthedocs.io/](https://pychesscom.readthedocs.io/)
* Tutorial: [https://www.kaggle.com/rohanrao/introducing-pychesscom](https://www.kaggle.com/rohanrao/introducing-pychesscom)
* WGM Chess Dataset: [https://www.kaggle.com/rohanrao/wgm-chess-games-dataset-preparation](https://www.kaggle.com/rohanrao/wgm-chess-games-dataset-preparation)

## License

This project is licensed under the [Apache License 2.0](LICENSE)

## Credits
Chess.com API: [https://www.chess.com/news/view/published-data-api](https://www.chess.com/news/view/published-data-api)   
Lichess Python client: [https://github.com/amasend/lichess\_python\_SDK](https://github.com/amasend/lichess_python_SDK)
