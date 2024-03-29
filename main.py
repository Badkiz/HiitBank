import _md5
import time
import random

class Account:
    def __int__(self, fname, lname, pin, passcode, account_no, balance, email, bvn):
        self.__fname = fname
        self.__lname = lname
        self.__address = None
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__balance = 0.0
        self.__account_no = "888" + str((random.randint(1000000, 9999999)))
        self.__nin = None
        if bvn == None:
            self.__bvn = str(random.randint(1000000000, 9999999999))
        else:
            self.__bvn

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_address(self):
        return self.__address

    def get_phone_no(self):
        return self.__phone_no

    def get_email(self):
        return self.__email

    def get_pin(self):
        return self.__pin

    def get_bvn(self):
        return self.__bvn

    def get_balance(self):
        return self.__balance

    def get_nin(self):
        return self.__nin

    def get_account_no(self):
        return self.__account_no

    def set_fname(self, fname):
        assert type(fname) == str, "only strings allowed for first name"
        self.__fname = fname

    def set_lname(self, lname):
        assert type(lname) == str, "only strings are allowed for last name"
        self.__lname = lname

    def set_email(self, email):
        assert type(email) == str, "only strings allowed for email"
        self.__email = email

    def set_phone_no(self, phone_no):
        assert type(phone_no) == str, "only strings allowed"
        self.__phone_no = phone_no

    def set_pin(self, new_pin: str):
        assert type(new_pin) == str, " new pin is not a string"
        assert new_pin.isnumeric(), "pin provided should contain only numbers"
        self.__pin = new_pin

    def set_passcode(self, new_passcode):
        assert type(new_passcode) == str, "new pass conde provided must be string"
        self.__passcode = _md5.md5(new_passcode)

    def set_address(self, address):
        assert type(address) == str, "address provided is not a string"
        self.__address = address

    def set_bvn(self, bvn: str):
        assert type(bvn) == str, "bvn inputed is not a string"
        assert bvn.isnumeric(), "bvn should contain only numbers"
        self.__bvn

    def set_nin(self, nin: str):
        assert type(nin) == str, "nin must be string"
        assert nin.isnumeric(), "nin must be numeric"
        self.__nin = None

    def withdraw(self,amount:float)->float:
        assert type(amount)==float,'Amount must be a number '
        assert amount>0,'Amount to withdraw must be positive'
        assert amount <self.__balance,'insufficent funds'

        self.__balance-=amount
        return self.__balance
    def deposit(self,amount:float)->float:
        assert  type(amount)==float,"Amount ust be a number "
        assert amount>0