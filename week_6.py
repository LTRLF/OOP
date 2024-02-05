# Class Code
class User:
    def __init__(self, user_ID, user_name):
        self.__user_ID = user_ID
        self.__user_name = user_name
        self.__account_list = []

    def add_account(self, User_Account):
        self.__account_list.append(User_Account)
    
    @property
    def account(self):
        return self.__account_list

class User_Account:
    def __init__ (self, account_no, balance, user):
        self.__account_no = account_no
        self.__balance = balance
        self.__transaction_list = []
        self.__atm_card = None
        
        self.__user = user

    def accdeposit(self,transaction):
        if transaction.amount > 0 and isinstance(transaction,Transaction):
            self.__balance += transaction.amount
            #เอาจนใเงินปัจจุบันยัดใน transaction total balance
            transaction.total_balance = self.__balance
            self.add_transaction(transaction)
            return "complete"
        else:
            return "Invalid"
        
    def accwithdraw(self,transaction):
        if transaction.amount > 0 and isinstance(transaction,Transaction):
            self.__balance -= transaction.amount
            transaction.total_balance = self.__balance
            self.add_transaction(transaction)
            return "complete"
        else:
            return "invalid"
    
    def acctransfer(self,transaction):
        if transaction.amount > 0 and transaction.amount <= self.__balance and isinstance(transaction,Transaction):
            #check ว่าเป็นแอคเดียวกันไหม
            if self != transaction.target_account:
                #update transfer account and make transaction record
                self.cur_balance -= transaction.amount
                self.add_transaction(transaction)
                #update target_account and make transaction record
                target_account = transaction.target_account
                target_account.__balance += transaction.amount
                target_account.add_transaction(transaction)
                return "complete"
            else:
                return "Error"
        else:
            return "invalid"

    @property
    def atm_card(self):
        return self.__atm_card
    @property
    def account_no(self):
        return self.__account_no
    @property
    def cur_balance(self):
        return self.__balance
    @cur_balance.setter
    def cur_balance(self, new_balance):
        self.__balance = new_balance
    
    @property
    def transaction_list(self):
        return self.__transaction_list
    def add_transaction(self, transaction_list):
        self.__transaction_list.append(transaction_list)
    def add_card(self, atm_card):
        self.__atm_card = atm_card

class ATM:
    withdraw_limit = 40000

    def __init__(self, atm_no, balance):
        self.__atmNo = atm_no
        self.__balance = balance

    def deposit(self, account_info, amount):
        if isinstance(account_info,User_Account) and amount > 0:
            self.__balance += amount
            if account_info.accdeposit(Transaction('D', amount, 'today', self.__atmNo)) == "complete":
                return 'Success'
            else:
                return 'Error'
        else:
            return "Error"

    def withdraw(self, account_info, amount):
        if amount > 0 and amount <= ATM.withdraw_limit and isinstance(account_info,User_Account) and amount <= account_info.cur_balance:
            self.__balance -= amount
            if account_info.accwithdraw(Transaction('W', amount, 'today', self.__atmNo)) == "complete":
                return "Success"
            else:
                return "Error"
        else:
            return "Error"

    def transfer(self, account_info, target_account, amount):
        if amount > 0 and account_info.cur_balance >= amount and isinstance(account_info,User_Account) and isinstance(target_account,User_Account):
            transaction_out = Transaction('T-', amount, 'today', self.__atmNo, target_account)
            transaction_out.add_target_account(target_account)
            if account_info.acctransfer(transaction_out) == "complete":
                transaction_in = Transaction('T+', amount, 'today', self.__atmNo, target_account)
                transaction_in.add_target_account(target_account)
                target_account.acctransfer(transaction_in)
                return 'Success'
            else:
                return 'Error'

    def insert_card(self, bank_info, atm_card, input_pin):
        #วน user ใน bank
        for that_user in bank_info.user_list:
            #วน account ใน user
            for that_account in that_user.account:
                if that_account.atm_card ==  atm_card and that_account.atm_card.pin == input_pin:
                    return that_account
                else:  
                    return None

class ATM_Card:
    def __init__(self, card_no, pin):
        self.__card_no = card_no
        self.__pin = pin

    @property
    def card_no(self):
        return self.__card_no
    @property
    def pin(self):
        return self.__pin

class Bank:
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []

    def add_user(self, user):
        self.__user_list.append(user)

    def add_atm(self, atm):
        self.__atm_list.append(atm)

    def card_fee(self, user_list):
        for that_user in user_list:
            for that_account in that_user:
                #สำหรับ account นั้นใน user นั้น จะไปเรียก atm_card(atm_card) มา 
                if that_user.that_account.atm_card != None:
                    #ถ้า card exist ให้ set current balance -150
                    that_user.that_account.balance -= 150

    @property
    def user_list(self):
        return self.__user_list
    @property
    def atm_list(self):
        return self.__atm_list

class Transaction:
    def __init__(self, transact_type, amount, date , atmNo, target_account = None):
        self.__transact_type = transact_type
        self.__amount = amount
        self.__date   = date
        self.__atmNo  = atmNo
        self.__target_account = target_account
        self.__total_balance = None

    def add_target_account(self, target_account):
        self.__target_account = target_account

    @property
    def target_account(self):
        return self.__target_account
    @property
    def amount(self):
        return self.__amount
    def get_total_balance(self):
        return self.__total_balance
    def set_total_balance(self, pre_balance):
        self.__total_balance = pre_balance

    total_balance = property(get_total_balance, set_total_balance)

    def __str__(self):
        return f"{self.__date} -> {self.__transact_type} -ATM:{self.__atmNo}-{self.__amount} -> Balance = {self.__total_balance}"

    #กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user ={'1-1101-12345-42-0':['Harry Potter'         ,'1234567890','12345',20000],
       '1-1101-12345-43-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def create_data(user,atm):
    i=0
    bank_info = Bank()
    #.items() แยกตัว key, value ใน dictionary ออกเป็นสองก้อน
    for key,value in user.items():
        user_info = User(key,value[0])     
        account_info = User_Account(value[1], value[3], user_info)
        i+=1
        card_info = ATM_Card(value[2], 1233+i)
        account_info.add_card(card_info)
        user_info.add_account(account_info)
        bank_info.add_user(user_info)

    for key,value in atm.items():
        atm_info = ATM(key,value)
        bank_info.add_atm(atm_info)

    return bank_info

bank = create_data(user,atm)

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
# TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

user1 = bank.user_list[0]
user2 = bank.user_list[1]
HarryAcc    = user1.account[0]
HermioneAcc = user2.account[0]
Harrycard = HarryAcc.atm_card
Hermionecard = HermioneAcc.atm_card

atm1 = bank.atm_list[0]
atm2 = bank.atm_list[1]

print("Test case #1")
print(f"{atm1.insert_card(bank,Harrycard,1234).atm_card.card_no}, {atm1.insert_card(bank,Harrycard,1234).account_no}, Success")


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2")
print(f"Hermione account before test : {HermioneAcc.cur_balance}")
atm2.deposit(HermioneAcc, 1000)
print(f"Hermione account after test : {HermioneAcc.cur_balance}")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
print(atm2.deposit(HermioneAcc, -1))

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4")
print(f"Hermione account before test : {HermioneAcc.cur_balance}")
atm2.withdraw(HermioneAcc, 500)
print(f"Hermione account after test : {HermioneAcc.cur_balance}")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5")
print(atm2.withdraw(HermioneAcc, -2000))

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6")
print(f"Harry account before test : {HarryAcc.cur_balance}")
print(f"Hermione account before test : {HermioneAcc.cur_balance}")
atm2.transfer(HarryAcc, HermioneAcc, 10000)
print(f"Harry account after test : {HarryAcc.cur_balance}")
print(f"Hermione account after test : {HermioneAcc.cur_balance}")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
for all_transaction in HermioneAcc.transaction_list:
    print("Hermione transaction : ", all_transaction)