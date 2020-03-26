import random #random kütüphanesini import ettik
class Env_tic_tac_toe(): #Ortam class ını oluşturduk.
    def __init__(self,random_play):  #Class parametre olarak bir random_play alacak.
        self.random_play = random_play #Dışarıdan gelecek olan random_play verisini kendi classımıza atadık.
        self.state = [[0,0,0],[0,0,0],[0,0,0]] #Durumu belirtmek için iki boyutlu bir dizi kullandık
        self.done = 0 #Oyunun bitip bitmediğini kontrol ediyoruz. 0 bitmediği anlamına gelir.
        self.random_agent_value ="O" # random ajanın değeri, biz random ajan için O değerini seçtik.
        self.winner = "Random Agenet" # Oyun bittiğinde kimin kazandığını bize söyleyecek olan değişken. Şimdilik ajanın kazandığını varsayıyoruz.
     #Ortamda bir adım atma fonksiyonu yazıyoruz

    def step(self,action,agent_value): #agent_value burada XOX değerlerini tutacak, bu isteğe bağlı olarak değiştirilebilir.
        #aksiyon kodlamasını şu şekilde yapacağız:
        if(self.state[action[0]][action[1]] != 0): #actionlar ile lokasyon belirleyeceğiz
            print("Bir Hata Var Bu kareye oynanamaz")
        else: self.state[action[0]][action[1]] = agent_value #Buradaki kareye ajanın değerini yazdık. Bu Satırdayke henüz agen_value yi daha oluşturmadık

        if(self.control_win(self.state) == agent_value): #Birazdan kimin kazandığını döndüren control_win fonksiyonu oluşturacağız. Burada ajanın kazandığı durumu kontrol ediyoruz
            self.done = 1 #Oyun duracak çünkü bir kazanan var.
            self.winner = "Agent " + agent_value #Kazanan agent oldu.
        if(self.control_win(self.state) == "BERABERE"): #Beraberlik durumu konrol ediliyor.
            self.done = 1
            self.winner = "BERABERE"
            #random u hareket ettirmeden önce randomun kazanıp kazanmadığını kontrol etmeliyiz.
        if(self.control_win(self.state) == self.random_agent_value):
            self.done = 1
            
        if(self.done != 1 and self.random_play == 1): #Oyun devam ediyorsa random ajan hareket etsin.
            self.random_agent_act() # random ajanı hareket ettiren fonksiyon henüz oluşturulmadı.
        return (self.state, self.done, self.winner)
    def control_win(self,state): #Kazananı kontrol eden control_win() fonksiyonunu şimdi yazıyoruz.
        for i in range(3): #Tek tek bütün durumları kontrol edeceğiz.
            if(state[i][0] != 0 and state[i][0] == state[i][1] and state[i][0]==state[i][2]): #Aynı satırda üçlüyü tamamlayarak kazandıp kazanmadığını kontrol ediyoruz.
                return state[i][0]
            if(state[0][i] != 0 and state[0][i]==state[1][i] and state[0][i]==state[2][i]): #Aynı sütunu kontrol ettik.
                return state[0][i]
            if(state[0][0] != 0 and state[0][0]==state[1][1] and state[0][0] == state[2][2]): #Çaprazı kontrol ettik.
                return state[0][0]
            if(state[0][2]!= 0 and state[0][2] == state[1][1] and state[2][0] == state[0][2]): #Diğer çaprazı kontrol ettik.
                return state[0][2]
        empty_spaces = [] # Boş olan yerle, sadece bu alanlara oynanabilir.
        for i in range(3):  #Bu döngüde boş alanlar kontrol edip dizi olarak empty_spaces dizisinin içine attık.
            for j in range(3):
                if(self.state[i][j] == 0):
                    empty_spaces.append([i,j])
        if(len(empty_spaces) == 0): #eğer boş alan dizisinin uzunluğu sıfır olursa, yani hiç boş alan kalmazsa oyun berabere.
            return "BERABERE"
        else:
            return 0
    def random_agent_act(self): #Random ajanı hareket ettiren fonksiyonu oluşturuyoruz.
        empty_spaces = [] # Boş olan yerle, sadece bu alanlara oynanabilir.
        for i in range(3):  #Bu döngüde boş alanlar kontrol edip dizi olarak empty_spaces dizisinin içine attık.
            for j in range(3):
                if(self.state[i][j] == 0):
                    empty_spaces.append([i,j])
        random_act = random.choice(list(enumerate(empty_spaces)))[0]
        action = empty_spaces[random_act]
        self.state[action[0]][action[1]] = self.random_agent_value #ajanın hareketini yani actionları belirledik.
#class ın dışında main fonksiyonumuz olacak fonksiyonu yazıyoruz
def learn_random_agent():
    episode = 5 # beş bölüm oynasın.
    for i in range(episode):
        env = Env_tic_tac_toe(random_play = 1) #doğru manasında.
        done = 0
        agent_value = "X" #randomunki O idi bizimki X olsun
        state = env.state
        print("episode",i)
        while(not done):
            
            empty_spaces = [] # Boş olan yerle, sadece bu alanlara oynanabilir.
            for i in range(3):  #Bu döngüde boş alanlar kontrol edip dizi olarak empty_spaces dizisinin içine attık.
                for j in range(3):
                    if(state[i][j] == 0): #Control edilmeli.
                        empty_spaces.append([i,j])
            random_act = random.choice(list(enumerate(empty_spaces)))[0]
            action = empty_spaces[random_act]
            new_s, done, winner = env.step(action,agent_value)
            print(state)
            state = new_s #Sürekli yeni durum oluşturmak için yaptık
            if(done == 1):
                print("Kazanan: " + winner)
learn_random_agent()
        
            
            
        
        
        
        
        
            
            
            
            
           
           
        
        
            

        
            
