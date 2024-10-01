import requests
from bs4 import BeautifulSoup
import math
from colorama import Fore


def banner():
    display_banner = """



        /$$$$$$$                  /$$ /$$$$$$$$                     /$$                                                      
        | $$__  $$                | $$| $$_____/                    | $$                                                      
        | $$  \ $$  /$$$$$$   /$$$$$$$| $$        /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$  /$$  /$$
        | $$$$$$$/ /$$__  $$ /$$__  $$| $$$$$    |____  $$ /$$__  $$| $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$| $$ | $$ | $$
        | $$__  $$| $$$$$$$$| $$  | $$| $$__/     /$$$$$$$| $$  \ $$| $$| $$$$$$$$| $$      | $$  \__/| $$$$$$$$| $$ | $$ | $$
        | $$  \ $$| $$_____/| $$  | $$| $$       /$$__  $$| $$  | $$| $$| $$_____/| $$      | $$      | $$_____/| $$ | $$ | $$
        | $$  | $$|  $$$$$$$|  $$$$$$$| $$$$$$$$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$/$$$$/
        |__/  |__/ \_______/ \_______/|________/ \_______/ \____  $$|__/ \_______/ \_______/|__/       \_______/ \_____/\___/ 
                                                            /$$  \ $$                                                          
                                                           |  $$$$$$/                                                          
                                                            \______/                                                           
        made by KryptonSec_My
        v1.0

        """
    print(Fore.GREEN + display_banner + Fore.WHITE)

def google_search(query, num_results):
    search_results = []
    pages = math.ceil(num_results / 10)  
    for page in range(pages):
        start = page * 10
        search_url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            html_content = response.text
            results = parse_search_results(html_content)
            search_results += results
            if len(search_results) >= num_results:
                break  
        else:
            print(Fore.RED + '[!]Error fetching dork results! womp womp')
            break
    return search_results[:num_results]  


def parse_search_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    search_results = []
    for g in soup.find_all('div', class_='g'):
        link_tag = g.find('a')
        if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
            search_results.append(link)
    return search_results


def auto_google_dork():

    banner()

    dork_query = input(Fore.CYAN + "Enter your Dork query: " + Fore.WHITE)  

    num_results = int(input(Fore.CYAN + "How many results do you want?: " + Fore.WHITE))

    search_results = google_search(dork_query, num_results)
    
    if not search_results:
        print(Fore.RED + "Failed to fetch the dork results, womp womp. Exiting." + Fore.WHITE)
        return
    
    print(Fore.GREEN + f"\nDorking Results ({num_results}):" + Fore.WHITE)
    for i, result in enumerate(search_results, 1):
        print(f"{i}. {result}")

    save_to_file = input(Fore.CYAN + "\nDo you want save the dork result into text file? (yes/no): " + Fore.WHITE).strip().lower()

    if save_to_file == 'yes':
        file_name = input(Fore.CYAN + "Enter the file name (without extension dumbass xD): " + Fore.WHITE).strip()
        with open(f"{file_name}.txt", 'w') as file:
            for result in search_results:
                file.write(f"{result}\n")
        print(Fore.GREEN + f"Results saved to {file_name}.txt" + Fore.WHITE)
    else:
        print(Fore.RED + "\nNo file saved." + Fore.WHITE)


if __name__ == "__main__":
    auto_google_dork()
