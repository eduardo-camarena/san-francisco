# San Francisco
This is a command line image downloader created in python with poetry


## Usage
This package was created using poetry so the best way to use it is to install the package by running `poetry install`.
The application needs 3 params a base url the amount of images you wanto to download (it only works if the images are numbered), the directory you want to save it to.
This is a hacky wayt to do this but you can add this command to your `.zshrc` file to use the script anywhere in your os.
```zsh
download_images(){
        export CURRENT_DIR=$(pwd);
        cd ~/Documents/git_repositories/san-francisco;
        poetry run download $@;
        cd $CURRENT_DIR;
        unset CURRENT_DIR;
}
```
for more info run `poetry run download --help`

### Listen to San Francisco by I hate sex