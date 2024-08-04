import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_cricbuzz_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    match_containers = soup.find_all('div', class_='cb-col-75 cb-col')

    matches = []
    for container in match_containers:
        match_details = container.find('div', class_='cb-col-60 cb-col cb-srs-mtchs-tm').find(
            'a').text.strip() if container.find('div', 'cb-col-60 cb-col cb-srs-mtchs-tm') else ''
        result = container.find('a', class_='cb-text-complete').text.strip() if container.find('a', 'cb-text-complete') else ''
        location = container.find('div', class_='text-gray').text.strip() if container.find('div', 'text-gray') else ''
        time = container.find('div', class_='cb-font-12 text-gray').text.strip() if container.find('div', 'cb-font-12 text-gray') else ''
        links = ', '.join(a['href'] for a in container.find_all('a', href=True))
        matches.append([match_details, result, location, time, links])

    df_matches = pd.DataFrame(matches, columns=['Match Details', 'Result', 'Location', 'Time', 'Links'])
    return df_matches

def analyze_and_save_data(df_matches, excel_filename):
    df_matches['Winning Team'] = df_matches['Result'].apply(lambda x: x.split('won')[0].strip() if 'won' in x else 'No result')
    win_counts = df_matches['Winning Team'].value_counts().reset_index()
    win_counts.columns = ['Team', 'Wins']
    location_counts = df_matches['Location'].value_counts().reset_index()
    location_counts.columns = ['Location', 'Matches']

    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df_matches.to_excel(writer, sheet_name='Raw Data', index=False)
        win_counts.to_excel(writer, sheet_name='Team Wins', index=False)
        location_counts.to_excel(writer, sheet_name='Match Locations', index=False)

    plt.figure(figsize=(10, 5))
    win_counts.set_index('Team')['Wins'].plot(kind='bar')
    plt.title('Number of Matches Won by Each Team')
    plt.xlabel('Team')
    plt.ylabel('Number of Wins')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    location_counts.set_index('Location')['Matches'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Most Common Match Locations')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

cricbuzz_url = 'https://www.cricbuzz.com/cricket-series/7476/icc-mens-t20-world-cup-2024/matches'
excel_filename = 'cricbuzz_analysis.xlsx'

df_matches = scrape_cricbuzz_data(cricbuzz_url)
analyze_and_save_data(df_matches, excel_filename)
print("Scraped data saved to cricbuzz_analysis.xlsx successfully")
