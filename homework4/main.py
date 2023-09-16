# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import threading
import multiprocessing
import asyncio
import argparse
import requests
import time
import aiohttp

URLS = ['https://icdn.lenta.ru/images/2023/08/19/16/20230819160623806/detail_5dc8a7ffc2667ecc48445c66439c70b0.jpg',
        'https://icdn.lenta.ru/images/2023/08/18/20/20230818202628366/owl_wide_1200_bc70de411614c258745bb0d6db710d23.jpg',
        'https://icdn.lenta.ru/images/2023/08/18/14/20230818140451624/owl_wide_1200_c718ad2de7dac054ce8a280fb83f9ab5.jpg']

# start_time = time.time()


def download_img(url: str) -> None:
    start_time = time.time()
    responce = requests.get(url)
    filename = responce.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(responce.content)
    print(
        f'Download image from {responce.url} is complete\nLoading time {time.time() - start_time:.2f}')


async def download_img_async(url: str) -> None:
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as responce:
            content = await responce.read()
            filename = url.split('/')[-1]
            with open(filename, 'wb') as file:
                file.write(content)
            print(
                f'Download image from {responce.url} is complete\nLoading time {time.time() - start_time:.2f}')


async def main(urls: str) -> None:
    start_time = time.time()
    tasks = [asyncio.ensure_future(download_img_async(url)) for url in urls]
    await asyncio.gather(*tasks)
    print(
        f'Download all images is complete.\nLoading time {time.time() - start_time:.2f}')


def threading_method(urls: str) -> None:
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_img, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(
        f'Download all images is complete.\nLoading time {time.time() - start_time:.2f}')


def processing_method(urls: str) -> None:
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_img, args=[url])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(
        f'Download all images is complete.\nLoading time {time.time() - start_time:.2f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser image')
    parser.add_argument('-u', '--urls', nargs='+', help='list URLs')
    urls = parser.parse_args().urls
    if not urls:
        urls = URLS

    print(f'Download images using threading method')
    threading_method(urls)

    print(f'Download images using multiprocessing method')
    processing_method(urls)

    print(f'Download images using async method')
    asyncio.run(main(urls))
