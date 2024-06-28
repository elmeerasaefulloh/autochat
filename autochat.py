import requests
import time
import random

sentences = [
    'Saya memprediksi bahwa proyek ini akan berkembang pesat sebagai crypto terkuat di masa depan.',
    'Proyek ini memiliki prospek yang besar.',
    'Tentu saja saat ini, saya percaya bahwa ini adalah proyek terbaik.',
    'Ini pasti akan menjadi BESAR!',
    'Tim telah menjadi inspirasi dalam pendekatan inovatif mereka untuk mencapai tujuan dan visi proyek.',
    'Saya sangat senang menjadi bagian dari ini.',
    'Proyek ini memiliki masa depan yang sangat cerah.',
    'Terima kasih juga kepada teman-teman dan Terima kasih telah berbagi kesempatan yang luar biasa ini.',
    'Semoga sukses untuk semua tim dengan kesempatan untuk ambil bagian dalam proyek besar ini. Saya berharap proyek ini akan berkembang dengan baik dan akan mencapai bulan.',
    'Saya mulai menyukai proyek ini. Saya hanya berharap dan berdoa proyek ini sukses, saya akan mencoba keberuntungan saya.',
    'Proyek Anda sangat bagus. Whitepaper juga sangat jelas. Saya berharap proyek Anda dapat sukses dan berhasil di masa depan. Saya juga berharap komunitas dapat tumbuh lebih besar dari sekarang.'
]

channel_id = input('Masukkan ID channel: ')
waktu = int(input('Masukkan waktu jeda (dalam detik): '))
auth_token = input('Masukkan Authorization token bot: ')

headers = {
    'Authorization': auth_token,
    'Content-Type': 'application/json'
}

while True:
    message = random.choice(sentences)
    payload = {
        'content': message
    }
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
    if response.status_code == 200:
        print('Pesan berhasil dikirim!')
        message_id = response.json()['id']
        time.sleep(1)
        delete_response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
        if delete_response.status_code == 204:
            print('Pesan berhasil dihapus!')
        else:
            print('Gagal menghapus pesan!')
    else:
        print('Pesan gagal dikirim!')
    
    time.sleep(waktu)
