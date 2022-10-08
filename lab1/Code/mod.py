import mmap

MEMORY =16*1024*1024*1024
CHUNKS=32
CHUNK_SIZE = int(MEMORY / CHUNKS)
FILEPATH_A = "C:/Users/user/Desktop/fileA.txt"
FILEPATH_B = "C:/Users/user/Desktop/file2.txt"
FILEPATH_C = "C:/Users/user/Desktop/file3.txt"


def readChunk(FIlEPATH,chunkNumber,CHUNK_SIZE):
    chunkNumber= chunkNumber*CHUNK_SIZE
    with open(FIlEPATH,"r+b") as file:
        mappedFile = mmap.mmap(file.fileno(),length=CHUNK_SIZE,access=mmap.ACCESS_READ,offset=chunkNumber)
        numbers=[]
        numbers = [int(num) for num in mappedFile.read().decode().split(' ')]
    return numbers

def writeChunk(FIlEPATH,number,numbers,CHUNK_SIZE):
    number=number*CHUNK_SIZE
    with open(FIlEPATH, "r+b") as file:
        mappedFile = mmap.mmap(file.fileno(),length=CHUNK_SIZE,access=mmap.ACCESS_WRITE,offset=number)
        mappedFile.write(" ".join(map(str, numbers)).encode())

def merge(FILEPATH_B,FILEPATH_C,chunkNumber,CHUNK_SIZE):
   seriesB = readChunk(FILEPATH_B,chunkNumber,CHUNK_SIZE)
   seriesC = readChunk(FILEPATH_C,chunkNumber,CHUNK_SIZE)
   numbers = []
   number = 0
   i = j = 0
   while (number < len(seriesB) and number < len(seriesC)):

      if seriesB[i] > seriesC[j]:
        numbers.append(seriesC[j])
        j += 1
      else:
        numbers.append(seriesB[i])
        i += 1
      number += 1
   if (i >= len(seriesB)):
       numbers.extend(seriesC[j:])
   elif j >= len(seriesC):
       numbers.extend(seriesB[i:])
   return numbers


def prepare(FILEPATH_A,FILEPATH_B,FILEPATH_C,CHUNK_SIZE,CHUNKS):
    chunkNumberWrite = 0
    chunkNumberRead = 0
    while chunkNumberRead <= CHUNKS:
        numbers = readChunk(FILEPATH_A, chunkNumberRead, CHUNK_SIZE)
        numbers.sort()
        writeChunk(FILEPATH_B, chunkNumberWrite, numbers, CHUNK_SIZE)

        chunkNumberRead += 1
        numbers = readChunk(FILEPATH_A, chunkNumberRead, CHUNK_SIZE)
        numbers.sort()
        writeChunk(FILEPATH_C, chunkNumberWrite, numbers, CHUNK_SIZE)

        chunkNumberRead += 1
        chunkNumberWrite += 1


def sort(FILEPATH_A,FILEPATH_B,FILEPATH_C,CHUNK_SIZE,CHUNKS):
    prepare(FILEPATH_A, FILEPATH_B, FILEPATH_C, CHUNK_SIZE, CHUNKS)
    while CHUNK_SIZE<=MEMORY:
        CHUNKS=int(CHUNKS/2)
        chunkNumberRead = 0
        while chunkNumberRead< CHUNKS:
            merge(FILEPATH_B,FILEPATH_C,chunkNumberRead,CHUNK_SIZE)
        CHUNK_SIZE*=2


        chunkNumberWrite = 0
        chunkNumberRead = 0
        while chunkNumberRead <= CHUNKS:
            numbers = readChunk(FILEPATH_A, chunkNumberRead, CHUNK_SIZE)
            writeChunk(FILEPATH_B, chunkNumberWrite, numbers, CHUNK_SIZE)
            chunkNumberRead += 1

            numbers = readChunk(FILEPATH_A, chunkNumberRead, CHUNK_SIZE)
            writeChunk(FILEPATH_C, chunkNumberWrite, numbers, CHUNK_SIZE)
            chunkNumberRead += 1
            chunkNumberWrite += 1


sort(FILEPATH_A,FILEPATH_B,FILEPATH_C,CHUNK_SIZE,CHUNKS)