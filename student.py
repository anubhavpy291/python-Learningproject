class st:
    sts = {}
    totalgpa = 0
    totalstd = 0
    @staticmethod
    def addusr(gpa,name):
        st.sts.update({name: gpa})
        st.totalgpa += gpa
        st.totalstd += 1
    def hi(self):
        pass
    @classmethod
    def stinfo(cls):
        print(f"the average gpa is {(cls.totalgpa / cls.totalstd):.2f}")
   
    @classmethod
    def stfullinfo(cls):
        print("name: gpa")
        print("------------------------------------")
        for key, iva in cls.sts.items():
            
            print(f"{key}: {iva}")
        print("------------------------------------")
        st.stinfo()
        print("------------------------------------")

isrun = True
def addusers():
    na = input("enter the stuent  name to add: ")
    sp = float(input("enter the gpa for student: "))
    st.addusr(sp,na)

while isrun:
    ins = input("add/list: ")
    if ins == "add" or ins == "a":
        addusers()
    elif ins == "list" or ins == "l":
        st.stfullinfo()