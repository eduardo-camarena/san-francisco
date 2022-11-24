import requests
import shutil
import typer

app = typer.Typer()

@app.command()
def download_images(
  base_url: str,
  last: int,
  to: str,
  first: int = 0,
  extension: str = '.jpg',
  add_extension: bool = False,
  zeroes: int = 0,
  query: str = ''
):
  query = '' if query == '' else f'?{query}'
  for i in range(first, last):
    filler = '0' * (zeroes + 1 - len(f'{i + 1}'))
    picture_number = f'{filler}{i + 1}'

    request_extension = extension if add_extension else '';
    request_url = f'{base_url}{picture_number}{request_extension}{query}'
  
    print(request_url)
    r = requests.get(request_url, stream=True)

    if r.status_code == 200:
      with open(f'{to}/{picture_number}{extension}', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


def main():
  app()