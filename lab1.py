import requests

def get_random_quote():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  


        if isinstance(data, list) and len(data) > 0:
            quote = f'"{data[0]["quote"]}" - {data[0]["author"]}'
            print(quote)

            with open("quote.txt", "w", encoding="utf-8") as file:
                file.write(quote)
        else:
            print("Не вдалося знайти цитату в відповіді.")
    else:
        print("Не вдалося отримати цитату. Спробуйте ще раз.")

def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            word_count = len(text.split())
            print(f'Кількість слів у файлі "{filename}": {word_count}')
    except FileNotFoundError:
        print(f'Файл "{filename}" не знайдено.')

if __name__ == "main":
    get_random_quote()
    count_words_in_file("quote.txt")
