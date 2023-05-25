import requests
import os

def download_imgur_image(imgur_link, save_path,folder):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, save_path)
    response = requests.get(imgur_link, headers=headers)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("圖片下載成功！")
    else:
        print("圖片下載失敗。")


def test():
    # 使用范例
    imgur_link = 'https://i.imgur.com/Fdo12tA.jpg'  
    save_path = 'image.jpg' 
    folder = 'images'
    download_imgur_image(imgur_link, save_path, folder)