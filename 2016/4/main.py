





alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'




class Room:


    def __init__(self, data):

        ###part 1
        self.data = data


        self.encrypted_name = ''.join(data.split('-')[:-1])



        self.sector_id = int(data.split('-')[-1][:-7])



        self.freq ={}
        for char in sorted(self.encrypted_name):

            if char not in self.freq.keys():
                self.freq[char] = 1
            else:
                self.freq[char] += 1


        self.prop_checksum = ''.join(data.split('[')[-1][:-1])



        self.real_checksum = ''.join(sorted(self.freq.keys(), key=lambda x:self.freq[x], reverse=True)[:5])

        self.is_valid = (self.real_checksum == self.prop_checksum)



        ###part 2

        self.shift_n = self.sector_id % 26

        
        self.encrypted_words = self.data.split('-')[:-1]


        self.decrypted_words = []
        for encrypted_word in self.encrypted_words:
            decrypted_word = ''
            for encrypted_letter in encrypted_word:
                decrypted_word += alpha[ord(encrypted_letter)-97+self.shift_n]

            self.decrypted_words.append(decrypted_word)















with open('./input.prod', 'r') as f:
    rooms = f.read().split('\n')[:-1]



# counter = 0
# for room in rooms:

    # r = Room(room)

    # if r.is_valid:
        # counter += r.sector_id

# print(counter)


target_sector_id = None
for room in rooms:
    r = Room(room)

    if 'northpole' in r.decrypted_words:
        print(r.decrypted_words, r.sector_id)







