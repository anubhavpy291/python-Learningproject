class pc:
    
    @staticmethod
    def info(namee):
        n = []
        spec = {"dell inspiration 3537": (6,"i5 4200u",720,"itnel hd 4400")}
        if spec.get(namee):
            print(namee)
            print("----------------------------------------")
            print(f"ram: {spec.get(namee)[0]}gb")
            print(f"cpu: {spec.get(namee)[1]}")
            print(f"storage: {spec.get(namee)[2]}gb")
            print(f"gpu: {spec.get(namee)[3]}")
            print("--------------------------------------")
        else:
            print("data is unavaliable")
pc.info("dell inspiration 3537")

