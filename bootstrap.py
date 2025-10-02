import sys
import os
import urllib.request
import zipfile
import shutil

# URLs based on parameter
URLS = {
    "mingw": [
        "https://github.com/libsdl-org/SDL/releases/download/release-2.32.10/SDL2-devel-2.32.10-mingw.zip",
        "https://github.com/libsdl-org/SDL_image/releases/download/release-2.8.8/SDL2_image-devel-2.8.8-mingw.zip",
        "https://github.com/libsdl-org/SDL_ttf/releases/download/release-2.24.0/SDL2_ttf-devel-2.24.0-mingw.zip",
    ],
    "msvc": [
        "https://github.com/libsdl-org/SDL/releases/download/release-2.32.10/SDL2-devel-2.32.10-VC.zip",
        "https://github.com/libsdl-org/SDL_image/releases/download/release-2.8.8/SDL2_image-devel-2.8.8-VC.zip",
        "https://github.com/libsdl-org/SDL_ttf/releases/download/release-2.24.0/SDL2_ttf-devel-2.24.0-VC.zip",
    ],
}

EXTRA_URL = "https://github.com/nevemlaci/SDL2_gfx/archive/refs/heads/master.zip"
OUTPUT_DIR = "external_dependencies"


def download_file(url, dest):
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, dest)
    print(f"Saved to {dest}")



def unzip_file(zip_path, extract_to):
    print(f"Unzipping {zip_path} to {extract_to}...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print("Done.")

def delete_downloaded_zip_files(directory, urls):
    downloaded_zip_names = [os.path.basename(url) for url in urls]
    for filename in downloaded_zip_names:
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            print(f"Deleting {file_path}...")
            os.remove(file_path)

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_deps.py [mingw|msvc]")
        sys.exit(1)

    toolchain = sys.argv[1].lower()
    if toolchain not in URLS:
        print("First parameter must be 'mingw' or 'msvc'")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect URLs to download
    urls = URLS[toolchain] + [EXTRA_URL]
    if toolchain == "unix":
        urls = [EXTRA_URL]
    for url in urls:
        filename = os.path.join(OUTPUT_DIR, os.path.basename(url))
        download_file(url, filename)
        unzip_file(filename, OUTPUT_DIR)
        old_path = os.path.join(OUTPUT_DIR, "SDL2_gfx-master")
        new_path = os.path.join(OUTPUT_DIR, "SDL2_GFX")
        if os.path.isdir(old_path):
            if os.path.isdir(new_path):
                shutil.rmtree(new_path)
            os.rename(old_path, new_path)
        delete_downloaded_zip_files(OUTPUT_DIR, urls)


if __name__ == "__main__":
    main()