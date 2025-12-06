#Random number game:
"""
import random
num_rand= round( random.random(), ndigits=1) *10
#num_rand = random.randint(1, 10)

user_inp= int(input("Enter Your num: "))

if num_rand==user_inp:
    print(f" {num_rand} is right guess")
else:
    while num_rand!=user_inp:
        user_inp= int(input("new guess: "))
    print(f"{user_inp}, nice guess")
"""


#todo list
"""
tasks=[]

def add_task():
    title = input("Task name: ")
    if not title.strip():
        print("Empty task ignored.")
        return
    tasks.append(title)
    print(f"Added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")




def show_menu():
    print("\n--- TODO MENU ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
           add_task()
        
        elif choice == "2":
            list_tasks()
            
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
"""


#CSV data analyzer
"""
import csv

def load_csv(path):
    with open(path, newline="") as f:
        reader=csv.DictReader(f)
        rows = list(reader)
    return rows

def main():
    rows = load_csv("data.csv")
    print(f"Loaded {len(rows)} rows")
    print("First row:", rows[0])


if __name__ == "__main__":
    main()
"""



import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    try:
        response= requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except:
        print(f"Error fetching page: {e}")
        return None
    
def parse_title(html):
    soup=BeautifulSoup(html, "html.parser")
    title_tag= soup.find("title")
    if title_tag is None:
        return None
    
    return title_tag.get_text(strip=True)

def extract_links(html):
    soup= BeautifulSoup(html,"html.parser")
    links=[]

    for a in soup.find_all("a"):
        href=a.get("href")
        text=a.get_text(strip=True)

        if href:
            links.append({"text":text, "href":href})

    return links

def extract_headings(html):
    soup=BeautifulSoup(html, "html.parser")
    headings=[]

    for level in ["h1","h2","h3"]:
        for tag in soup.find_all(level):
            text=tag.get_text(strip=True)
            headings.append({"level":level, "text":text})

    return headings


    
def summarize_page(html):
    title = parse_title(html)
    links = extract_links(html)
    headings = extract_headings(html)

    summary = {
        "title": title,
        "num_links": len(links),
        "num_headings": len(headings),
        "links": links,
        "headings": headings,
    }
    return summary



def main():
    url = input("Enter a URL to scrape: ")
    html = fetch_page(url)

    if html is None:
        return
    print("Page downloaded successfully!")


    summary = summarize_page(html)

    print("\n=== PAGE SUMMARY ===")
    print("Title:", summary["title"])
    print("Total links:", summary["num_links"])
    print("Total headings (h1–h3):", summary["num_headings"])

    print("\nSome links:")
    for link in summary["links"][:5]:
        print(f"- {link['text'] or '[no text]'} -> {link['href']}")

    print("\nSome headings:")
    for h in summary["headings"][:5]:
        print(f"- {h['level']}: {h['text']}")




if __name__ == "__main__":
    main()


