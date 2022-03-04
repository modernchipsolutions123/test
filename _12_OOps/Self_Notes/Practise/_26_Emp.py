class Emp(object):
    def __init__(self,id):
        self.id = id

    def __add__(self, obj):
        result = self.id + obj.id  # 10 + 20
        return result
kad = Emp(10)
print("Kad obj ", kad)
ali = Emp(20)
print("ali obj ", ali)

print("Adding both objects", kad + ali)

