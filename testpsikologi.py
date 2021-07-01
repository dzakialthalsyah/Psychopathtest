from termcolor import colored
from pyfiglet import figlet_format


class classpsikologi:
    def __init__(self, nilai1, nilai2, nilai3, nilai4, nilai5, nilai6, nilai7, nilai8, nilai9, nilai10):
        self.nilainya1 = nilai1
        self.nilainya2 = nilai2
        self.nilainya3 = nilai3
        self.nilainya4 = nilai4
        self.nilainya5 = nilai5
        self.nilainya6 = nilai6
        self.nilainya7 = nilai7
        self.nilainya8 = nilai8
        self.nilainya9 = nilai9
        self.nilainya10 = nilai10

    def functionprint(self):
        print((colored(figlet_format("PSYCHOPATH TEST", font="future_1"), color="red")))
        print((colored("-------------------- Coded by Dzaki Althalsyah -------------------- \n", color="blue")))
        print((colored(
            "Github: https://github.com/dzakialthalsyah/   ||   Instagram: https://instagram.com/dzakialthalsyah/ \n\n\n",
            color="cyan")))

        q1 = input("""1.
Kamu melihat sebuah kereta yang akan menabrak dan membunuh lima orang.
Saat itu kamu sedang berada di atas jembatan dan berdiri di samping orang asing bertubuh besar.
Kamu ingin menghentikan kereta tersebut tapi badanmu terlalu kecil. Tetapi jika kamu mendorong
orang asing di sebelahmu ke rel dan membunuhnya, kamu akan menyelamatkan lima orang tersebut.
Apakah kamu akan mendorongnya?

option:
a = ya
b = tidak

jawaban: 
""")

        if q1 == "a":
            try:
                nilai1_hasil1 = self.nilainya1 + 1
                print(nilai1_hasil1)
            except:
                pass

        elif q1 == "b":
            try:
                nilai1_hasil1 = self.nilainya2 - 1
                print(nilai1_hasil1)
            except:
                pass
        else:
            print("salah")

        q2 = input("""2.
Ada dua orang saudara wanita bernama Clara dan Gaby. Suatu hari ketika berada
di pemakaman ibunya, Clara melihat seorang pemuda tampan dan langsung jatuh cinta.
Namun sayang Clara tak bisa menemukan pemuda itu karena tak tahu siapa dia sebenarnya.
Nah pada suatu hari Clara membunuh saudarinya, Gaby. Mengapa Clara melakukan hal itu? 

option:
a = Clara membunuh Gaby dengan harapan lelaki tampan tersebut 
akan datang kembali saat pemakaman Claire berlangsung.
b = Dua wanita ini mencintai lelaki yang sama (terlibat cinta segitiga) 
atau dengan kata lain Clara cemburu kepada Gaby sehingga ia membunuhnya.

jawaban: """)

        if q2 == "b":
            try:
                nilai2_hasil1 = self.nilainya2 + 1
            except:
                pass

        elif q2 == "a":
            try:
                nilai2_hasil1 = self.nilainya2 - 1
            except:
                pass
        else:
            print("salah")

        q3 = input("""3.
Jika disuruh memilih antara warna merah dan putih, warna apa yang akan kamu pilih? 

option:
a = putih
b = merah

jawaban: """)

        if q3 == "b":
            try:
                nilai3_hasil1 = self.nilainya3 + 1
            except:
                pass

        elif q3 == "a":
            try:
                nilai3_hasil1 = self.nilainya3 - 1
            except:
                pass
        else:
            print("salah")

        q4 = input("""4.
Saat pertama kali bertemu dengan orang yang kamu sukai, apa hal yang akan kamu lakukan? 

option:
a = Kamu akan mengenalkan diri kamu apa adanya.
b = Kamu akan mengungkapkan segala kelebihan kamu yang bisa membuatnya terpesona dan membuatmu terlihat sempurna di matanya.

jawaban: """)

        if q4 == "a":
            try:
                nilai4_hasil1 = self.nilainya4 + 1
            except:
                pass

        elif q4 == "b":
            try:
                nilai4_hasil1 = self.nilainya4 - 1
            except:
                pass
        else:
            print("salah")

        q5 = input("""5.
Seorang anak mendapatkan hadiah ulang tahun berupa sepeda dan sepatu sepak bola,
tetapi dia tidak menyukainya. Apa alasannya? 

option:
a = Anak itu mengalami cacat kaki.
b = Anak tersebut tidak suka bersepeda dan bermain sepak bola. Dia lebih menyukai olahraga lain seperti badminton atau bola basket.

jawaban: """)

        if q5 == "b":
            try:
                nilai5_hasil1 = self.nilainya5 + 1
            except:
                pass

        elif q5 == "a":
            try:
                nilai5_hasil1 = self.nilainya5 - 1
            except:
                pass
        else:
            print("salah")

        q6 = input("""6.
Pilih satu dari empat hal ini. Perkelahian, kenakalan, sikap brutal, atau pornografi? 

option:
a = Brutal, perkelahian, kenakalan
b = Brutal, perkelahian, pornografi

jawaban: """)

        if q6 == "a":
            try:
                nilai6_hasil1 = self.nilainya6 + 1
            except:
                pass

        elif q6 == "b":
            try:
                nilai6_hasil1 = self.nilainya6 - 1
            except:
                pass
        else:
            print("salah")

        q7 = input("""7.
Kamu sedang menginap di lantai 10 sebuah hotel. Tiba-tiba ketika kamu melongok dari balkon,
kamu melihat seorang pembunuh yang tengah menghabisi nyawa korbannya. Apesnya,
pembunuh tersebut melihatmu dan kamu bisa melihat bahwa dia mendekatkan jarinya ke wajahnya
sambil membuat gestur atau gerakan tubuh. Gestur seperti apa yang dibuatnya? 

option:
a = Kamu akan melihat bahwa si pembunuh mendekatkan jarinya ke bibirnya dan meminta kamu diam.
b = Kamu melihat si pembunuh sedang menghitung di lantai mana kamu tinggal supaya bisa membunuhmu 
juga sehingga kamu akan bersiap agar kamu tidak akan dibunuh juga.

jawaban: """)

        if q7 == "a":
            try:
                nilai7_hasil1 = self.nilainya7 + 1
            except:
                pass

        elif q7 == "b":
            try:
                nilai7_hasil1 = self.nilainya7 - 1
            except:
                pass
        else:
            print("salah")

        q8 = input("""8.
Ada perampok masuk ke rumahmu. Kebetulan di dapurmu hanya ada pisau dapur tajam yang baru
kamu asah dan pisau buah tetapi tidak terlalu tajam. Mana pisau yang akan kamu pilih untuk
membunuh si perampok? 

option:
a = memilih pisau yang tak terlalu tajam.
b = memilih pisau tajam.

jawaban: """)

        if q8 == "b":
            try:
                nilai8_hasil1 = self.nilainya8 + 1
            except:
                pass

        elif q8 == "a":
            try:
                nilai8_hasil1 = self.nilainya8 - 1
            except:
                pass
        else:
            print("salah")

        q9 = input("""9.
Kamu punya tetangga yang jarang terlihat. Kira-kira ada apa dengannya? 

option:
a = tetanggamu hanya sedang sibuk.
b = Dia tidak begitu suka dengan keramaian.

jawaban: """)

        if q9 == "a":
            try:
                nilai9_hasil1 = self.nilainya9 + 1
            except:
                pass

        elif q9 == "b":
            try:
                nilai9_hasil1 = self.nilainya9 - 1
            except:
                pass
        else:
            print("salah")

        q10 = input("""10.
Seandainya kamu diharuskan membunuh seseorang dan kamu tahu bahwa orang tersebut sedang
bersembunyi di dalam lemari, apa yang akan kamu lakukan? 
option:
a = Membiarkannya ketakutan hingga dia akhirnya keluar dari lemari, barulah membunuhnya
b = Segera membuka lemari dan membunuhnya.

jawaban: """)

        if q10 == "b":
            try:
                nilai10_hasil1 = self.nilainya10 + 1
            except:
                pass

        elif q10 == "a":
            try:
                nilai10_hasil1 = self.nilainya10 - 1
            except:
                pass
        else:
            print("salah")

        hasil_keseluruhan = nilai1_hasil1 + nilai2_hasil1 + nilai3_hasil1 + nilai4_hasil1 + nilai5_hasil1 + nilai6_hasil1 + nilai7_hasil1 + nilai8_hasil1 + nilai9_hasil1 + nilai10_hasil1

        if hasil_keseluruhan >= 8:
            print("\n\nHasil = 100% bukan psikopat")

        elif hasil_keseluruhan >= 6 and hasil_keseluruhan < 8:
            print("\n\nHasil = bukan psikopat")

        elif hasil_keseluruhan <= 2:
            print("\n\nHasil = 100% psikopat")

        elif hasil_keseluruhan >= 3 < 5:
            print("\n\nHasil = psikopat")
        elif hasil_keseluruhan == 5:
            print("\n\nHasil = bisa jadi psikopat")
        else:
            pass


p1 = classpsikologi(0, 0, 0, 0, 0, 0, 0 , 0, 0, 0)
p1.functionprint()