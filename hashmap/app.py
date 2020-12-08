from hashmap.hash_algo import AlgoHashTable


if __name__ == "__main__":
    hash_table =AlgoHashTable(256)
    with open("data.txt") as f:
        for line in f:
            key, value = line.split(":")
            hash_table.set_val(key, value)

print(hash_table.get_val('mashrur@example.com'))
print(hash_table.get_val('evgeny@example.com'))