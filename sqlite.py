import sqlite3

# 連結
con = sqlite3.connect('city.db')

# 物件(keelung)
cursor_keelung = con.cursor()
keelung_area = [(1,'中正區') , (2,'七堵區') , (3,'暖暖區') ,
           (4,'仁愛區') , (5,'中山區') , (6,'安樂區') , (7,'信義區')]

# 檢查資料表是否存在
cursor_keelung.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('keelung',))
result = cursor_keelung.fetchone()
if result:
    print('keelung 資料表已經存在')
else:
    # 建立資料表
    cursor_keelung.execute('CREATE TABLE keelung (id INT , area TEXT)')
    for keelung in keelung_area :
        cursor_keelung.execute('INSERT INTO keelung VALUES (? , ?)' , keelung)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(taipei)
cursor_taipei = con.cursor()
taipei_area = [(1,'松山區') , (2,'信義區') , (3,'大安區') ,(4,'中山區') , 
               (5,'中正區') , (6,'大同區') , (7,'萬華區') ,(8,'文山區') , 
               (9,'南港區') , (10,'內湖區') , (11,'士林區') , (12,'北投區')]

# 檢查資料表是否存在
cursor_taipei.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('taipei',))
result = cursor_taipei.fetchone()
if result:
    print('taipei 資料表已經存在')
else:
    # 建立資料表
    cursor_taipei.execute('CREATE TABLE taipei (id INT , area TEXT)')
    for taipei in taipei_area :
        cursor_taipei.execute('INSERT INTO taipei VALUES (? , ?)' , taipei)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(new_taipei)
cursor_new_taipei = con.cursor()
new_taipei_area = [(1,'板橋區') , (2,'三重區') , (3,'中和區') ,(4,'永和區') , (5,'新莊區') , 
                   (6,'新店區') , (7,'樹林區') , (8,'鶯歌區') , (9,'三峽區') , (10,'淡水區') , 
                   (11,'汐止區') , (12,'瑞芳區') , (13,'土城區') , (14,'蘆洲區') , (15,'五股區') , 
                   (16,'泰山區') , (17,'林口區') , (18,'深坑區') , (19,'石碇區') , (20,'坪林區') , 
                   (21,'三芝區') , (22,'石門區') , (23,'八里區') , (24,'平溪區') , (25,'雙溪區') , 
                   (26,'貢寮區') , (27,'金山區') , (28,'萬里區') , (29,'烏來區') ]   # 未修改

# 檢查資料表是否存在
cursor_new_taipei.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('new_taipei',))
result = cursor_new_taipei.fetchone()
if result:
    print('new_taipei 資料表已經存在')
else:
    # 建立資料表
    cursor_new_taipei.execute('CREATE TABLE new_taipei (id INT , area TEXT)')
    for new_taipei in new_taipei_area :
        cursor_new_taipei.execute('INSERT INTO new_taipei VALUES (? , ?)' , new_taipei)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(taoyuan)
cursor_taoyuan = con.cursor()
taoyuan_area = [(1,'桃園區') , (2,'中壢區') , (3,'大溪區') ,(4,'楊梅區') , (5,'蘆竹區') , 
                (6,'大園區') , (7,'龜山區') , (8,'八德區') , (9,'龍潭區') , (10,'平鎮區') , 
                (11,'新屋區') , (12,'觀音區') , (13,'復興區') ]

# 檢查資料表是否存在
cursor_taoyuan.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('taoyuan',))
result = cursor_taoyuan.fetchone()
if result:
    print('taoyuan 資料表已經存在')
else:
    # 建立資料表
    cursor_taoyuan.execute('CREATE TABLE taoyuan (id INT , area TEXT)')
    for taoyuan in taoyuan_area :
        cursor_taoyuan.execute('INSERT INTO taoyuan VALUES (? , ?)' , taoyuan)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(hsinchu_county) 新竹縣
cursor_hsinchu_county = con.cursor()
hsinchu_county_area = [(1,'竹北市') , (2,'竹東鎮') , (3,'新埔鎮') ,(4,'關西鎮') , (5,'湖口鄉') , 
                       (6,'新豐鄉') , (7,'芎林鄉') , (8,'橫山鄉') , (9,'北埔鄉') , (10,'寶山鄉') , 
                       (11,'峨眉鄉') , (12,'尖石鄉') , (13,'五峰鄉') ] 

# 檢查資料表是否存在
cursor_hsinchu_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('hsinchu_county',))
result = cursor_hsinchu_county.fetchone()
if result:
    print('hsinchu_county 資料表已經存在')
else:
    # 建立資料表
    cursor_hsinchu_county.execute('CREATE TABLE hsinchu_county (id INT , area TEXT)')
    for hsinchu_county in hsinchu_county_area :
        cursor_hsinchu_county.execute('INSERT INTO hsinchu_county VALUES (? , ?)' , hsinchu_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(hsinchu) 新竹市
cursor_hsinchu = con.cursor()
hsinchu_area = [(1,'東區') , (2,'北區') , (3,'香山區') ]

# 檢查資料表是否存在
cursor_hsinchu.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('hsinchu',))
result = cursor_hsinchu.fetchone()
if result:
    print('hsinchu 資料表已經存在')
else:
    # 建立資料表
    cursor_hsinchu.execute('CREATE TABLE hsinchu (id INT , area TEXT)')
    for hsinchu in hsinchu_area :
        cursor_hsinchu.execute('INSERT INTO hsinchu VALUES (? , ?)' , hsinchu)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(miaoli_county) 苗栗縣
cursor_miaoli_county = con.cursor()
miaoli_county_area = [(1,'苗栗市') , (2,'苑裡鎮') , (3,'通宵鎮') ,(4,'竹南鎮') , (5,'頭份市') , 
                      (6,'後龍鎮') , (7,'卓蘭鎮') , (8,'大湖鄉') , (9,'公館鄉') , (10,'銅鑼鄉') , 
                      (11,'南庄鄉') , (12,'頭屋鄉') , (13,'三義鄉') , (14,'西湖鄉') , (15,'造橋鄉') , 
                      (16,'三灣鄉') , (17,'獅潭鄉') , (18,'泰安鄉') ] 


# 檢查資料表是否存在
cursor_miaoli_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('miaoli_county',))
result = cursor_miaoli_county.fetchone()
if result:
    print('miaoli_county 資料表已經存在')
else:
    # 建立資料表
    cursor_miaoli_county.execute('CREATE TABLE miaoli_county (id INT , area TEXT)')
    for miaoli_county in miaoli_county_area :
        cursor_miaoli_county.execute('INSERT INTO miaoli_county VALUES (? , ?)' , miaoli_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(taichung) 台中
cursor_taichung = con.cursor()
taichung_area = [(1,'中區') , (2,'東區') , (3,'南區') ,(4,'西區') , (5,'北區') , 
                 (6,'西屯區') , (7,'南屯區') , (8,'北屯區') , (9,'豐原區') , (10,'大甲區') , 
                 (11,'清水區') , (12,'沙鹿區') , (13,'梧棲區') , (14,'后里區') , (15,'神岡區') , 
                 (16,'潭子區') , (17,'大雅區') , (18,'新社區') , (19,'石岡區') , (20,'外埔區') , 
                 (21,'大安區') , (22,'烏日區') , (23,'大肚區') , (24,'龍井區') , (25,'霧峰區') , 
                 (26,'太平區') , (27,'大里區') , (28,'和平區')]


# 檢查資料表是否存在
cursor_taichung.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('taichung',))
result = cursor_taichung.fetchone()
if result:
    print('taichung 資料表已經存在')
else:
    # 建立資料表
    cursor_taichung.execute('CREATE TABLE taichung (id INT , area TEXT)')
    for taichung in taichung_area :
        cursor_taichung.execute('INSERT INTO taichung VALUES (? , ?)' , taichung)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(nantou_county) 南投縣
cursor_nantou_county = con.cursor()
nantou_county_area = [(1,'南投市') , (2,'埔里鎮') , (3,'草屯鎮') ,(4,'竹山鎮') , (5,'集集鎮') , 
                      (6,'名間鄉') , (7,'鹿谷鄉') , (8,'中寮鄉') , (9,'魚池鄉') , (10,'國姓鄉') , 
                      (11,'水里鄉') , (12,'信義鄉') , (13,'仁愛鄉') ]


# 檢查資料表是否存在
cursor_nantou_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('nantou_county',))
result = cursor_nantou_county.fetchone()
if result:
    print('nantou_county 資料表已經存在')
else:
    # 建立資料表
    cursor_nantou_county.execute('CREATE TABLE nantou_county (id INT , area TEXT)')
    for nantou_county in nantou_county_area :
        cursor_nantou_county.execute('INSERT INTO nantou_county VALUES (? , ?)' , nantou_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(changhua_county) 彰化縣
cursor_changhua_county = con.cursor()
changhua_county_area = [(1,'彰化市') , (2,'鹿港鎮') , (3,'和美鎮') ,(4,'線西鄉') , (5,'伸港鄉') , 
                        (6,'福興鄉') , (7,'秀水鄉') , (8,'花壇鄉') , (9,'芬園鄉') , (10,'員林市') , 
                        (11,'溪湖鎮') , (12,'田中鎮') , (13,'大村鄉') , (14,'埔鹽鄉') , (15,'埔心鄉') , 
                        (16,'永靖鄉') , (17,'社頭鄉') , (18,'二水鄉') , (19,'北斗鎮') , (20,'二林鎮') , 
                        (21,'田尾鄉') , (22,'埤頭鄉') , (23,'芳苑鄉') , (24,'大城鄉') , (25,'竹塘鄉') , 
                        (26,'溪州鄉')]

# 檢查資料表是否存在
cursor_changhua_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('changhua_county',))
result = cursor_changhua_county.fetchone()
if result:
    print('changhua_county 資料表已經存在')
else:
    # 建立資料表
    cursor_changhua_county.execute('CREATE TABLE changhua_county (id INT , area TEXT)')
    for changhua_county in changhua_county_area :
        cursor_changhua_county.execute('INSERT INTO changhua_county VALUES (? , ?)' , changhua_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(yunlin_county) 雲林縣
cursor_yunlin_county = con.cursor()
yunlin_county_area = [(1,'斗六市') , (2,'斗南鎮') , (3,'虎尾鎮') ,(4,'西螺鎮') , (5,'土庫鎮') , 
                      (6,'北港鎮') , (7,'古坑鄉') , (8,'大埤鄉') , (9,'莿桐鄉') , (10,'林內鄉') , 
                      (11,'二崙鄉') , (12,'崙背鄉') , (13,'麥寮鄉') , (14,'東勢鄉') , (15,'褒忠鄉') , 
                      (16,'臺西鄉') , (17,'元長鄉') , (18,'四湖鄉') , (19,'口湖鄉') , (20,'水林鄉')]



# 檢查資料表是否存在
cursor_yunlin_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('yunlin_county',))
result = cursor_yunlin_county.fetchone()
if result:
    print('yunlin_county 資料表已經存在')
else:
    # 建立資料表
    cursor_yunlin_county.execute('CREATE TABLE yunlin_county (id INT , area TEXT)')
    for yunlin_county in yunlin_county_area :
        cursor_yunlin_county.execute('INSERT INTO yunlin_county VALUES (? , ?)' , yunlin_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(chiayi_county) 嘉義縣
cursor_chiayi_county = con.cursor()
chiayi_county_area = [(1,'太保市') , (2,'朴子市') , (3,'布袋鎮') ,(4,'大林鎮') , (5,'民雄鄉') , 
                      (6,'溪口鄉') , (7,'新港鄉') , (8,'六腳鄉') , (9,'東石鄉') , (10,'義竹鄉') , 
                      (11,'鹿草鄉') , (12,'水上鄉') , (13,'中埔鄉') , (14,'竹崎鄉') , (15,'梅山鄉') , 
                      (16,'番路鄉') , (17,'大埔鄉') , (18,'阿里山鄉')]



# 檢查資料表是否存在
cursor_chiayi_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('chiayi_county',))
result = cursor_chiayi_county.fetchone()
if result:
    print('chiayi_county 資料表已經存在')
else:
    # 建立資料表
    cursor_chiayi_county.execute('CREATE TABLE chiayi_county (id INT , area TEXT)')
    for chiayi_county in chiayi_county_area :
        cursor_chiayi_county.execute('INSERT INTO chiayi_county VALUES (? , ?)' , chiayi_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(chiayi) 嘉義市
cursor_chiayi = con.cursor()
chiayi_area = [(1,'東區') , (2,'西區')]



# 檢查資料表是否存在
cursor_chiayi.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('chiayi',))
result = cursor_chiayi.fetchone()
if result:
    print('chiayi 資料表已經存在')
else:
    # 建立資料表
    cursor_chiayi.execute('CREATE TABLE chiayi (id INT , area TEXT)')
    for chiayi in chiayi_area :
        cursor_chiayi.execute('INSERT INTO chiayi VALUES (? , ?)' , chiayi)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(tainan) 台南市
cursor_tainan = con.cursor()
tainan_area = [(1,'新營區') , (2,'鹽水區') , (3,'白河區') , (4,'柳營區') , (5,'後壁區') , 
               (6,'東山區') , (7,'麻豆區') , (8,'下營區') , (9,'六甲區') , (10,'官田區') , 
               (11,'大內區') , (12,'佳里區') , (13,'學甲區') , (14,'西港區') , (15,'七股區') , 
               (16,'將軍區') , (17,'北門區') , (18,'新化區') , (19,'善化區') , (20,'新市區') , 
               (21,'安定區') , (22,'上山區') , (23,'玉井區') , (24,'楠西區') , (25,'南化區') , 
               (26,'左鎮區') , (27,'仁德區') , (28,'歸仁區') , (29,'關廟區') , (30,'龍崎嶇') , 
               (31,'永康區') , (32,'東區') , (33,'南區') , (34,'北區') , (35,'安南區') , 
               (36,'安平區') , (37,'中西區')]

# 檢查資料表是否存在
cursor_tainan.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('tainan',))
result = cursor_tainan.fetchone()
if result:
    print('tainan 資料表已經存在')
else:
    # 建立資料表
    cursor_tainan.execute('CREATE TABLE tainan (id INT , area TEXT)')
    for tainan in tainan_area :
        cursor_tainan.execute('INSERT INTO tainan VALUES (? , ?)' , tainan)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(kaohsiung) 高雄市
cursor_kaohsiung = con.cursor()
kaohsiung_area = [(1,'鹽埕區') , (2,'鼓山區') , (3,'左營區') , (4,'楠梓區') , (5,'三民區') , 
                  (6,'興新區') , (7,'前金區') , (8,'苓雅區') , (9,'前鎮區') , (10,'旗津區') , 
                  (11,'小港區') , (12,'鳳山區') , (13,'林園區') , (14,'大寮區') , (15,'大樹區') , 
                  (16,'大社區') , (17,'仁武區') , (18,'鳥松區') , (19,'岡山區') , (20,'橋頭區') , 
                  (21,'燕巢區') , (22,'田寮區') , (23,'阿蓮區') , (24,'路竹區') , (25,'湖內區') , 
                  (26,'茄萣區') , (27,'永安區') , (28,'彌陀區') , (29,'梓官區') , (30,'旗山嶇') , 
                  (31,'美濃區') , (32,'六龜區') , (33,'甲仙區') , (34,'杉林區') , (35,'內門區') , 
                  (36,'茂林區') , (37,'桃源區') , (38,'那瑪夏區')]

# 檢查資料表是否存在
cursor_kaohsiung.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('kaohsiung',))
result = cursor_kaohsiung.fetchone()
if result:
    print('kaohsiung 資料表已經存在')
else:
    # 建立資料表
    cursor_kaohsiung.execute('CREATE TABLE kaohsiung (id INT , area TEXT)')
    for kaohsiung in kaohsiung_area :
        cursor_kaohsiung.execute('INSERT INTO kaohsiung VALUES (? , ?)' , kaohsiung)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(pingtung_county) 屏東縣
cursor_pingtung_county = con.cursor()
pingtung_county_area = [(1,'屏東市') , (2,'潮州鎮') , (3,'東港鎮') , (4,'恆春鎮') , (5,'萬丹鄉') , 
                        (6,'長治鄉') , (7,'麟洛鄉') , (8,'九如鄉') , (9,'里港鄉') , (10,'鹽埔鄉') , 
                        (11,'高樹鄉') , (12,'萬巒鄉') , (13,'內埔鄉') , (14,'竹田鄉') , (15,'新埤鄉') , 
                        (16,'枋寮鄉') , (17,'新園鄉') , (18,'崁頂鄉') , (19,'林邊鄉') , (20,'南州鄉') , 
                        (21,'佳冬鄉') , (22,'琉球鄉') , (23,'車城鄉') , (24,'滿洲鄉') , (25,'枋山鄉') , 
                        (26,'三地門鄉') , (27,'霧臺鄉') , (28,'瑪家鄉') , (29,'泰武鄉') , (30,'來義鄉') , 
                        (31,'春日鄉') , (32,'獅子鄉') , (33,'牡丹鄉')]

# 檢查資料表是否存在
cursor_pingtung_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('pingtung_county',))
result = cursor_pingtung_county.fetchone()
if result:
    print('pingtung_county 資料表已經存在')
else:
    # 建立資料表
    cursor_pingtung_county.execute('CREATE TABLE pingtung_county (id INT , area TEXT)')
    for pingtung_county in pingtung_county_area :
        cursor_pingtung_county.execute('INSERT INTO pingtung_county VALUES (? , ?)' , pingtung_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(taitung_county) 台東縣
cursor_taitung_county = con.cursor()
taitung_county_area = [(1,'臺東市') , (2,'成功鎮') , (3,'關山鎮') , (4,'卑南鄉') , (5,'鹿野鄉') , 
                       (6,'池上鄉') , (7,'東河鄉') , (8,'長濱鄉') , (9,'太麻里鄉') , (10,'大武鄉') , 
                       (11,'綠島鄉') , (12,'海端鄉') , (13,'延平鄉') , (14,'金鋒鄉') , (15,'達人鄉') , 
                       (16,'蘭嶼鄉')]



# 檢查資料表是否存在
cursor_taitung_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('taitung_county',))
result = cursor_taitung_county.fetchone()
if result:
    print('taitung_county 資料表已經存在')
else:
    # 建立資料表
    cursor_taitung_county.execute('CREATE TABLE taitung_county (id INT , area TEXT)')
    for taitung_county in taitung_county_area :
        cursor_taitung_county.execute('INSERT INTO taitung_county VALUES (? , ?)' , taitung_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(hualien_county) 花蓮縣
cursor_hualien_county = con.cursor()
hualien_county_area = [(1,'花蓮市') , (2,'鳳林鎮') , (3,'玉里鎮') , (4,'新城鄉') , (5,'吉安鄉') , 
                       (6,'壽豐鄉') , (7,'光復鄉') , (8,'豐濱鄉') , (9,'瑞穗鄉') , (10,'富里鄉') , 
                       (11,'秀林鄉') , (12,'萬榮鄉') , (13,'卓溪鄉')]

# 檢查資料表是否存在
cursor_hualien_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('hualien_county',))
result = cursor_hualien_county.fetchone()
if result:
    print('hualien_county 資料表已經存在')
else:
    # 建立資料表
    cursor_hualien_county.execute('CREATE TABLE hualien_county (id INT , area TEXT)')
    for hualien_county in hualien_county_area :
        cursor_hualien_county.execute('INSERT INTO hualien_county VALUES (? , ?)' , hualien_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(yilan_county) 宜蘭縣
cursor_yilan_county = con.cursor()
yilan_county_area = [(1,'宜蘭市') , (2,'羅東鎮') , (3,'蘇澳鎮') , (4,'頭城鎮') , (5,'礁溪鄉') , 
                     (6,'壯圍鄉') , (7,'員山鄉') , (8,'冬山鄉') , (9,'五結鄉') , (10,'三星鄉') , 
                     (11,'大同鄉') , (12,'南澳鄉')]

# 檢查資料表是否存在
cursor_yilan_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('yilan_county',))
result = cursor_yilan_county.fetchone()
if result:
    print('yilan_county 資料表已經存在')
else:
    # 建立資料表
    cursor_yilan_county.execute('CREATE TABLE yilan_county (id INT , area TEXT)')
    for yilan_county in yilan_county_area :
        cursor_yilan_county.execute('INSERT INTO yilan_county VALUES (? , ?)' , yilan_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(penghu_county) 澎湖縣
cursor_penghu_county = con.cursor()
penghu_county_area = [(1,'馬公市') , (2,'湖西鄉') , (3,'白沙鄉') , (4,'西嶼鄉') , (5,'望安鄉') , 
                      (6,'七美鄉')]

# 檢查資料表是否存在
cursor_penghu_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('penghu_county',))
result = cursor_penghu_county.fetchone()
if result:
    print('penghu_county 資料表已經存在')
else:
    # 建立資料表
    cursor_penghu_county.execute('CREATE TABLE penghu_county (id INT , area TEXT)')
    for penghu_county in penghu_county_area :
        cursor_penghu_county.execute('INSERT INTO penghu_county VALUES (? , ?)' , penghu_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(kinmen_county) 金門縣
cursor_kinmen_county = con.cursor()
kinmen_county_area = [(1,'金城鎮') , (2,'金沙鎮') , (3,'金湖鎮') , (4,'金寧鄉') , (5,'烈嶼鄉') , 
                      (6,'烏坵鄉')]

# 檢查資料表是否存在
cursor_kinmen_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('kinmen_county',))
result = cursor_kinmen_county.fetchone()
if result:
    print('kinmen_county 資料表已經存在')
else:
    # 建立資料表
    cursor_kinmen_county.execute('CREATE TABLE kinmen_county (id INT , area TEXT)')
    for kinmen_county in kinmen_county_area :
        cursor_kinmen_county.execute('INSERT INTO kinmen_county VALUES (? , ?)' , kinmen_county)
    con.commit() # 儲存變更
# --------------------------------------------------------------------- #

# 物件(lienchiang_county) 連江縣
cursor_lienchiang_county = con.cursor()
lienchiang_county_area = [(1,'南竿鄉') , (2,'北竿鄉') , (3,'莒光鄉') , (4,'東引鄉')]

# 檢查資料表是否存在
cursor_lienchiang_county.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('lienchiang_county',))
result = cursor_lienchiang_county.fetchone()
if result:
    print('lienchiang_county 資料表已經存在')
else:
    # 建立資料表
    cursor_lienchiang_county.execute('CREATE TABLE lienchiang_county (id INT , area TEXT)')
    for lienchiang_county in lienchiang_county_area :
        cursor_lienchiang_county.execute('INSERT INTO lienchiang_county VALUES (? , ?)' , lienchiang_county)
    con.commit() # 儲存變更



















# # 讀取資料
# cursor_keelung.execute('SELECT * FROM keelung')
# keelung_data = cursor_keelung.fetchall()
# print(keelung_data)
# print()

# cursor_taipei.execute('SELECT * FROM taipei')
# taipei_data = cursor_taipei.fetchall()
# print(taipei_data)
# print()

# cursor_new_taipei.execute('SELECT * FROM new_taipei')
# new_taipei_data = cursor_new_taipei.fetchall()
# print(new_taipei_data)
# print()

# cursor_taoyuan.execute('SELECT * FROM taoyuan')
# taoyuan_data = cursor_taoyuan.fetchall()
# print(taoyuan_data)
# print()

# cursor_hsinchu_county.execute('SELECT * FROM hsinchu_county')
# hsinchu_county_data = cursor_hsinchu_county.fetchall()
# print(hsinchu_county_data)
# print()

# cursor_hsinchu.execute('SELECT * FROM hsinchu') # 新竹市
# hsinchu_data = cursor_hsinchu.fetchall()
# print(hsinchu_data)
# print()

# cursor_miaoli_county.execute('SELECT * FROM miaoli_county') # 苗栗縣
# miaoli_county_data = cursor_miaoli_county.fetchall()
# print(miaoli_county_data)
# print()

# cursor_taichung.execute('SELECT * FROM taichung') # 台中
# taichung_data = cursor_taichung.fetchall()
# print(taichung_data)
# print()

# cursor_nantou_county.execute('SELECT * FROM nantou_county') # 南投縣
# nantou_county_data = cursor_nantou_county.fetchall()
# print(nantou_county_data)
# print()

# cursor_changhua_county.execute('SELECT * FROM changhua_county') # 彰化縣
# changhua_county_data = cursor_changhua_county.fetchall()
# print(changhua_county_data)
# print()

# cursor_yunlin_county.execute('SELECT * FROM yunlin_county') # 雲林縣
# yunlin_county_data = cursor_yunlin_county.fetchall()
# print(yunlin_county_data)
# print()

# cursor_chiayi_county.execute('SELECT * FROM chiayi_county') # 嘉義縣
# chiayi_county_data = cursor_chiayi_county.fetchall()
# print(chiayi_county_data)
# print()

# cursor_chiayi.execute('SELECT * FROM chiayi') # 嘉義縣
# chiayi_data = cursor_chiayi.fetchall()
# print(chiayi_data)
# print()

# cursor_tainan.execute('SELECT * FROM tainan') # 台南市
# tainan_data = cursor_tainan.fetchall()
# print(tainan_data)
# print()

# cursor_kaohsiung.execute('SELECT * FROM kaohsiung') # 高雄市
# kaohsiung_data = cursor_kaohsiung.fetchall()
# print(kaohsiung_data)
# print()

# cursor_pingtung_county.execute('SELECT * FROM pingtung_county') # 屏東縣
# pingtung_county_data = cursor_pingtung_county.fetchall()
# print(pingtung_county_data)
# print()

# cursor_taitung_county.execute('SELECT * FROM taitung_county') # 台東縣
# taitung_county_data = cursor_taitung_county.fetchall()
# print(taitung_county_data)
# print()

# cursor_hualien_county.execute('SELECT * FROM hualien_county') # 花蓮縣
# hualien_county_data = cursor_hualien_county.fetchall()
# print(hualien_county_data)
# print()

# cursor_yilan_county.execute('SELECT * FROM yilan_county') # 宜蘭縣
# yilan_county_data = cursor_yilan_county.fetchall()
# print(yilan_county_data)
# print()

# cursor_penghu_county.execute('SELECT * FROM penghu_county') # 澎湖縣
# penghu_county_data = cursor_penghu_county.fetchall()
# print(penghu_county_data)
# print()

# cursor_kinmen_county.execute('SELECT * FROM kinmen_county') # 金門縣
# kinmen_county_data = cursor_kinmen_county.fetchall()
# print(kinmen_county_data)
# print()

# cursor_lienchiang_county.execute('SELECT * FROM lienchiang_county') # 連江縣
# lienchiang_county_data = cursor_lienchiang_county.fetchall()
# print(lienchiang_county_data)
# print()




# print(keelung_data[0][1])  # 基隆的第一個資料
# print(taipei_data[1][0])  # 台北的第二個資料

con.close()  # 關閉資料庫連線
