class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash (self, string):
        uni_code = 0
        if not isinstance(string, str):
            print('this should be a sting')
        else:
            for char in string:
                    uni_code += ord(char)
        return uni_code           
    
    def add (self, key, value):
        index = self.hash(key)
        if index not in self.collection:
            self.collection[index] = {}
        self.collection[index][key] = value

    def remove (self, key):
        index = self.hash(key)
        if index in self.collection:
            if key in self.collection[index]:
                del self.collection[index][key]
    def lookup (self, key):
        index = self.hash(key)
        if index in self.collection:
            return self.collection[index].get(key)
        else:
            return

