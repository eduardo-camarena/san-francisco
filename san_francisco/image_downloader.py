import os
import requests
import shutil
import typer
from progress.bar import Bar
from dotenv import load_dotenv

app = typer.Typer()

@app.command()
def download_images(
  base_url: str,
  save_to: str,
  last: int,
  first: int = 0,
  extension: str = '.jpg',
  add_extension: bool = False,
  zeroes: int = 0,
  query: str = '',
  name: str = '',
  add: int = 0
):
  save_path = f"{os.environ.get('BASE_PATH')}/{save_to}" if os.environ.get('BASE_PATH') else f'/{save_to}'
  query = '' if query == '' else f'?{query}'
  with Bar('Downloading', max=last - first) as bar:
    for i in range(first, last):
      filler = '0' * (zeroes + 1 - len(f'{i + 1}'))
      picture_number = f'{filler}{i + 1}'

      request_extension = extension if add_extension else '';
      request_url = f'{base_url}{picture_number}{request_extension}{query}'

      r = requests.get(request_url, stream=True)

      picture_name = f'{name} ({i - first + add + 1})' if name else f'{i - first + add + 1}'
      if r.status_code == 200:
        with open(f'{save_path}/{picture_name}{extension}', 'wb') as f:
          r.raw.decode_content = True
          shutil.copyfileobj(r.raw, f)

      bar.next()


def main():
  load_dotenv()
  app()