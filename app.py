from bs4 import BeautifulSoup
import requests
import mechanicalsoup

base_link = 'https://codewithmosh.com'
login_url = 'https://sso.teachable.com/secure/146684/users/sign_in?flow_school_id=146684'

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
browser.set_verbose(2)
browser.open(base_link)
browser.follow_link("sign_in")






# login_form_data = {
#     'user': {
#         'email': 'mostafa.mareyahmed@gmail.com',
#         'password': 'Aq12345678910',
#         'school_id': 146684
#     },
#     'g-recaptcha-response': '03AGdBq26kV-mMZtL5blGWl3X0SKpuGbR1AxSofD4EBynH0-cQ2OhhYv_F31jw5xdd9wwzC-Q74KizIRsnLoVI_NNH9GI0JDTUh2qMaD7-mAST0IWOFMn-PSoYoz5DGhvYgcGbTxID2MGSoj5bSOZU4ZXAOE95hk2YJQT4uajFu5TQv3ZdyG-0AMUDvdLE3276CVWgVuQJaWFuAt6mKasHQFLP0mGkhInPDFJyizlDp-DGoLYqezVRD8ZTgoRyL3px5vLmeKwfyGSzrGBr1WT4de_KC2lqyPJQLkpXPGFG4t4oAZiR4P3GPtNJoEhp-25jt0ZUB0yNlMenOHFKTOCCoQvB7yN5Cax2mZVEaBk33YS-Dovsv_pR_xDNlTX4x8xkdBG2yXQVFIIpuTwnuEdYAazNe1W1mCwe9psnFq2-7xEt95cBwgmBfteWeHzBG0HiaxQeYhmn5Hdz',
#     'authenticity_token': '6DyMJC2mGgcZsz6loqZHS64ry5Er98oKqh7TcLtODK3vPNaFQCrWP9ugI3I/iJqogb2pG72trAltrrPsvnN4rw==',
#     'utf8': '',
#     'commit': 'Log In'
# }
##login##
# with requests.session() as session:
#     response = session.post(login_url, login_form_data)
#     print(response.text)
#     with open('index.html', 'w') as f:
#         f.write(response.text)

# html_text = requests.get('https://codewithmosh.com/courses/1120640/lectures/24393589').text
# soup = BeautifulSoup(html_text, 'lxml')
# lectures = soup.find_all('li', class_='section-item incomplete')
#
# for lec in lectures:
#     lec_name = lec.find('span', class_='lecture-name').text.split('\n')[1].strip() + '.mp4'
#     lec_link = base_link + lec.find('a')['href']
#     html_text = requests.get(lec_link).text
#     soup = BeautifulSoup(html_text, 'lxml')
#     video = soup.find('a', class_='download')
#     if video is None:
#         html_text = requests.get(base_link + soup.find_all('a')[-2]['href']).text
#         soup = BeautifulSoup(html_text, 'lxml')
#         print(soup.prettify())
#         break
#     else:
#         video_link = video['href']
#         print(video_link)
#
#     r = requests.get(video_link, stream=True)
#     total_size = r.headers.get('content-length')
#     print(total_size)
#     with open(lec_name, 'wb') as f:
#         downloaded_chunks = 0
#         for chunk in r.iter_content(chunk_size=1024 * 1024):
#             if chunk:
#                 f.write(chunk)
#                 downloaded_chunks += len(chunk)
#                 print(end='\r')
#                 print(f'{int((downloaded_chunks / int(total_size)) * 100)}%', end='')
#     print(end='\r')
#     print("Downloaded")
