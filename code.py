app_notification = '''Привет, это Stepik VideoGames, портал видео про видеоигры.
Введите 1, чтобы посмотреть видео, 2 чтобы найти видео, 3 чтобы посмотреть плейлисты, exit или 0, чтобы выйти.
'''

VIDEO_REQUEST = '1'
FIND_VIDEO_REQUEST = '2'
PLAYLIST_REQUEST = '3'
NOT_FOUND_INFO = 'Ничего не найдено\n'
EXIT_REQUEST = 'exit 0'


# videos ------------------

videos = [
'ИгроСториз: Mafia 4, GTA 6 и BioShock Online – Take-Two дает бой конкурентам на PS5 и Xbox Series X https://youtu.be/05GPNjBtF48',
'Поиграли в Sekiro: Shadows Die Twice. Свежо, но знакомо https://youtu.be/nwPs5f4WLN8',
'Gothic Remake - Актуально ли в 2021 году ? [Мнение после Демки] https://youtu.be/eVtx5Y6lFjk',
'Начало прохождения - Anno 1800 #01 https://youtu.be/J3Wk2CecrUg']


def handle_videos(videos, command, not_found_info = NOT_FOUND_INFO):
    if command == VIDEO_REQUEST:
        print('У нас нашлось {0} видео\n'.format(len(videos)))

        for video in videos:
            print(video)

        print('\n')
    elif command == FIND_VIDEO_REQUEST:
        print('Введите слово для поиска:\n')
        user_request = input()
        result = ''

        for video_str in videos:
            # без обработки вводимых знаков препинания, но без поиска по ссылке

            sub_words = video_str.split('https://youtu.be/')[0].split()

            for sub_word in sub_words:
                if user_request.lower() == sub_word.lower():
                    result += video_str + '\n'

        result_len = len(result.split('\n')) - 1
        print('''У нас нашлось {0} видео по запросу {1}:\n{2}'''.format(result_len, user_request, result)
              if result_len else not_found_info)


# playlists ------------------

playlists = ['ИгроСториз', 'Репортажи', 'Обзоры']

def handle_playlists(playlists):
    print('У нас нашлось {0} плейлиста\n'.format(len(playlists)))
    result = ''

    for playlist in playlists:
        result += playlist + '\n'

    if len(result):
        print(result + '\n')

# main part ------------------

def start_app():
    print(app_notification)

    while True:
        command = input()

        if command in EXIT_REQUEST:
            break
        elif command == VIDEO_REQUEST or command == FIND_VIDEO_REQUEST:
            handle_videos(videos, command)
        elif command == PLAYLIST_REQUEST:
            handle_playlists(playlists)
        else:
            print(NOT_FOUND_INFO)


start_app()
