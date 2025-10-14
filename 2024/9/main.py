



with open('./input.prod', 'r',) as f:
    cont = f.read()[:-1]

cont = list( map(int, cont))



class DiskMap:

    def __init__(self, diskmap):
        self.diskmap = diskmap

        self.mem_sections =[]

        file_id = 0

        for i_block, block_len in enumerate(diskmap):
            if block_len==0:
                continue
            if i_block %2 ==0:
                self.mem_sections.append(MemSection(file_id, block_len))
                file_id+=1
            else:
                self.mem_sections.append(MemSection(-1, block_len))



    def mv_last_file(self):
        pass

#     def sort_allp2(self):

        # for i, mem_section in enumerate(self.mem_sections[::-1]):

            # i_mem = len(self.mem_sections)-1 - i

            # if mem_section.fileID<0:
                # continue

            # for j_fr_mem,  fr_mem_section in enumerate(self.mem_sections[:]):
                # if fr_mem_section.fileID>=0:
                    # continue

                # if mem_section.block_size>fr_mem_section.block_size:
                    # continue

                # if mem_section.block_size == fr_mem_section.block_size:
                    # self.mem_sections.pop(j_fr_mem)
                    # self.mem_sections.insert(mem_section)
                    # self.mem_sections.pop(i_mem)
                # else










   




    def sort_allp1(self):

        for i_last_mem_back, last_mem in enumerate(self.mem_sections[::-1]):
            if last_mem.fileID > -1:
                break

        i_last_mem = len(self.mem_sections)-1 - i_last_mem_back

        for i_free_block, free_block in enumerate(self.mem_sections):
            if free_block.fileID == -1:
                break




        # while i_free_block +1 < i_last_mem:
        while i_last_mem - i_free_block >1:

            if self.mem_sections[-1].fileID <0:
                self.mem_sections.pop(-1)
                continue


            free_block = self.mem_sections[i_free_block]

            # last_block = self.mem_sections[-1]
            # if last_mem.fileID ==-1:
                # self.n_empty -= last_block.block_size
                # # self.mem_sections.pop(-1)
                # return this_free_id

            ##if the last block (data) is smaller then the current free block
            if free_block.block_size > last_mem.block_size:

                # change the free block memory that will be taken up by the last block
                # self.mem_sections[this_free_id].block_size -=last_block.block_size

                # remove the old free memory
                self.mem_sections.pop(i_free_block)
                # insert the moved memory
                self.mem_sections.insert(i_free_block, MemSection(last_mem.fileID, last_mem.block_size))
                # insert the remaining free memory
                self.mem_sections.insert(i_free_block+1, MemSection(-1, free_block.block_size - last_mem.block_size))
                # remove the last memory that was just sorted
                self.mem_sections.pop(-1)





            elif free_block.block_size == last_mem.block_size:

                #remove the old free memory
                self.mem_sections.pop(i_free_block)
                #insert the moved memory
                self.mem_sections.insert(i_free_block, MemSection(last_mem.fileID, last_mem.block_size))
                # remove the last memory that was just sorted
                self.mem_sections.pop(-1)





            else: #if free_block.block_size < last_mem.block_size:

                #remove the old free memory
                self.mem_sections.pop(i_free_block)

                #insert as much of the moved memory as you can
                self.mem_sections.insert(i_free_block, MemSection(last_mem.fileID, free_block.block_size))

                # remove the last memory that was just partially sorted
                self.mem_sections.pop(-1)

                # add back the remaining memory block
                self.mem_sections.append(MemSection(last_mem.fileID, last_mem.block_size - free_block.block_size))





            for i_last_mem_back, last_mem in enumerate(self.mem_sections[::-1]):
                if last_mem.fileID > -1:
                    break
            i_last_mem = len(self.mem_sections) - i_last_mem_back


            for i_free_block, free_block in enumerate(self.mem_sections):
                if free_block.fileID == -1:
                    break

        if self.mem_sections[-1].fileID <0:
            self.mem_sections.pop(-1)

            # print(i_free_block , i_last_mem, '\t\t', self)




    def calc_checksum(self):
        checksum = 0
        ind = 0

        for mem_section in self.mem_sections:
            inds = range(ind, ind + mem_section.block_size)
            # fileIDs = [mem_section.fileID]*mem_section.block_size
            fileIDs = iter(mem_section.fileID for _ in range(mem_section.block_size))
            # print(inds, fileIDs)

            multi_map  = map(lambda x1,x2: x1*x2, inds, fileIDs)

            checksum += sum( multi_map)

            ind +=mem_section.block_size


        return checksum







    def __str__(self):
        s = ''
        for mem_section in self.mem_sections:
            s+=f'//{mem_section.fileID} for {mem_section.block_size} blocks'

        return s










class MemSection:
    def __init__(self, fileID, block_size):

        self.fileID = fileID ## -1 for free space
        self.block_size = block_size

    def __str__(self,):
        s = ''
        s+=f'ID:{self.fileID}, size:{self.block_size}'
        return s






if __name__=="__main__":

    d = DiskMap(cont)

    d.sort_all()

    print(d.calc_checksum())

    # print(d)

    # 00...111...2...333.44.5555.6666.777.888899
    # 0099.111...2...333.44.5555.6666.777.8888..
    # 00998111...2...333.44.5555.6666.777.888...
    # 009981118882...333.44.5555.6666.777.......
    # 009981118882777333.44.5555.6666...........
    # 009981118882777333644.5555.666............
    # 00998111888277733364465555.66.............
    # 0099811188827773336446555566..............


# 5120609204317 too low
# 6288599242964 too low
# 6288599492129




