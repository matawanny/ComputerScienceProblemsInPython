class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, (record_key, record_value) in enumerate(bucket):
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, (record_key, record_value) in enumerate(bucket):
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


if __name__ == "__main__":
    hash_table = AlgoHashTable(256)
    hash_table.set_val('mashrur@example.com', {'first_name': 'Mashrur', 'last_name':'Hoasain'})
    hash_table.set_val('johndoe@example.com', {'first_name': 'John', 'last_name':'Doe'})
    print(hash_table)
    hash_table.set_val('mashrur@example.com', {'first_name': 'Mashrur', 'last_name':'Python'})
    print(hash_table)
    print(hash_table.get_val('mashrur@example.com'))