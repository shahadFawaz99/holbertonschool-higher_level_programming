import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        # نجهز قائمة تحتوي القواميس المطلوبة
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        # كتابة البيانات في ملف CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
