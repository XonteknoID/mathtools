import os, sys, math, time


m = "\33[91m"
h = "\33[92m"
k = "\33[93m"
b = "\33[96m"
p = "\33[97m"
d = "\33[90m"
bm = "\33[41m"
bk = "\33[43m"
bp = "\33[49m"
bold = "\33[1m"


head = (f'''{bold}
{m}╔═                                                                  ═╗
 {h}╔═══╦══╗    ╔═╗╔═╗╔═══════╗    ╔═╦════╗
 {h}║      ╠═══╦╝ ╚╣ ║║__ ___ ╠╦═══╣ ║    ║{d} ├{m}⇒»{b}〉{p}Creator {m}:{p} Xontek noID 
 {h}║  ╔ ╗ ║ ╔╗╠╗ ╔╝ ╚═╗║ ║║ ╔╗║ ╔╗║ ║  ╚═╣{d} ├{m}⇒»{b}〉{p}Email {m}:\33[95mxontek@gmail.com
 {h}║  ║ ║ ║ ╚╝║║ ╠╣ ╔╗║║ ║║ ║║║ ║║║ ╠══╗ ║{d} ├{m}⇒»{b}〉{p}Facebook {m}:{p} NO ID
 {h}║  ╚╦╝ ║ ╔╗║║ ╚║ ║║║║ ║║ ╚╝║ ╚╝║ ╚    ║ \33[95mhttps://github.com/XonteknoID{bp}
 {h}╚═══╩══╩═╩═╝╚══╩═╝╚╝╚═╝╚═══╩═══╩══╩═══╝
                    {k}<{m}/{k}> {p}{bm}Mathematics Tool V1.0{bp} {k}<{m}/{k}>
{m}╚═                                                                  ═╝{p}''')
def sp(a):
      for e in a + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.002)

def home():
      os.system("clear")
      sp(head)
      sp(f'''
   {p}┌───────{m}〈{h} Menu {m}〉{p}────────────┐
   {p}├─{m}»{b}〉{p}1{m}.{p} Kalkulator Sederhana  │
   {p}├─{m}»{b}〉{p}2{m}.{p} BMIGen                │
   {p}├─{m}»{b}〉{p}3{m}.{p} Konvensi Panjang      │
   {p}├─{m}»{b}〉{p}4{m}.{p} Konvensi Massa        │
   {p}├─{m}»{b}〉{p}0{m}.{p} Keluar( Exit )        │
   {p}└─────────────────────────────┘
   ''')
      choice = input(f"   {m}⊨{b}〉{p}Pilih Menu {m}>>{p} ")
      while choice!= "1" and choice!= "2" and choice!= "3" and choice!= "4" and choice!= "0":
            print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[ {h}Pilihan Kamu Tidak Ada Dalam Menu{m} ]")
            choice = input(f"   {m}⊨{b}〉{p}Pilih Menu {m}>>{p} ")
      
      if choice == "1":
            calc()
      elif choice == "2":
            bmigen()
      elif choice == "3":
            long_conversation()
      elif choice == "4":
            conversation_mass()
      else :
            os.system("clear")
            print("           Thanks you  ヾ(＾-＾)ノ ")
            exit()
            
def calc():
      def home_calc():
            
            os.system("clear")
            print(head)
            sp(f'''                        {m}"{p}KALKULATOR SEDERHANA{m}"
   {p}┌───{m}〈{h} Operasi Math {m}〉{p}───────────────┐
   {p}│ 1{m}. {p}Penjumlahan    6{m}. {p}Pangkat 2     │
   {p}│ 2{m}. {p}Pengurangan    7{m}. {p}Pangkat 3     │
   {p}│ 3{m}. {p}Perkalian                       │
   {p}│ 4{m}. {p}Pembagian      9{m}. {p}Kembali       │
   {p}│ 5{m}. {p}Akar Kuadrat   0{m}. {p}Keluar        │
   {p}└────────────────────────────────────┘
   ''')
            choice = input(f"   {m}⊨{b}〉{p}Pilih Operasi Math {m}>>{p} ")
            while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6" and choice!="7" and choice!="9" and choice!="0":
                  print(f"   {m}[{k}!{m}] {h}Error {m}[{k}!{m}]\n   {m}[ {h}Pilihan Kamu Tidak Ada Di Dalam Operasi Math {m}]")
                  choice = input(f"   {m}⊨{b}〉{p}Pilih Operasi Math {m}>>{p} ")
            if choice == "1":
                  add()
            elif choice == "2":
                  subtract()
            elif choice == "3":
                  multiply()
            elif choice == "4":
                  divide()
            elif choice == "5":
                  square_root()
            elif choice == "6":
                  rank_two()
            elif choice == "7":
                  cube()
            elif choice == "9":
                  home()
            else:
                  os.system("clear")
                  print("           Thanks you  ヾ(＾-＾)ノ ")
                  exit()
      
      def add():
            os.system("clear")
            print(head)
            menu = "1"
            sp(f"   {p}───{m}〈{h} Operasi Penjumlahan {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Angka Pertama {m}>>{p} ")
            y = input(f"   {m}⊨{b}〉{p}Angka Kedua   {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n{p}   {x} {m}+{p} {y} {m}={p} {float(x)+ float(y)}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def subtract():
            os.system("clear")
            print(head)
            menu = "2"
            sp(f"   {p}───{m}〈{h} Operasi Pengurangan {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Angka Pertama {m}>>{p} ")
            y = input(f"   {m}⊨{b}〉{p}Angka Kedua   {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n{p}   {x} {m}-{p} {y} {m}={p} {float(x)- float(y)}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def multiply():
            os.system("clear")
            print(head)
            menu = "3"
            sp(f"   {p}───{m}〈{h} Operasi Perkalian {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Angka Pertama {m}>>{p} ")
            y = input(f"   {m}⊨{b}〉{p}Angka Kedua   {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n{p}   {x} {m}×{p} {y} {m}={p} {float(x)* float(y)}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def divide():
            os.system("clear")
            print(head)
            menu = "4"
            sp(f"   {p}───{m}〈{h} Operasi Pembagian {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Angka Pertama {m}>>{p} ")
            y = input(f"   {m}⊨{b}〉{p}Angka Kedua   {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n{p}   {x} {m}÷{p} {y} {m}={p} {float(x) / float(y)}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def square_root():
            os.system("clear")
            print(head)
            menu = "5"
            sp(f"   {p}───{m}〈{h} Operasi Akar Kuadrat {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Masukan Angka {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n   {m}√ {p}{x} {m}={p} {math.sqrt(float(x))}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def rank_two():
            os.system("clear")
            print(head)
            menu = "6"
            sp(f"   {p}───{m}〈{h} Operasi Pangkat 2 {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Masukan Angka {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n    {p}{x} ² {m}={p} {float(x) **2}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def cube():
            os.system("clear")
            print(head)
            menu = "7"
            sp(f"   {p}───{m}〈{h} Operasi Pangkat 3 {m}〉{p}───────────────")
            x = input(f"   {m}⊨{b}〉{p}Masukan Angka {m}>>{p} ")
            print(f"\n    {m}[ {h}HASIL {m}]")
            print(f"\n    {p}{x} ³ {m}={p} {float(x) **3}")
            mode = input(f"\n   Ketik ({k}A{m}/{k}a{p}) untuk menghitung lagi{m},{p}({k}B{m}/{k}b{p}) untuk kembali ke menu \n dan ({k}Q{m}/{k}q{p}) untuk keluar{m}..{p} ")
            back_exit_again(mode, menu)
      def back_exit_again(mode, menu):
            if str(mode).upper() == "A":
                  if menu == "1":
                        add()
                  elif menu == "2":
                        subtract()
                  elif menu == "3":
                        multiply()
                  elif menu == "4":
                        divide()
                  elif menu == "5":
                        square_root()
                  elif menu == "6":
                        rank_two()
                  elif menu == "7":
                        cube()
            elif str(mode).upper() == "B":
                  home_calc()
            else:
                  os.system('clear')
                  print("           Thanks you  ヾ(＾-＾)ノ ")
                  exit()
            
            
      if __name__=="__main__":
            home_calc()
            
def bmigen():
      def home_bmi():
            os.system("clear")
            print(head)
            sp(f'''                             {m}"{p}BMI Gen{m}"
 {h}Apa itu BMI {k}?
   {p}Body Mass Index ({h}BMI{p}) atau Indeks Massa Tubuh ({h}IMT{p}) adalah 
 angka yang menjadi penilaian standar untuk menentukan
 apakah berat badan Anda tergolong {b}normal{m},{b} kurang{m},{b} berlebih{m},{p} 
 atau {b}obesitas{m}.{p}berdasarkan tinggi badan dan berat badan{m}.
   {p}Dengan ketentuan sebagai berikut{m}:
 {h}Cowok {m}:
   {h}BMI {m}<{p} 17 {m}={b} Kurus
   {h}BMI {p}17{m}-{p}22 {m}={b} Normal
   {h}BMI {p}23{m}-{p}27 {m}={b} Gendut
   {h}BMI {m}>{p} 27 {m}={b} Obesitas atau Kegemukan 
 {h}Cewek {m}:
   {h}BMI {m}<{p} 18 {m}={b} Kurus
   {h}BMI {p}18{m}-{p}24 {m}={b} Normal
   {h}BMI {p}24{m}-{p}27 {m}={b} Gendut
   {h}BMI {m}>{p} 27 {m}={b} Obesitas atau Kegemukan ''') 
            choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
            while choice!= "" and choice!= "b" and choice!= "q":
                  choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
                 
            if choice == "":
                  main_bmi()
            elif choice == "b":
                  home()
            else:
                  os.system('clear')
                  print("           Thanks you  ヾ(＾-＾)ノ ")
                  exit()
      
      def main_bmi():
            os.system("clear")
            print(head)
            print(f'                              {m}"{p}BMI Gen{m}"\n\n   ')
            name = input(f"   {m}⊨{b}〉{p}Siapa Namamu {m}>>{p} ")
            sex = input(f"   {m}⊨{b}〉{p}Jenis Kelamin ({k}Co{m}/{k}Ce{p}) {m}>>{p} ").lower()
            while sex!="co" and sex!= "ce":
                  print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[{h} Cowok (co) Cewek(ce) {m}]")
                  sex = input(f"   {m}⊨{b}〉{p}Jenis Kelamin ({k}Co{m}/{k}Ce{p}) {m}>>{p} ").lower()
            bb = int(input(f"   {m}⊨{b}〉{p}Berat Badan ({k}Kg{p}) {m}>>{p} "))
            tb1 = int(input(f"   {m}⊨{b}〉{p}Tinggi Badan ({k}Cm{p}) {m}>>{p} "))
            tb2 = tb1/100
            bmi = int(bb/(tb2*tb2))
            
            def male():
                  if bmi < 17:
                        cc = "Kurus（┬┬＿┬┬）"
                  elif bmi >= 17 and bmi < 23:
                        cc = "Normal (-^〇^-)"
                  elif bmi >= 24 and bmi < 27:
                        cc = "Gendut (•ˋ _ ˊ•)"
                  else:
                        cc = "Obesitas o(╥﹏╥)"
                  return cc
            def female():
                  if bmi < 18:
                        cc = "Kurus（┬┬＿┬┬）"
                  elif bmi >= 18 and bmi < 25:
                        cc = "Normal (-^〇^-)"
                  elif bmi >= 25 and bmi < 27:
                        cc = "Gendut (•ˋ _ ˊ•)"
                  else:
                        cc = "Obesitas o(╥﹏╥)"
                  return cc
                  
            def output(hasil_bmi):
                  print(f'''
    {m}╔════════════════════════════════════════════════╗
         Hey {b}{name} {p}!                         
      Tinggi Badanmu {b}{tb1}{p} cm                 
      Berat Badanmu {b}{bb}{p} kg                   
      BMI kamu {b}{bmi}{p}                          
                                              
        Dari Hasil Di Atas,                   
      Di Simpulkan Kamu Orangnya {b}{hasil_bmi}  
    {m}╚════════════════════════════════════════════════╝ 
      ''')
                  go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung BMImu ({k}y{m}/{k}n{p}) ")
                  while go_again!= "y" and go_again!= "n":
                        go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung BMImu ({k}y{m}/{k}n{p}) ")
                        
                  if go_again == "y":
                        main_bmi()
                  else:
                        home()
      
            if sex == "co":
                  r=male()
                  output(r)
            else:
                  r=female()
                  output(r)
            
      
      
      if __name__=="__main__":
            home_bmi()
            
def long_conversation():
      unit_length = ["km","hm","dam","m","dm","cm","mm"]
      description = (f'''
  {h}Km                  {m}"{p}KONVERSI SATUAN PANJANG{m}"                    
 {m}┌───┐                                         
 {m}│   │{h}Hm                                      {p}┌{m}〈 {h}Satuan Panjang {m}〉{p}─┐
 {m}│{h}▲{m}  └───┐       {p} Setiap Naik Satu{p}            │                     │
 {m}│┃      │{h}Dam         {p}Tangga {m}÷{p} 10{p}             │ {m}[{h}Km{m}] {p}Kilo Meter     │
 {m}│┃┃     └───┐                                {p}│ {m}[{h}Hm{m}] {p}Hekto Meter    │
 {m}│┃┃         │ {h}M       {p}Setiap Turun Satu{p}      │{m}[{h}Dam{m}] {p}Deka Meter     │
 {m}│┃┃         └───┐         {p}Tangga {m}x {p}10{p}        │  {m}[{h}M{m}] {p}Meter          │
 {m}│┃┃             │{h}Dm                          {p}│ {m}[{h}Dm{m}] {p}Desi Meter     │
 {m}│┃┃             └───┐                        {p}│ {m}[{h}Cm{m}] {p}Centi Meter    │
 {m}│┃┃                 │{h}Cm                      {p}│ {m}[{h}Mm{m}] {p}Mili Meter     │
 {m}│ ┃                 └───┐                    {p}│                     │
 {m}│ {h}▼{m}                     │{h}Mm                  {p}└─────────────────────┘
 {m}│                       └───┐         {p}Masukan Input Sesuai Dengan
 {m}│  {p}TANGGA SATUAN PANJANG{m}    │      {p}Tabel Satuan Panjang di Atas
 {m}└───────────────────────────┘      {m}[{k}!{m}] {h}Contoh{m}( {p}Dari {m}: {h}Km{m}, {p}Ke {m}: {h}M {m}) \n''')
      def home_length():
            os.system("clear")
            print(head)
            sp(description)
            choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
            while choice!= "" and choice!= "b" and choice!= "q":
                  choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
                       
            if choice == "":
                  from_to_long_conversation()
            elif choice == "b":
                  home()
            else:
                  os.system('clear')
                  print("           Thanks you  ヾ(＾-＾)ノ ")
                  exit()
      def from_to_long_conversation():
            os.system("clear")
            print(head)
            print(description)
      
            from_ = input(f"   {m}⊨{b}〉{p}DARI {m}>>{p} ").lower()
            while from_!= "km" and from_!= "hm" and from_!= "dam" and from_!= "m" and from_!= "dm" and from_!= "cm" and from_!= "mm":
                  print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[{h} Masukan Satuan Panjang {m}]")
                  from_ = input(f"   {m}⊨{b}〉{p}DARI {m}>>{p} ").lower()
            to_ = input(f"   {m}⊨{b}〉{p}KE {m}>>{p} ").lower()
            while to_!= "km" and to_!= "hm" and to_!= "dam" and to_!= "m" and to_!= "dm" and to_!= "cm" and to_!= "mm":
                  print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[{h} Masukan Satuan Panjang {m}]")
                  to_ = input(f"   {m}⊨{b}〉{p}KE {m}>>{p} ").lower()
                  
            def main_length():
                  os.system("clear")
                  print(head)
                  print(description)
                  print(f"{p}──────{m}〈{h} Konversi {from_}{m}/{h}{to_} {m}〉{p}──────────\n" )
                  numb = int(input(f"   {m}⊨{b}〉{p}Berapa {h}{from_} {m}>>{p} "))
            
                  results = numb
                  if unit_length.index(from_) < unit_length.index(to_):
                        for i in range (unit_length.index(to_) - unit_length.index(from_)):
                              results *= 10
                        
                  else:
                        for i in range (unit_length.index(from_) - unit_length.index(to_)):
                              results /= 10
                              
                  print(f"\n──────{m}〈{h} Hasil Konversi {from_}{m}/{h}{to_} {m}〉{p}──────────\n" )
                  print(f"   {numb}{h} {from_} {m}= {p}{results}{h} {to_}")
                  
                  go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung ({from_}/{to_}) ({k}y{m}/{k}n{p}) ")
                  while go_again!= "y" and go_again!= "n":
                        go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung ({from_}/{to_}) ({k}y{m}/{k}n{p}) ")
                        
                  if go_again == "y":
                        main_length()
                  else:
                        home_length()
                  
            if __name__=="__main__":
                  main_length()
                              
                  
            
            
      if __name__=="__main__":
            home_length()
def conversation_mass():
      mass_unit = ["kg","hg","dag","g","dg","cg","mg"]
      description = (f'''
  {h}Kg                  {m}"{p}KONVERSI SATUAN MASA{m}"                    
 {m}┌───┐                                         
 {m}│   │{h}Hg {m}= {h}ons                                {p}┌{m}〈   {h}Satuan Masa  {m}〉{p}─┐
 {m}│{h}▲{m}  └───┐       {p} Setiap Naik Satu{p}            │                     │
 {m}│┃      │{h}Dag         {p}Tangga {m}÷{p} 10{p}             │ {m}[{h}Kg{m}] {p}Kilo Gram      │
 {m}│┃┃     └───┐                                {p}│ {m}[{h}Hg{m}] {p}Hekto Gram     │
 {m}│┃┃         │ {h}G       {p}Setiap Turun Satu{p}      │{m}[{h}Dag{m}] {p}Deka Gram      │
 {m}│┃┃         └───┐         {p}Tangga {m}x {p}10{p}        │  {m}[{h}G{m}] {p}Gram           │
 {m}│┃┃             │{h}Dg                          {p}│ {m}[{h}Dg{m}] {p}Desi Gram      │
 {m}│┃┃             └───┐                        {p}│ {m}[{h}Cg{m}] {p}Centi Gram     │
 {m}│┃┃                 │{h}Cg                      {p}│ {m}[{h}Mg{m}] {p}Mili Gram      │
 {m}│ ┃                 └───┐                    {p}│                     │
 {m}│ {h}▼{m}                     │{h}Mg                  {p}└─────────────────────┘
 {m}│                       └───┐         {p}Masukan Input Sesuai Dengan
 {m}│  {p}TANGGA SATUAN MASA   {m}    │      {p}Tabel Satuan Masa di Atas
 {m}└───────────────────────────┘      {m}[{k}!{m}] {h}Contoh{m}( {p}Dari {m}: {h}Kg{m}, {p}Ke {m}: {h}g {m}) \n''')
      def home_mass():
            os.system("clear")
            print(head)
            sp(description)
            choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
            while choice!= "" and choice!= "b" and choice!= "q":
                  choice = input(f"{p} type ({k}B{m}/{k}b{p}) to return to main menu{m},{p} ({k}Q{m}/{k}q{p})to exit and enter to start{m}...{p} ").lower()
                       
            if choice == "":
                  from_to_conversation_mass()
            elif choice == "b":
                  home()
            else:
                  os.system('clear')
                  print("           Thanks you  ヾ(＾-＾)ノ ")
                  exit()
      def from_to_conversation_mass():
            os.system("clear")
            print(head)
            print(description)
      
            from_ = input(f"   {m}⊨{b}〉{p}DARI {m}>>{p} ").lower()
            while from_!= "kg" and from_!= "hg" and from_!= "dag" and from_!= "g" and from_!= "dg" and from_!= "cg" and from_!= "mg":
                  print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[{h} Masukan Satuan Masa {m}]")
                  from_ = input(f"   {m}⊨{b}〉{p}DARI {m}>>{p} ").lower()
            to_ = input(f"   {m}⊨{b}〉{p}KE {m}>>{p} ").lower()
            while to_!= "kg" and to_!= "hg" and to_!= "dag" and to_!= "g" and to_!= "dg" and to_!= "cg" and to_!= "mg":
                  print(f"   {m}[{k}!{m}]{h} Error {m}[{k}!{m}]\n   {m}[{h} Masukan Satuan Masa {m}]")
                  to_ = input(f"   {m}⊨{b}〉{p}KE {m}>>{p} ").lower()
                  
            def main_mass():
                  os.system("clear")
                  print(head)
                  print(description)
                  print(f"{p}──────{m}〈{h} Konversi {from_}{m}/{h}{to_} {m}〉{p}──────────\n" )
                  numb = int(input(f"   {m}⊨{b}〉{p}Berapa {h}{from_} {m}>>{p} "))
            
                  results = numb
                  if mass_unit.index(from_) < mass_unit.index(to_):
                        for i in range (mass_unit.index(to_) - mass_unit.index(from_)):
                              results *= 10
                        
                  else:
                        for i in range (mass_unit.index(from_) - mass_unit.index(to_)):
                              results /= 10
                              
                  print(f"\n──────{m}〈{h} Hasil Konversi {from_}{m}/{h}{to_} {m}〉{p}──────────\n" )
                  print(f"   {numb}{h} {from_} {m}= {p}{results}{h} {to_}")
                  
                  go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung ({from_}/{to_}) ({k}y{m}/{k}n{p}) ")
                  while go_again!= "y" and go_again!= "n":
                        go_again = input(f"  {m}[{k}?{m}] {p}Apa Kamu Ingin Kembali Menghitung ({from_}/{to_}) ({k}y{m}/{k}n{p}) ")
                        
                  if go_again == "y":
                        main_mass()
                  else:
                        home_mass()
                  
            if __name__=="__main__":
                  main_mass()
                              
                  
            
            
      if __name__=="__main__":
            home_mass()
            
if __name__=="__main__":
      home()